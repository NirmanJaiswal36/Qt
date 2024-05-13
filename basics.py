from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
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
        self.show()
        
if __name__== '__main__':
    app = QApplication(sys.argv)
    mw = App()
    
    sys.exit(app.exec())