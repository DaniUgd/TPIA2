from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout,QMainWindow
from PyQt5.QtCore import QTimer, QCoreApplication
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import funciones
import init
import time

class Kmeans(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 656)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 10, 841, 561))
        self.widget.setObjectName("widget")

        layout = QVBoxLayout(self.widget)
        self.canvas = init.MplCanvas(self, width=5, height=4)
        layout.addWidget(self.canvas)
        self.toolbar = NavigationToolbar((self.canvas), self)
        layout.addWidget(self.toolbar)

        self.btn_anterior = QtWidgets.QPushButton(self.centralwidget)
        self.btn_anterior.setGeometry(QtCore.QRect(50, 600, 111, 31))
        self.btn_anterior.setObjectName("btn_anterior")
        self.btn_siguiente = QtWidgets.QPushButton(self.centralwidget)
        self.btn_siguiente.setGeometry(QtCore.QRect(700, 600, 111, 31))
        self.btn_siguiente.setObjectName("btn_siguiente")
        self.btn_iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_iniciar.setGeometry(QtCore.QRect(250, 600, 111, 31))
        self.btn_iniciar.setObjectName("btn_iniciar")
        self.btn_parar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_parar.setGeometry(QtCore.QRect(470, 600, 111, 31))
        self.btn_parar.setObjectName("btn_parar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "K-Means"))
        self.btn_anterior.setText(_translate("MainWindow", "ANTERIOR"))
        self.btn_siguiente.setText(_translate("MainWindow", "SIGUIENTE"))
        self.btn_iniciar.setText(_translate("MainWindow", "INICIAR"))
        self.btn_parar.setText(_translate("MainWindow", "PARAR"))

        
    def incrementar_i(self):
        self.i += 1
    
    def decrementar_i(self):
        self.i -= 1

    def obtener_i(self):
        return self.i    

    def parar_estado(self):
        self.estado = 1

    def iniciar_estado(self):
        self.estado = 0    
    
    def obtener_estado(self):
        return self.estado