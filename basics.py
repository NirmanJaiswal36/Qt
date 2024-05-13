from turtle import onclick
from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton, QLineEdit, QMessageBox, QAction
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

        self.textbox = QLineEdit(self)
        self.textbox.move(5,20)
        self.textbox.resize(300,100)

        self.button = QPushButton("Show Text",self)
        self.button.move(100,150)
        self.button.setToolTip("shows the text written in a message box")
        self.button.clicked.connect(self.onclick)
        self.show()
    
    @pyqtSlot()

    def onclick(self):
        text = self.textbox.text()
        QMessageBox.question(self,"Message","You typed: \n"+text,QMessageBox.Ok,QMessageBox.Ok)
        self.textbox.setText("")

        
if __name__== '__main__':
    app = QApplication(sys.argv)
    mw = App()
    
    sys.exit(app.exec())