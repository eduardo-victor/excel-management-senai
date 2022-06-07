from base64 import encode
from encodings import utf_8
from tkinter import Menu
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import pandas as pd

class MenuDeletar(QMainWindow):
    def __init__(self):
        super(MenuDeletar, self).__init__()
        #CARREGAR TELA
        self.menu_deletar = uic.loadUi("telas/senai-xls-3.ui")
        
        #BOTÕES
        self.menu_deletar.load_excel.clicked.connect(self.load_plan)
        self.menu_deletar.botao_deletar.clicked.connect(self.delete_plan)
        self.menu_deletar.update_plan.clicked.connect(self.upd_plan)


        #MOSTRAR TELA
        self.menu_deletar.show()
    


    def load_plan(self):
        self.file_path = 'excel/editalcovid.xlsx'
        self.menu_deletar.load_path.setText(str(self.file_path))
        
        self.planilha = pd.read_excel(self.file_path)

        self.line_list = []

        for line in range(0, self.planilha.shape[0]):
            self.line_list.append(line)

        #SUBSTITUI
        for j in self.line_list:
            self.menu_deletar.cb_line.addItem(str(j))

    def delete_plan(self):
        self.row = self.menu_deletar.cb_line.currentText()
        self.planilha = self.planilha.drop(int(self.row), axis=0)
        self.menu_deletar.lbl_msg.setText("Linha deletada com sucesso, atualize a planilha!")
    
    def upd_plan(self):    
        self.planilha.to_excel('editalcovid2.xlsx')
        self.menu_deletar.lbl_msg.setText("")

    
