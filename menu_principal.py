from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys

from menu_delete import MenuDeletar
from menu_insert import MenuInsert
from menu_search import MenuProcurar

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        #CARREGAR TELA
        self.menu = uic.loadUi("telas/senai-xls.ui")

        #MOSTRAR TELA
        self.menu.show()

        #BOTÕES
        self.menu.botao_delete.clicked.connect(self.tela_deletar)
        self.menu.botao_insert.clicked.connect(self.tela_inserir)
        self.menu.botao_search.clicked.connect(self.tela_buscar)

    def tela_deletar(self):
        self.menu.close()
        self.deletar = MenuDeletar()
    
    def tela_inserir(self):
        self.menu.close()
        self.inserir = MenuInsert()
    
    def tela_buscar(self):
        self.menu.close()
        self.buscar = MenuProcurar()

if __name__ == '__main__':
    # Initialize The App
    app = QApplication(sys.argv)
    UIWindow = Menu()
    app.exec_()