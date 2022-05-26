from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys

class MenuProcurar(QMainWindow):
    def __init__(self):
        super(MenuProcurar, self).__init__()
        #CARREGAR TELA
        self.buscar = uic.loadUi("telas/senai-xls-4.ui")

        #MOSTRAR TELA
        self.buscar.show()