from csv import reader
from tkinter import filedialog
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

class MenuInsert(QMainWindow):
    def __init__(self):
        super(MenuInsert, self).__init__()

        #VARIAVEIS
        # self.rating_list = []
        # self.yq_list = []
        # CARREGAR TELA
        self.menu_insert = uic.loadUi("telas/senai-xls-2.ui")

        #MOSTRAR TELA
        self.menu_insert.show()

        #BOTÕESSS
        self.menu_insert.load_excel.clicked.connect(self.load_plan)
        
    
    def load_plan(self):
        self.file_path = QFileDialog.getOpenFileName(self, 'CSV File', '')
        self.menu_insert.load_path.setText(str(self.file_path))
        

        #NÃO FUNCIONOU ESSA PARTE AQUI
        with open(self.file_path, 'r') as file:
            for line_number, content in enumerate(file):
                print(line_number, content)