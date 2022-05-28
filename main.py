from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget , QWidget, QPushButton
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt, pyqtSlot
import sys
import os


linux_user = ''
icons = ['❌', '🔐', '🛑', '🔁']
if sys.platform == "linux":
    sysos = "Linux"
    linux_user = os.getlogin()
elif sys.platform == "win32" or "win64":
    sysos = "Windows"

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.appUi()

    def appUi(self):
        # Base UI
        self.WIDTH = 300
        self.HEIGHT = 160
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.center()
        self.setWindowTitle("Power Menu")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.mainwindow = QWidget(self)
        self.mainwindow.resize(self.WIDTH, self.HEIGHT)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.9)
        # UI
        radius = 8
        self.mainwindow.setStyleSheet(
            """
            background-color: #33383d;
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )
        self.exitbtn()
        self.outbtn()
        self.shutbtn()
        self.rebtn()

        # Show Window
        self.show()
    
    # Buttons

    def exitbtn(self):
        icon = icons[0]
        clsbtn = QPushButton(icon, self)
        clsbtn.move(self.WIDTH - 35,0)
        clsbtn.resize(35,35)
        clsbtn.clicked.connect(self.on_exit)
        clsbtn.setStyleSheet("background-color: transparent;font-size:16px;")

    def outbtn(self):
        icon = icons[1]
        clsbtn = QPushButton(icon, self)
        clsbtn.move(int(self.WIDTH / 2 - 135), int(self.HEIGHT - 140))
        clsbtn.resize(120,120)
        clsbtn.clicked.connect(self.on_logout)
        clsbtn.setStyleSheet("background-color: transparent;font-size:35px;")
    
    def shutbtn(self):
        icon = icons[2]
        clsbtn = QPushButton(icon, self)
        clsbtn.move(int(self.WIDTH / 2 - 57), 20)
        clsbtn.resize(120,120)
        clsbtn.clicked.connect(self.on_shut)
        clsbtn.setStyleSheet("background-color: transparent;font-size:35px;")

    def rebtn(self):
        icon = icons[3]
        clsbtn = QPushButton(icon, self)
        clsbtn.move(int(self.WIDTH / 2 + 30), 20)
        clsbtn.resize(120,120)
        clsbtn.clicked.connect(self.on_restart)
        clsbtn.setStyleSheet("background-color: transparent;font-size:35px;")

    @pyqtSlot()
    def on_exit(self):
        exit()

    def on_logout(self):
        if sysos == "Linux":
            os.system('pkill -KILL -u ' + linux_user)
        elif sysos == "Windows":
            os.system("Rundll32.exe user32.dll,LockWorkStation")
    
    def on_shut(self):
        if sysos == "Linux":
            os.system("poweroff")
        elif sysos == "Windows":
            os.system("shutdown")

    def on_restart(self):
        if sysos == "Linux":
            os.system("reboot")
        elif sysos == "Windows":
            os.system("Restore-Computer")


    # Settings
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.moveFlag = False

    # Center Window
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft()) 
    
 
# Start
try:
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
except:
    exit()
