import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class CustomMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gráfico en una ventana personalizada de Qt")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        self.canvas = MplCanvas(self, width=5, height=4)
        layout.addWidget(self.canvas)

        self.toolbar = NavigationToolbar(self.canvas, self)
        layout.addWidget(self.toolbar)

        self.plot()

    def plot(self):
        # Ejemplo de gráfico
        x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(x)
        self.canvas.axes.plot(x, y)
        self.canvas.draw()

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CustomMainWindow()
    main_window.show()
    sys.exit(app.exec_())
