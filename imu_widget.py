from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import QTimer
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

class IMUVisualizer(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vector = np.array([0.0, 0.0, 0.0])
        self.width = 1
        self.height = 1

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(16)  # ~60 FPS

    def set_vector(self, x, y, z):
        self.vector = np.array([x, y, z])

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.1, 0.1, 0.1, 1.0)

    def resizeGL(self, w, h):
        self.width = w
        self.height = h
        glViewport(0, 0, w, h)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, self.width / self.height if self.height != 0 else 1, 1, 100)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)  # angled camera view

        self.draw_axis()
        self.draw_vector(self.vector, (1, 1, 0))  # Yellow vector

    def draw_axis(self):
        axis_length = 1.0
        circle_radius = axis_length
        segments = 64

        # Axis lines
        glBegin(GL_LINES)
        # X - Red
        glColor3f(1, 0, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(axis_length, 0, 0)
        # Y - Green
        glColor3f(0, 1, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(0, axis_length, 0)
        # Z - Blue
        glColor3f(0, 0, 1)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, axis_length)
        glEnd()

        # Circle in YZ (around X axis)
        glColor3f(0.5, 0.5, 0.5)
        glBegin(GL_LINE_LOOP)
        for i in range(segments):
            angle = 2 * np.pi * i / segments
            y = circle_radius * np.cos(angle)
            z = circle_radius * np.sin(angle)
            glVertex3f(0, y, z)
        glEnd()

        # Circle in XZ (around Y axis)
        glBegin(GL_LINE_LOOP)
        for i in range(segments):
            angle = 2 * np.pi * i / segments
            x = circle_radius * np.cos(angle)
            z = circle_radius * np.sin(angle)
            glVertex3f(x, 0, z)
        glEnd()

        # Circle in XY (around Z axis)
        glBegin(GL_LINE_LOOP)
        for i in range(segments):
            angle = 2 * np.pi * i / segments
            x = circle_radius * np.cos(angle)
            y = circle_radius * np.sin(angle)
            glVertex3f(x, y, 0)
        glEnd()

    def draw_vector(self, vec, color):
        glColor3f(*color)
        glLineWidth(3)
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(*vec)
        glEnd()
        glLineWidth(1)

