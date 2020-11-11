import sys
from table import *
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

data = ['PHP','Java','Python']
    
class MyWin(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.tableWidget.setRowCount(3)
        self.ui.tableWidget.setColumnCount(2)
        
        self.ui.pushButton.clicked.connect(self.clear)
        self.ui.tableWidget.setHorizontalHeaderLabels(('Метод', 'Действие'))
        self.ui.tableWidget.setVerticalHeaderLabels(('#1', '#2', '#3'))



        row = 0
        for item in data:
            cellinfo = QTableWidgetItem(item)
            #cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            combo = QtWidgets.QComboBox()
            combo.addItem('Изучить')
            combo.addItem('Удалить')
            combo.addItem('Забыть')
            
            self.ui.tableWidget.setItem(row, 0, cellinfo)
            self.ui.tableWidget.setCellWidget(row, 1, combo)
            row +=1
            
            #progress = QtWidgets.QProgressBar()
            #progress.setMinimum(0)
            #progress.setMaximum(100)


           #progress.setValue(item[1])
            #progress.setFormat('{0:.2f}%'.format (item[1]))
            #col +=1
            #self.ui.tableWidget.setCellWidget(line, 1, progress)
            #line += 1
            #row +=1
        #self.ui.tableWidget.sortByColumn(0,QtCore.Qt.AscendingOrder)

        
    def clear(self):
        self.ui.tableWidget.clear()
        
                    
 
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    
    sys.exit(app.exec_())
