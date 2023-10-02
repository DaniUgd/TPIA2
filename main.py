
from PyQt5.QtWidgets import QApplication
from init import vistaPrincipal
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = vistaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
