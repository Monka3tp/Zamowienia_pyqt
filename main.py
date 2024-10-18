import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.sButton.toggled.connect(self.size)
        self.ui.mButton.toggled.connect(self.size)
        self.ui.lButton.toggled.connect(self.size)
        self.ui.xlButton.toggled.connect(self.size)
        self.ui.kartaButton.toggled.connect(self.size)
        self.ui.blikButton.toggled.connect(self.size)
        self.ui.odbiorButton.toggled.connect(self.size)
        self.show()

    def size(self):
        rozmiar = 'Wybierz'
        platnosc = 'Wybierz'
        if self.ui.sButton.isChecked():
            # rozmiar = 'S'
            rozmiar = self.ui.sButton.text()
        if self.ui.mButton.isChecked():
            rozmiar = self.ui.mButton.text()
        if self.ui.lButton.isChecked():
            rozmiar = self.ui.lButton.text()
        if self.ui.xlButton.isChecked():
            rozmiar = self.ui.xlButton.text()


        if self.ui.kartaButton.isChecked():
            platnosc = 'karta płatnicza'
        if self.ui.blikButton.isChecked():
            platnosc = 'blik'
        if self.ui.odbiorButton.isChecked():
            platnosc = 'płatność przy odbiorze'

        self.ui.outputLabel.setText(f'Wybrano rozmiar: {rozmiar}, Metoda płatności: {platnosc}')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())