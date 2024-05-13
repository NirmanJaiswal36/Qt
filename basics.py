from turtle import onclick
from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton
from PyQt5.QtGui import QIcon
import sys

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Main Window"
        self.initUI()
    
    

    
    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(100,100,300,300)
        self.button = QPushButton("Import Shapefile",self)
        self.button.move(10,20)
        self.button.clicked.connect(self.onclick)
        self.show()
    
    @pyqtSlot()

    def onclick(self):
        print("Shapefile imported")
        
if __name__== '__main__':
    app = QApplication(sys.argv)
    mw = App()
    
    sys.exit(app.exec())