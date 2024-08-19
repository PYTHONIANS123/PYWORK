from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QPushButton, QVBoxLayout, QGridLayout,QLineEdit,
                               QLabel, QMessageBox)
from PyQt5.QtGui import QFont, QPalette, QColor

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Currency Converter 2024")
        # setting the maximum height and width
        self.setMaximumSize(400, 300)
        self.MainUI()
        
    def ReloadCurrency(self):
        with open("currency_base.txt", "r") as currency_:
            currency_base=[lines.strip("\n") for lines in currency_]
            return currency_base
        
        
    def MainUI(self):
        # Main layout
        self.layout=QVBoxLayout()
        self.setLayout(self.layout)
        
        # Currency selection for base currency
        self.currency_selector=QComboBox()
        self.currency_selector.addItems(self.ReloadCurrency())
        self.currency_selector.currentIndexChanged.connect(self.change_base_currency)
        # adding the currency_selector to layout
        self.layout.addWidget(self.currency_selector)
        
        # Grid layout for input and output
        self.grid_layout=QGridLayout()
        self.base_label_amount=QLabel("Amount")
        self.base_input=QLineEdit()
        self.grid_layout.addWidget(self.base_label_amount, 0, 0)
        self.grid_layout.addWidget(self.base_input, 0, 1)
        
        # Currency Selection for target 1 currencies
        self.target_selector_1=QComboBox()
        self.target_selector_1.addItems(self.ReloadCurrency())
        self.target_selector_1.currentIndexChanged.connect(self.convert_currency)
        self.target_value_1=QLabel("0")
        self.grid_layout.addWidget(self.target_selector_1, 1, 0) 
        self.grid_layout.addWidget(self.target_value_1, 1, 1)
        # Currency Selection for target 2 currencies
        self.target_selector_2=QComboBox()
        self.target_selector_2.addItems(self.ReloadCurrency())
        self.target_selector_2.currentIndexChanged.connect(self.convert_currency)
        self.target_value_2=QLabel("0")
        self.grid_layout.addWidget(self.target_selector_2, 2, 0)
        self.grid_layout.addWidget(self.target_value_2, 2, 1)
        
        # Adding the gridlayout to the main layout
        self.layout.addLayout(self.grid_layout)
        
        
    def change_base_currency(self):
        pass       
    
    def convert_currency(self):
        pass
        
        
#
if __name__=="__main__":
    app=QApplication([])
    window=CurrencyConverter()
    window.show()
    app.exec()