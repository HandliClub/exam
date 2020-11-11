import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.text = 'Начало'
        self.text1 = 't'
        self.text2 = 'q = t * t'
        self.text3 = 'q'
        self.text4 = 'Вывод'
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

        qp.setPen(pen)
        qp.drawEllipse(90, 5, 80, 20)

        qp.setPen(pen)
        qp.drawText(110, 18, self.text)

        qp.setPen(pen)
        qp.drawText(130, 53, self.text1)

        qp.setPen(pen)
        qp.drawText(110, 95, self.text2)

        qp.setPen(pen)
        qp.drawText(130, 132, self.text3)

        qp.setPen(pen)
        qp.drawText(110, 175, self.text4)
        
        qp.setPen(pen)
        qp.drawLine(130, 25, 130, 40)
#############Параллелограмм
        qp.setPen(pen)
        qp.drawLine(100, 40, 200, 40)

        qp.setPen(pen)
        qp.drawLine(80, 60, 180, 60)

        qp.setPen(pen)
        qp.drawLine(80, 60, 100, 40)

        qp.setPen(pen)
        qp.drawLine(180, 60, 200, 40)
##############
        
        qp.setPen(pen)
        qp.drawLine(130, 60, 130, 80)

        
##############прямоугольник
        qp.setPen(pen)
        qp.drawLine(80, 80, 180, 80)

        qp.setPen(pen)
        qp.drawLine(80, 100, 180, 100)

        qp.setPen(pen)
        qp.drawLine(80, 80, 80, 100)

        qp.setPen(pen)
        qp.drawLine(180, 80, 180, 100)

##############
        
        qp.setPen(pen)
        qp.drawLine(130, 100, 130, 120)

#############Параллелограмм
        qp.setPen(pen)
        qp.drawLine(100, 120, 200, 120)

        qp.setPen(pen)
        qp.drawLine(80, 140, 180, 140)

        qp.setPen(pen)
        qp.drawLine(80, 140, 100, 120)

        qp.setPen(pen)
        qp.drawLine(180, 140, 200, 120)
################
        qp.setPen(pen)
        qp.drawLine(130, 140, 130, 160)
        
        qp.setPen(pen)
        qp.drawEllipse(90, 160, 80, 20)
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
