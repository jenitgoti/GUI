class CalibrationWorker(QObject):
    progress = Signal(str)
    finished = Signal(bool, str)

    SOURCES = [
        "/opt/ros/humble/setup.bash",
        "/root/ur_ws_sim/install/setup.bash",
    ]
    SCRIPTS_DIR = "/root/ur_ws_sim/tools/scripts"

    def __init__(self, base_dir: str, params: dict, parent=None):
        super().__init__(parent)
        self.base_dir = base_dir
        self.params = params  # ✅ store user inputs here

    def _script(self, name: str) -> str:
        p = os.path.join(self.SCRIPTS_DIR, name)
        if not os.path.exists(p):
            raise FileNotFoundError(f"Script not found: {p}")
        return p

    def _run_one(self, title: str, args: list[str], cwd: str):
        self.progress.emit(title)

        if args and args[0] == "python3":
            args[0] = sys.executable

        sources_existing = []
        for s in self.SOURCES:
            if os.path.exists(s):
                sources_existing.append(s)
            else:
                print(f"[WARN] source file not found: {s}")

        source_cmd = " && ".join(f"source {shlex.quote(s)}" for s in sources_existing)
        run_cmd = " ".join(shlex.quote(x) for x in args)
        bash_cmd = f"set -e; {source_cmd} && {run_cmd}" if source_cmd else f"set -e; {run_cmd}"

        subprocess.run(["bash", "-lc", bash_cmd], cwd=cwd, check=True)

    @Slot()
    def run(self):
        try:
            scripts_cwd = self.SCRIPTS_DIR

            # ✅ take run_id from GUI
            run_id = str(self.params.get("run_id", "")).strip()
            if not run_id:
                raise RuntimeError("run_id is empty. Please enter a Run ID in the GUI.")

            # ✅ take camera selection from GUI (or default False)
            use_realsense = bool(self.params.get("use_realsense", False))
            use_webcam = bool(self.params.get("use_webcam", False))

            # Build cameras list exactly as needed: --cameras realsense webcam
            cameras = []
            if use_realsense:
                cameras.append("realsense")
            if use_webcam:
                cameras.append("webcam")
            if not cameras:
                raise RuntimeError("No cameras selected for calibration")

            # Step 1
            args = [
                "python3", self._script("multi_camera_calibration.py"),
                "--run-id", run_id,
                "--nx", "7",
                "--ny", "10",
                "--square-size", "0.025",
                "--cameras", *cameras,
            ]

            self._run_one(
                "Step 1/4: Multi-camera calibration …",
                args,
                cwd=scripts_cwd,
            )

            # Step 2
            self._run_one(
                "Step 2/4: Pose estimation (PnP) …",
                [
                    "python3",
                    self._script("multi_camera_PnP.py"),
                    "--run-id", run_id,
                    "--nx", "7",
                    "--ny", "10",
                    "--square-size", "0.022",
                    "--cameras", *cameras,
                ],
                cwd=scripts_cwd,
            )

            # Step 3
            self._run_one(
                "Step 3/4: Hand–eye calibration …",
                [
                    "python3",
                    self._script("multi_sensor_handeye_opt.py"),
                    "--run-id", run_id,
                    "--no-of-runs", "10",
                    "--cameras", *cameras,
                ],
                cwd=scripts_cwd,
            )

            # Step 4
            self._run_one(
                "Step 4/4: Creating calibration report …",
                [
                    "python3",
                    self._script("generate_multi_sensor_report.py"),
                    "--base-dir", "/root/ur_ws_sim/data",
                    "--run-id", run_id,
                    "--cameras", *cameras,
                ],
                cwd=scripts_cwd,
            )

        except FileNotFoundError as e:
            traceback.print_exc()
            self.finished.emit(False, str(e))
            return
        except subprocess.CalledProcessError as e:
            traceback.print_exc()
            self.finished.emit(False, f"Command failed with exit code {e.returncode}.")
            return
        except Exception as e:
            traceback.print_exc()
            self.finished.emit(False, f"Unexpected error:\n{e}")
            return

        self.finished.emit(True, "Calibration pipeline completed successfully.")
