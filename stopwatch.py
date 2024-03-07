from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt, QRectF
from PyQt5.QtGui import QPainter, QBrush, QPainterPath, QRegion, QFont
from style import STYLESHEET

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Stopwatch')
        self.setGeometry(100, 100, 300, 200)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(STYLESHEET)
        self.setWindowOpacity(1.0)

        layout = QVBoxLayout()
        self.label = QLabel('00:00:000', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 40))
        layout.addWidget(self.label)

        self.startButton = QPushButton('Start', self)
        self.startButton.clicked.connect(self.startTimer)
        layout.addWidget(self.startButton)

        self.pauseButton = QPushButton('Pause', self)
        self.pauseButton.clicked.connect(self.pauseTimer)
        layout.addWidget(self.pauseButton)

        self.resetButton = QPushButton('Reset', self)
        self.resetButton.clicked.connect(self.resetTimer)
        layout.addWidget(self.resetButton)

        self.exitButton = QPushButton('Exit', self)
        self.exitButton.clicked.connect(self.close)
        layout.addWidget(self.exitButton)

        self.setLayout(layout)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)
        self.elapsedTime = QTime(0, 0, 0)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        rect = self.rect()
        path.addRoundedRect(QRectF(rect), 20.0, 20.0)
        painter.fillPath(path, QBrush(self.palette().window().color()))
        self.setMask(QRegion(path.toFillPolygon().toPolygon()))
        painter.end()

    def startTimer(self):
        if not self.timer.isActive():
            self.timer.start(1)
            self.elapsedTime.start()

    def pauseTimer(self):
        if self.timer.isActive():
            self.timer.stop()
            elapsed = self.elapsedTime.elapsed()
            self.elapsedTime = QTime(0, 0, 0)
            self.elapsedTime = self.elapsedTime.addMSecs(elapsed)

    def resetTimer(self):
        self.timer.stop()
        self.elapsedTime = QTime(0, 0, 0)
        self.label.setText('00:00:000')

    def updateTimer(self):
        time = self.elapsedTime.elapsed()
        ms = time % 1000
        seconds = int(time / 1000)
        m, s = divmod(seconds, 60)
        self.label.setText(f'{m:02}:{s:02}:{ms:03}')
