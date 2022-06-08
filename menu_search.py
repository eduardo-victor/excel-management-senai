from ast import Str
import enum
from math import comb
from msilib.schema import ComboBox
import re
from traceback import print_tb
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QTableWidgetItem
from PyQt5 import uic
import sys
import pandas as pd

class MenuProcurar(QMainWindow):
    def __init__(self):
        super(MenuProcurar, self).__init__()
        #CARREGAR TELA
        self.menu_buscar = uic.loadUi("telas/senai-xls-4.ui")

        #BOTOES
        self.menu_buscar.load_excel.clicked.connect(self.load_plan)
        self.menu_buscar.botao_buscar.clicked.connect(self.imprimir)

        #MOSTRAR TELA
        self.menu_buscar.show()
    

    def load_plan(self):
        self.file_path = 'excel/editalcovid.xlsx'
        self.menu_buscar.load_path.setText(str(self.file_path))
        self.planilha = pd.read_excel(self.file_path)

        self.line_list = []
        self.name_list = []

        for row in self.planilha:
            self.name_list.append(row)

        for line in range(0, self.planilha.shape[0]):
            self.line_list.append(line)
        
        for i in self.name_list:
            self.menu_buscar.cb_colunas.addItem(i)

        for j in self.line_list:
            self.menu_buscar.cb_rows.addItem(str(j))
        
    def imprimir(self):
        coluna = self.menu_buscar.cb_colunas.currentText()
        linha = self.menu_buscar.cb_rows.currentText()
        
        result = self.planilha.loc[int(linha), coluna]
        self.menu_buscar.lbl_retorno.setText(f"COLUNA: {coluna} | LINHA: {linha} | CONTEÚDO: {result}")