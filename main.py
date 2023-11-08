import random
import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.rezerwuj_button.clicked.connect(self.rezerwuj)
        self.show()

    def rezerwuj(self):
        cena = 0
        termin_wizyty = 0
        specjalizacja = ""
        if self.ui.wizyta_prywatna.isChecked():
            cena = 200
            termin_wizyty = random.randint(1, 14)
        else:
            termin_wizyty = random.randint(0, 1000)
        if self.ui.internista.isChecked():
            specjalizacja = "internista"
        elif self.ui.dermatolog.isChecked():
            specjalizacja = "dermatolog"
        else:
            specjalizacja = "pediatra"
        self.ui.result.setText(
            f"Pomyślnie zarezerwowano wizytę u lekarza: {specjalizacja}. Termin wizyty przypada za: {termin_wizyty}. Koszt wizyty: {cena}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())
