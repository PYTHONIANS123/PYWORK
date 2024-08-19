from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QPushButton, QVBoxLayout, QGridLayout,QLineEdit,
                               QLabel, QMessageBox)
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon
import ast
import requests

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ONLINE CURRENCY CONVERTER")
        # setting the maximum height and width
        self.setMaximumSize(500, 200)
        self.setGeometry(200, 150, 400, 200)
        self.setWindowIcon(QIcon("currencyIcon.png"))
        self.MainUI()
        
    def ReloadCurrency(self):
        with open("currency_codes.txt", "r") as currency_:
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
        self.base_input.textChanged.connect(self.convert_currency)
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
        
        # Update rates button
        self.update_button=QPushButton("Update Rates")
        self.update_button.clicked.connect(self.update_rates)
        self.layout.addWidget(self.update_button)
                
        # Styling
        # --Colors--- use
        # 1. #f0f0f0 ---> ligth gray color(composed of: Red 240, Green: 240, Blue: 240)
        # 2. #007BFF --> 
        
        self.setStyleSheet("""
                           QWidget{
                               background-color:#f0f0f0;
                           }
                           QLabel{
                               font-size:16px;
                               font-weight:bold;
                           }
                           QPushButton{
                               background-color:#007BFF;
                               color:white;
                               font-size:16px;
                               pading:10px;
                               border-radius:5px;
                           }
                           QComboBox{
                               font-size:16px;
                               padding:5px;
                           }
                           """)
        
        self.base_currency="USD"
        
        
    def fetch_latest_rates(self):
        try:
            response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{self.base_currency}")
            data = response.json()
            return data["rates"]
        except Exception as e:
            print(f"Error fetching rates: {e}")
            return None
        
    def update_rates(self):
        rates=self.fetch_latest_rates()
        if rates:
            with open(str(self.currency_selector.currentText()+".txt"), "w") as BaseCurrency:
                BaseCurrency.write(str(rates))
                QMessageBox.information(self, "Update Rates", "Rates Update Successfully")
                # self.base_input.setText("0")
                # self.target_value_1.setText("0")
                # self.target_value_2.setText("0")
        else:
            QMessageBox.warning(self, "Update Rates", "Failed to update Rates! \nResults maybe inaccurate")
        
    def change_base_currency(self):
        self.base_currency=self.currency_selector.currentText()
        self.update_rates()
        self.convert_currency()
             

    def convert_currency(self):
        try:
            self.base_currency=self.currency_selector.currentText()
            # Remove this block from MainUI()
            with open(str(self.base_currency+".txt"), "r") as USD:
                exchange_rates=USD.read()
            self.exchange_rates=ast.literal_eval(exchange_rates)

            try:
                base_amount=float(self.base_input.text())
                target_currency_1=self.target_selector_1.currentText()
                target_currency_2=self.target_selector_2.currentText()
                self.target_value_1.setText(f"{base_amount*self.exchange_rates[target_currency_1]:.2f}")
                self.target_value_2.setText(f"{base_amount*self.exchange_rates[target_currency_2]:.2f}")
                
            except ValueError:
                self.target_value_1.setText("0")
                self.target_value_2.setText("0")

        except FileNotFoundError:
            pass
#
if __name__=="__main__":
    app=QApplication([])
    window=CurrencyConverter()
    window.show()
    app.exec()