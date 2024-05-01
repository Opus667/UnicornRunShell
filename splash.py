from PyQt5.QtWidgets import QSplashScreen, QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap

app = QApplication([])

pixmap = QPixmap("unipuke_512.png")

splash = QSplashScreen()
splash.setPixmap(pixmap)

QTimer.singleShot(3000,splash.close)
QTimer.singleShot(3000, app.quit)

splash.show()
app.exec_()