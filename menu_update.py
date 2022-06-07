import csv
from tkinter import filedialog
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

class MenuUpdate(QMainWindow):
    def __init__(self):
        super(MenuUpdate, self).__init__()

        #LOAD DISPLAY
        self.menu_update = uic.loadUi("telas\\senai-xls-5.ui")


        #MOSTRAR TELA
        self.menu_update.show()
    
    #BOTÕESSS
        self.menu_update.load_excel.clicked.connect(self.load_plan)
        self.menu_update.insert_button.clicked.connect(self.write_file)
        self.menu_update.update_plan.clicked.connect(self.upd_plan)
        
    
    def load_plan(self):
        self.file_path = 'excel/editalcovid.xlsx'
        self.menu_update.load_path.setText(str(self.file_path))
        
        self.planilha = pd.read_excel(self.file_path)
        
        self.name_list = []
        self.line_list = []

        for row in self.planilha:
            self.name_list.append(row)
        
        for line in range(0, self.planilha.shape[0]):
            print(line)
            self.line_list.append(line)
            print(self.line_list)

        for i in self.name_list:
            self.menu_update.cb_column.addItem(i)
        
        #SUBSTITUI
        for j in self.line_list:
            self.menu_update.cb_line.addItem(str(j))
        
    def write_file(self):
        self.coluna = self.menu_insert.cb_column.currentText()
        self.line = self.menu_insert.cb_line.currentText()
        self.planilha.loc[int(self.line), self.coluna] =  self.menu_insert.data_insert.text()
        self.menu_update.data_insert.setText("Inserido com sucesso, atualize a planilha.")
        
    def upd_plan(self):    
        self.planilha.to_excel('editalcovid2.xlsx')
        self.menu_update.data_insert.setText("")
        