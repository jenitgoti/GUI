

class EmbeddedTerminal(QWidget):
    """
    A closable terminal-like widget that runs a command with QProcess
    and streams its output to a text box.
    """
    def __init__(self, command, title="Command Output", parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        # Log area
        self.text_area = QPlainTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setFont(QFont("Monospace", 10))
        self.text_area.appendPlainText(f">>> {title}\n")
        layout.addWidget(self.text_area)

        # Button row
        btn_layout = QHBoxLayout()
        self.stop_btn = QPushButton("Stop")
        self.stop_btn.clicked.connect(self.stop_process)
        btn_layout.addWidget(self.stop_btn)

        self.close_btn = QPushButton("Close")
        self.close_btn.clicked.connect(self.close_terminal)
        btn_layout.addWidget(self.close_btn)

        layout.addLayout(btn_layout)

        # QProcess
        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.on_ready_read)
        self.process.finished.connect(self.on_finished)

        # Start process
        self.process.start(command[0], command[1:])

    def on_ready_read(self):
        data = bytes(self.process.readAllStandardOutput()).decode("utf-8")
        self.text_area.insertPlainText(data)
        self.text_area.moveCursor(QTextCursor.End)

    def on_finished(self, exit_code, exit_status):
        self.text_area.appendPlainText(f"\n\nProcess finished with exit code {exit_code}.")

    def stop_process(self):
        if self.process and self.process.state() == QProcess.Running:
            self.process.kill()
            self.text_area.appendPlainText("\n\nProcess was terminated by user.")

    def close_terminal(self):
        if self.process and self.process.state() == QProcess.Running:
            self.process.kill()
        self.setParent(None)  # removes widget from layout
        self.deleteLater()


class ConnectArmWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Always start from stackedWidget_3(0)
        self.ui.stackedWidget_3.setCurrentIndex(0)

        # Disable all top buttons manually (except by code)
        for btn in [
            self.ui.pushButton,
            self.ui.pushButton_2,
            self.ui.pushButton_3,
            self.ui.pushButton_4,
            self.ui.pushButton_5,
            self.ui.pushButton_6
        ]:
            btn.setEnabled(False)
            btn.setCheckable(True)  # Needed to change icon to "on" image when checked

        

        # Connect flow buttons to next steps
        self.ui.congigureBtn.clicked.connect(self.config)
        self.ui.roscoreBtn.clicked.connect(self.roscore)
        self.ui.calibrateBtn.clicked.connect(self.calibrate)
        self.ui.launchdriverBtn.clicked.connect(self.driver)
        self.ui.launchmoveitBtn_2.clicked.connect(self.moveit)


        # Map UI buttons to actions

        # Map UI buttons to actions
        self.ui.congigureBtn.clicked.connect(self.config_ip)
        self.ui.roscoreBtn.clicked.connect(self.start_roscore)
        self.ui.calibrateBtn.clicked.connect(self.calibrate_robot)
        self.ui.launchdriverBtn.clicked.connect(self.launch_driver)
        self.ui.launchmoveitBtn_2.clicked.connect(self.launch_moveit)
        

        self.ui.pushButton_7.clicked.connect(self.run_half_sphere)
        self.ui.pushButton_8.clicked.connect(self.run_plane)
        

    def config(self):

        self.ui.stackedWidget_3.setCurrentIndex(5)
        self.ui.pushButton.setChecked(True) 
        
    def roscore(self):
        

        self.ui.stackedWidget_3.setCurrentIndex(4)
        self.ui.pushButton_2.setChecked(True)
        
    def calibrate(self):

        self.ui.stackedWidget_3.setCurrentIndex(3)
        self.ui.pushButton_3.setChecked(True)
        

    def driver(self):
        self.ui.stackedWidget_3.setCurrentIndex(2)
        self.ui.pushButton_4.setChecked(True)
        

    def moveit(self):
        
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.ui.pushButton_5.setChecked(True)

   

   


    def get_full_ip(self, entry_field):
        try:
            ip = entry_field.text().strip()
        except Exception as e:
            print("Invalid widget passed to get_full_ip:", e)
            return None

    # Basic IPv4 pattern check
        ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
        if not re.match(ip_pattern, ip):
            self.show_ip_error("Invalid IP format. Enter a valid IP like 192.168.1.10.")
            self.ui.stackedWidget_3.setCurrentIndex(0)
            self.ui.pushButton.setChecked(False)
            return None

    # Ensure each octet is in 0–255
        parts = ip.split(".")
        if any(not part.isdigit() or not (0 <= int(part) <= 255) for part in parts):
            self.show_ip_error("Each part of IP must be between 0 and 255.")
            self.ui.stackedWidget_3.setCurrentIndex(0)
            self.ui.pushButton.setChecked(False)
            return None

        return ip

    def show_ip_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Invalid IP Address")
        msg.setText(message)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: white;
                color: black;
            }
            QMessageBox QLabel {
                background-color: white;
                color: black;
            }
            QMessageBox QPushButton {
                background-color: #f0f0f0;
                color: black;
            }
        """)
        msg.exec()

    def show_password_dialog(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Sudo Password")
        dialog.setLabelText("Enter your sudo password:")
        dialog.setTextEchoMode(QLineEdit.EchoMode.Password)

        dialog.setStyleSheet("""
            QInputDialog {
                background-color: white;
                color: black;
            }
            QLabel {
                color: black;
            }
            QLineEdit {
                background-color: white;
                color: black;
            }
            QPushButton {
                background-color: #f0f0f0;
                color: black;
            }
        """)

        ok = dialog.exec()
        password = dialog.textValue()
        return password, ok == QDialog.DialogCode.Accepted

    
    def run_sudo_command(self, command):
        robot_ip = self.get_full_ip(self.ui.Robot_IP)
        if not robot_ip:
            return 
        if not hasattr(self, 'terminal_3_text_edit'):
        # Dynamically create QTextEdit widget if not already created
            self.terminal_3_text_edit = QTextEdit(self.ui.right_main_cointainer)
            self.terminal_3_text_edit.setObjectName("terminal_3")
            self.ui.verticalLayout.addWidget(self.terminal_3_text_edit)  # Add to layout
    
        password, accepted = self.show_password_dialog()
        if accepted and password:
                try:
                    sudo_command = f"echo '{password}' | sudo -S {command}; echo 'Press Enter to close...'; read"
            

                    proc = subprocess.Popen(
                        ['gnome-terminal', '--', 'bash', '-c', sudo_command],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                    )
                    stdout, stderr = proc.communicate(password + '\n')

                    if proc.returncode == 0:
                        self.terminal_3_text_edit.append("✅ Command succeeded!\n" + stdout)
                        QTimer.singleShot(4000, lambda : self.run_command("bash robot_control.sh config_ip_2 dummy {robot_ip}; exec bash", "pinging robot ip"))
                    else:
                        self.terminal_3_text_edit.append("❌ Command failed!\n" + stderr)
                except Exception as e:
                    self.terminal_3_text_edit.append(f"⚡ Exception: {str(e)}")
        else:
                self.terminal_3_text_edit.append("⚡ No password entered.")



    def run_command(self, command, title=""):
        
        if not hasattr(self, 'terminal_3_text_edit'):
        # Dynamically create QTextEdit widget if not already created
            self.terminal_3_text_edit = QTextEdit(self.ui.right_main_cointainer)
            self.terminal_3_text_edit.setObjectName("terminal_3")
            self.ui.verticalLayout.addWidget(self.terminal_3_text_edit)  # Add to layout
    
        self.terminal_3_text_edit.append(f"\n>>> {title or command}\n")  # Append command title
        try:
            subprocess.Popen(
                ['gnome-terminal', '--', 'bash', '-i', '-c', command],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            self.terminal_3_text_edit.append(f"{title} launched in new terminal.\n")  # Log success
        except Exception as e:
            self.terminal_3_text_edit.append(f"Error: {str(e)}\n")  # Log errors if any


    
    
    
    


   
    def config_ip(self):
        pc_ip = self.get_full_ip(self.ui.PC_IP)
        robot_ip = self.get_full_ip(self.ui.Robot_IP)
        if not pc_ip or not robot_ip:
            return # Prevents execution if validation fails
        # Ask for sudo password
        

        
        self.show_ip_error(f"\n>>> Configuring IP for {pc_ip} and pinging {robot_ip}\n")

       
        self.run_sudo_command("bash robot_control.sh config_ip dummy {pc_ip} {robot_ip}")
        


    def start_roscore(self):
        self.run_command("bash robot_control.sh start_roscore", "Start ROS Core")


    def calibrate_robot(self):
        robot_ip = self.get_full_ip(self.ui.Robot_IP)
        if not robot_ip:
            return

        self.run_command(f"bash robot_control.sh calibrate_robot dummy {robot_ip}", "Launch Calibration")


    def launch_driver(self):
        robot_ip = self.get_full_ip(self.ui.Robot_IP)
        if not robot_ip:
            return

        self.run_command(f"bash robot_control.sh launch_driver dummy {robot_ip}", "Launch Robot Driver")

        
    def launch_moveit(self):
        self.run_command("bash robot_control.sh launch_moveit", "Launch MoveIt")


    def run_plane(self):
        self.run_command("bash robot_control.sh run_plane", "Run plane.py")

    def run_half_sphere(self):
        self.run_command("bash robot_control.sh run_half_sphere", "Run half_sphere.py")


