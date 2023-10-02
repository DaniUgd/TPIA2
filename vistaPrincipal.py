from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QMessageBox
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import funciones
import init
import matplotlib.pyplot as plt

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(882, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 20, 811, 501))
        self.widget.setObjectName("widget")

        layout = QVBoxLayout(self.widget)
        self.canvas = init.MplCanvas(self, width=5, height=4)
        layout.addWidget(self.canvas)
        self.toolbar = NavigationToolbar((self.canvas), self)
        layout.addWidget(self.toolbar)

        self.btn_kmeans = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kmeans.setGeometry(QtCore.QRect(300, 570, 101, 31))
        self.btn_kmeans.setObjectName("btn_kmeans")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 530, 201, 21))
        self.label.setObjectName("label")
        self.dataset1 = QtWidgets.QRadioButton(self.centralwidget)
        self.dataset1.setGeometry(QtCore.QRect(30, 530, 121, 21))
        self.dataset1.setObjectName("dataset1")
        self.dataset2 = QtWidgets.QRadioButton(self.centralwidget)
        self.dataset2.setGeometry(QtCore.QRect(30, 560, 121, 21))
        self.dataset2.setObjectName("dataset2")
        self.dataset3 = QtWidgets.QRadioButton(self.centralwidget)
        self.dataset3.setGeometry(QtCore.QRect(30, 590, 121, 21))
        self.dataset3.setObjectName("dataset3")
        self.n_cluster = QtWidgets.QLineEdit(self.centralwidget)
        self.n_cluster.setGeometry(QtCore.QRect(510, 530, 51, 20))
        self.n_cluster.setObjectName("n_cluster")
        self.btn_kmeanspp = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kmeanspp.setGeometry(QtCore.QRect(460, 570, 101, 31))
        self.btn_kmeanspp.setObjectName("btn_kmeanspp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu Principal"))
        self.btn_kmeans.setText(_translate("MainWindow", "KMEANS"))
        self.label.setText(_translate("MainWindow", "INGRESAR LA CANTIDAD DE CLUSTERS"))
        self.dataset1.setText(_translate("MainWindow", "DATA_SET1"))
        self.dataset2.setText(_translate("MainWindow", "DATA_SET2"))
        self.dataset3.setText(_translate("MainWindow", "DATA_SET3"))
        self.btn_kmeanspp.setText(_translate("MainWindow", "KMEANS++"))
        
    def abrirKmeans(self):
        if(self.n_cluster.text() != ''):
            n_cluster = int(self.n_cluster.text())
            if(n_cluster>1 and n_cluster<6):
                tipo_dataset = 0
                if self.dataset1.isChecked():
                    tipo_dataset = 1
                elif self.dataset2.isChecked():
                    tipo_dataset = 2
                elif self.dataset3.isChecked():        
                    tipo_dataset = 3
                if(n_cluster != None and tipo_dataset != 0):
                    dataset=funciones.recuperadata(tipo_dataset)
                    self.vistak = init.vistaKmeans(dataset,n_cluster)
                    self.vistak.show()
                else:
                    QMessageBox.information(None, "Error", "Debe seleccionar el tipo de DataSet.")
            else:
                QMessageBox.information(None, "Error", "Debe seleccionar el cluster dentro del rango permitido.")
        else:
            QMessageBox.information(None, "Error", "Debe seleccionar el cluster dentro del rango permitido.")    
    def abrirKmeanspp(self):
        if(self.n_cluster.text() != ''):
            n_cluster = int(self.n_cluster.text())
            if(n_cluster>1 and n_cluster<6):
                tipo_dataset = 0
                if self.dataset1.isChecked():
                    tipo_dataset = 1
                elif self.dataset2.isChecked():
                    tipo_dataset = 2
                elif self.dataset3.isChecked():        
                    tipo_dataset = 3
                if(n_cluster != None and tipo_dataset != 0):
                    dataset=funciones.recuperadata(tipo_dataset)
                    self.vistakpp = init.vistaKmeanspp(dataset,n_cluster)
                    self.vistakpp.show()
                else:
                    QMessageBox.information(None, "Error", "Debe seleccionar el tipo de DataSet.")
            else:
                QMessageBox.information(None, "Error", "Debe seleccionar el cluster dentro del rango permitido.")
        else:
            QMessageBox.information(None, "Error", "Debe seleccionar el cluster dentro del rango permitido.")            
    def setearDataset(self,i):
        self.canvas.axes.clear() 
        dataSET = funciones.recuperadata(i)
        funciones.graficar_dataset(self.canvas.axes, dataSET)
        
        self.canvas.draw()



