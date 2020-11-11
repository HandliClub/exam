import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 280, 250)
        self.setWindowTitle('Pen')
        self.show()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()


    def drawLines(self, qp):

        pen = QPen(Qt.black, 2, Qt.SolidLine)
        pen.setStyle(Qt.DashLine)
        qp.setPen(QPen(Qt.green,  8, Qt.DashLine))

        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(40, 40, 200, 160)

        qp.setBrush(QColor(255, 255, 255))




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
