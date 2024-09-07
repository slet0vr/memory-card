from PyQt5.QtWidgets import QApplication, QWidget
app = QApplication([])
from layout_quizz import *



window = QWidget()
window.resize(600, 500)
window.setWindowTitle('Memory Card')
window.setLayout(main_line_quizz)
window.show()

app.exec()