import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add a title
        self.setWindowTitle("Hello World")

        # Set Layout
        self.setLayout(qtw.QVBoxLayout())

        #Create a Label
        my_label = qtw.QLabel("Hello World!")
        self.layout().addWidget(my_label)
        self.show()
        
app = qtw.QApplication([])
mw = MainWindow()

#Run the app
app.exec_()

