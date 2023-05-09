from PyQt5.QtWidgets import QApplication
from Randevu import dataPage

app = QApplication([])
dataPencere = dataPage()
dataPencere.show()
app.processEvents()
app.exec_()
