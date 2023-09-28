import random
import os
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('design.ui')
        self.dark_mode = True

        self.game = [[None for i in range(9)] for j in range(9)]
        self.backup_game = [[None] * 9 for _ in range(9)]
        self.backup_style = [[None] * 9 for _ in range(9)]


        for i in range(9):
            for j in range(9):
                tb = QLineEdit()
                tb.setSizePolicy(QSizePolicy.Preferred , QSizePolicy.Preferred)
                tb.setStyleSheet('font-size: 20px')
                self.game[i][j] = tb #backend
                self.ui.my_grid.addWidget(tb , i , j) #frontend
                tb.textChanged.connect(self.checkGame)
            


        self.ui.show()
        self.ui.b_NG.clicked.connect(self.newGame)
        self.ui.b_check.clicked.connect(self.checkGame)
        self.ui.b_reset.clicked.connect(self.resetGame)
        self.ui.b_mode.clicked.connect(self.modeGame)


    def modeGame(self):
        if self.dark_mode :
            self.ui.setStyleSheet('background: white; color: black')
            self.dark_mode = False
        else:
            self.ui.setStyleSheet('background: black; color: white')
            self.dark_mode = True


    def resetGame(self):
        for row in range(9):
            for col in range(9):
                text = self.backup_game[row][col].text()
                style = self.backup_style[row][col]
                self.game[row][col].setText(text)
                self.game[row][col].setStyleSheet(style)

 
    def checkGame(self):
        for row in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() != '':
                        self.game[row][i].setStyleSheet('font-size: 20px ; background-color:pink ; color: black')

        for col in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != '':
                        self.game[i][col].setStyleSheet('font-size: 20px ; background-color:pink ; color: black')

        for i in range(3):
            for j in range(3):
                box = set()
                for k in range(3):
                    for l in range(3):
                        text = self.game[3*i + k][3*j + l].text()
                        if text != '':
                            if text in box:
                                self.game[3*i + k][3*j + l].setStyleSheet('font-size: 20px ; background-color:pink; color: black')
                            else:
                                box.add(text)


            sender = self.sender() 
            for row in range(9):
                for col in range(9):
                    if self.game[row][col] == sender:
                        if not self.isValidEntry(row, col):
                            sender.setStyleSheet('font-size: 20px ; background-color:pink ; color: black')
           
                         
        is_filled = True
        is_correct = True
        for i in range(9):
            for j in range(9):
                if self.game[i][j].text() == '':
                    is_filled = False
                    break
                elif not self.isValidEntry(i, j):
                    is_correct = False
                    break
        
        if is_filled and is_correct:
            QMessageBox.information(self, "The end", "you win :) ")


    
    def isValidEntry(self, row, col):
        value = self.game[row][col].text()
        
        # بررسی صحت در سطر
        for j in range(9):
            if j != col and self.game[row][j].text() == value:
                return False
        
        # بررسی صحت در ستون
        for i in range(9):
            if i != row and self.game[i][col].text() == value:
                return False
        
        # بررسی صحت در مربع 3x3
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if (i != row or j != col) and self.game[i][j].text() == value:
                    return False
        
        return True



    def newGame(self):

        for i in range(9):
            for j in range(9):
                self.game[i][j].setText('')
                self.game[i][j].setAlignment(Qt.AlignCenter)
            
                
        r = random.randint(1,6)
        file_path = f'data/s{r}.txt'
 
        if not os.path.exists(file_path):
            QMessageBox.critical(self, "Error", f"File '{file_path}' does not exist!")
            return
        
        try:
            f = open(file_path, 'r') # az noe khandani
            big_text = f.read() # yek str tak khati
            rows = big_text.split('\n') # satr ha
        finally:
            f.close()
        
        
        
        for i in range(9):
            numbers = rows[i].split(' ') #adad
            for j in range(9):
                if numbers[j] != "0":
                    self.game[i][j].setStyleSheet('font-size: 20px ; background-color: rgb(172, 172, 172); color: black')
                    self.game[i][j].setText(numbers[j]) #jaigozari
                else:
                    self.game[i][j].setStyleSheet('font-size: 20px ; color: rgb(172, 172, 172); background-color:black ')
                
                self.backup_game[i][j] = QLineEdit(self.game[i][j].text())
                self.backup_style[i][j] = self.game[i][j].styleSheet()


app = QApplication([])
window = MainWindow()
app.exec()