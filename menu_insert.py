import csv
from tkinter import filedialog
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

class MenuInsert(QMainWindow):
    def __init__(self):
        super(MenuInsert, self).__init__()

        # CARREGAR TELA
        self.menu_insert = uic.loadUi("telas/senai-xls-2.ui")

        #MOSTRAR TELA
        self.menu_insert.show()

        #BOTÕESSS
        self.menu_insert.load_excel.clicked.connect(self.load_plan)
        self.menu_insert.insert_button.clicked.connect(self.write_file)
        self.menu_insert.update_plan.clicked.connect(self.upd_plan)
        
    
    def load_plan(self):
        self.file_path = 'excel/editalcovid.xlsx'
        self.menu_insert.load_path.setText(str(self.file_path))
        
        self.planilha = pd.read_excel(self.file_path)
        
        self.name_list = []
        self.line_list = []

        for row in self.planilha:
            self.name_list.append(row)
        
        for line in range(0, self.planilha.shape[0]):
            self.line_list.append(line)

        for i in self.name_list:
            self.menu_insert.cb_column.addItem(i)

    def write_file(self):
        self.coluna = self.menu_insert.cb_column.currentText()
        self.planilha.loc[self.planilha.shape[0], self.coluna] =  self.menu_insert.data_insert.text()
        self.menu_insert.data_insert.setText("Inserido com sucesso, atualize a planilha.")
    
    def upd_plan(self):    
        self.planilha.to_excel('editalcovid2.xlsx')
        self.menu_insert.data_insert.setText("")


