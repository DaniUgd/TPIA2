from vistaPrincipal import Ui_MainWindow
from vistaKmeans import Kmeans
from vistaKmeanspp import Kmeanspp
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import funciones

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)

class vistaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        validator = QRegExpValidator(QRegExp("^(?:[2-5]|[1-9])$"), self.ui.n_cluster)
        self.ui.n_cluster.setValidator(validator)
        self.ui.btn_kmeans.clicked.connect(self.ui.abrirKmeans)
        self.ui.btn_kmeanspp.clicked.connect(self.ui.abrirKmeanspp)
        self.ui.dataset1.clicked.connect(lambda: self.ui.setearDataset(1))
        self.ui.dataset2.clicked.connect(lambda: self.ui.setearDataset(2))
        self.ui.dataset3.clicked.connect(lambda: self.ui.setearDataset(3))

class vistaKmeans(QMainWindow):
    def __init__(self,dataset,n_cluster):
        super().__init__()
        self.ui = Kmeans()
        self.ui.setupUi(self)  
        self.ui.i = 0  
        self.ui.estado = 0  
        centroides=funciones.generaAleatorio(dataset,n_cluster)
        listaCentroides = []
        listaCentroides=funciones.iteraKmeans(dataset,centroides,n_cluster,50)
        funciones.inicia_grafico(dataset,listaCentroides,n_cluster,self.ui)
        self.ui.btn_siguiente.clicked.connect(lambda: funciones.graficar_siguiente(dataset,listaCentroides,n_cluster,self.ui))
        self.ui.btn_anterior.clicked.connect(lambda: funciones.graficar_anterior(dataset,listaCentroides,n_cluster,self.ui))
        self.ui.btn_iniciar.clicked.connect(lambda: funciones.graficar_en_bucle(dataset,listaCentroides,n_cluster,self.ui))
        self.ui.btn_parar.clicked.connect(lambda: funciones.detener_grafico(self.ui))

class vistaKmeanspp(QMainWindow):
    def __init__(self,dataset,n_cluster):
        super().__init__()
        self.ui = Kmeanspp()
        self.ui.setupUi(self)  
        self.ui.i = 0  
        self.ui.estado = 0  
        centroides=funciones.kmeans_plus(dataset,n_cluster)
        listaCentroides = []
        listaCentroides=funciones.iteraKmeans(dataset,centroides,n_cluster,50)
        funciones.inicia_grafico(dataset,listaCentroides,n_cluster,self.ui)
        self.ui.btn_siguientepp.clicked.connect(lambda: funciones.graficar_siguiente(dataset,listaCentroides,n_cluster,self.ui))
        self.ui.btn_anteriorpp.clicked.connect(lambda: funciones.graficar_anterior(dataset,listaCentroides,n_cluster,self.ui))
        self.ui.btn_iniciarpp.clicked.connect(lambda: funciones.graficar_en_bucle(dataset,listaCentroides,n_cluster,self.ui))
        self.ui.btn_pararpp.clicked.connect(lambda: funciones.detener_grafico(self.ui))