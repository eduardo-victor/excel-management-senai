from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys

from menu_delete import MenuDeletar
from menu_insert import MenuInsert
from menu_search import MenuProcurar
from menu_update import MenuUpdate

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
        self.menu.botao_update.clicked.connect(self.tela_atualizar)

    def tela_deletar(self):
        self.deletar = MenuDeletar()
    
    def tela_inserir(self):
        self.inserir = MenuInsert()
    
    def tela_buscar(self):
        self.buscar = MenuProcurar()
    
    def tela_atualizar(self):
        self.atualizar = MenuUpdate()

if __name__ == '__main__':
    # Initialize The App
    app = QApplication(sys.argv)
    UIWindow = Menu()
    app.exec_()