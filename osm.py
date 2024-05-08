import sys
import osmnx as ox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OSMnx Map Viewer")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        self.plot_map()

    def plot_map(self):
        # Retrieve geographic data using OSMnx
        gdf = ox.geocode_to_gdf("Gujarat, India")
        
        # Create a figure and axes for the plot
        fig, ax = plt.subplots()
        
        # Plot the geographic data
        gdf.plot(ax=ax)
        
        # Embed the plot in a PyQt5 canvas
        canvas = FigureCanvas(fig)
        self.layout.addWidget(canvas)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec_())
