import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)
        self.drawB.clicked.connect(self.drawf)

    def drawf(self):
        self.do_paint = True
        self.update()

    def draw(self):
        R = randint(20, 100)
        self.qp.setBrush(QColor(*[randint(0, 255) for _ in range(3)]))
        self.qp.drawEllipse(150, 150, R, R)

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
