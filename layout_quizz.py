from PyQt5.QtWidgets import QPushButton, QRadioButton, QLabel, QVBoxLayout, QSpinBox, QGroupBox, QButtonGroup, QHBoxLayout
from PyQt5.QtCore import Qt
btn_menu = QPushButton("меню")
btn_rest = QPushButton("Відпочити")
spin = QSpinBox()
spin.setValue(30)

def create_card_layout():
    
    layout = QVBoxLayout()

    
    question_label = QLabel("Яблуко")
    layout.addWidget(question_label)

    
    radio_group_box = QGroupBox("Варіанти відповіді:")

    
    line1_quizz = QRadioButton("caterpillar")
    line2_quizz = QRadioButton("apple")
    line3_quizz = QRadioButton("aplication")
    line4_quizz = QRadioButton("building")

    
    radio_button_group = QButtonGroup()
    radio_button_group.addButton(line1_quizz)
    radio_button_group.addButton(line2_quizz)
    radio_button_group.addButton(line3_quizz)
    radio_button_group.addButton(line4_quizz)


main_line_quizz = QVBoxLayout()
line1_quizz = QHBoxLayout()
line1_quizz.addWidget(btn_menu)
line1_quizz.addStretch(1)
line1_quizz.addWidget(btn_rest)
line1_quizz.addWidget(spin)
line1_quizz.addWidget(QLabel("хвилин"))

main_line_quizz.addLayout(line1_quizz)
