from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys

class MenuInsert(QMainWindow):
    def __init__(self):
        super(MenuInsert, self).__init__()
        # CARREGAR TELA
        self.menu_insert = uic.loadUi("telas/senai-xls-2.ui")

        #MOSTRAR TELA
        self.menu_insert.show()