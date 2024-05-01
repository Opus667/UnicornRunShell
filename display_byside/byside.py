from PyQt5.QtWidgets import QSplashScreen, QApplication #, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from subprocess import run  

app = QApplication([])

pixmap = QPixmap("unipuke_512.png")

comando = ["/usr/local/bin/displayplacer", "id:733B270D-2AC6-9A82-DE5D-D12F507D9322 res:1920x1080 hz:60 color_depth:8 enabled:true scaling:off origin:(2560,520) degree:180"]

execucao = run(comando)

splash = QSplashScreen()
splash.setPixmap(pixmap)

QTimer.singleShot(10000, splash.close)
QTimer.singleShot(5000, app.quit)

splash.show()

# label = QLabel("Fuck World!")
# label.show()

app.exec_()