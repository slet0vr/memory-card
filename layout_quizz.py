from PyQt5.QtWidgets import QPushButton, QRadioButton, QLabel, QVBoxLayout, QSpinBox, QGroupBox, QButtonGroup, QHBoxLayout
from PyQt5.QtCore import Qt
btn_menu = QPushButton("меню")
btn_rest = QPushButton("Відпочити")
spin = QSpinBox()
spin.setValue(30)




main_line_quizz = QVBoxLayout()
line1_quizz = QHBoxLayout()
line1_quizz.addWidget(btn_menu)
line1_quizz.addStretch(1)
line1_quizz.addWidget(btn_rest)
line1_quizz.addWidget(spin)
line1_quizz.addWidget(QLabel("хвилин"))

main_line_quizz.addLayout(line1_quizz)
