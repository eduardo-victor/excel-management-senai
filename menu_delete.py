from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys

class MenuDeletar(QMainWindow):
    def __init__(self):
        super(MenuDeletar, self).__init__()
        #CARREGAR TELA
        self.deletar = uic.loadUi("telas/senai-xls-3.ui")

        #MOSTRAR TELA
        self.deletar.show()