import enum
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
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

        for line in range(0, self.planilha.shape[0]):
            self.line_list.append(line)
        
        for j in self.line_list:
            self.menu_buscar.cb_rows.addItem(str(j))
        
    def imprimir(self):
        self.combo = self.menu_buscar.cb_rows.currentText()
        self.menu_buscar.tabela.setColumnCount(self.planilha.shape[1])
        self.menu_buscar.tabela.setRowCount(1)
        
        for row in self.planilha.iterrows():
            values = row[1]
            for col_index , value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.0f}'.format(value)
                tableItem = self.menu_buscar.tabela(str(value))
                self.menu_buscar.tabela.setItem(row[0], col_index, tableItem)