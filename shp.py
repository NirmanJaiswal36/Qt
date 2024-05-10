from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsPolygonItem, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QColor, QPolygonF, QBrush
import shapefile


class ShapefileViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shapefile Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.zoom_factor = 1.0

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.scale(0.001,0.001)
        self.setCentralWidget(self.view)

        self.import_button = QPushButton("Import File")
        self.import_button.clicked.connect(self.import_file)

        layout = QVBoxLayout()
        layout.addWidget(self.import_button)
        layout.addWidget(self.view)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def import_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Shapefile", "", "Shapefiles (*.shp)")
        if filename:
            self.load_shapefile(filename)

    def load_shapefile(self, filename):
        self.scene.clear()
        sf = shapefile.Reader(filename)
        shapes = sf.shapes()

        for shape in shapes:
            points = [QPointF(point[0], -point[1]) for point in shape.points]  # Flip y-coordinate
            polygon = QPolygonF(points)
            polygon_item = QGraphicsPolygonItem(polygon)
            polygon_item.setBrush(QBrush(QColor(52, 165, 111)))
            self.scene.addItem(polygon_item)

    def wheelEvent(self, event):
        zoom_in_factor = 1.25
        zoom_out_factor = 1 / zoom_in_factor

        if event.angleDelta().y() > 0:
            self.zoom_factor *= zoom_in_factor
        else:
            self.zoom_factor *= zoom_out_factor

        self.view.scale(zoom_in_factor, zoom_in_factor)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = ShapefileViewer()
    window.show()
    sys.exit(app.exec_())
