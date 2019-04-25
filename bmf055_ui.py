import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from . import acc_ui

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMF055")
        # self.setGeometry(50,50,1000,1000)

        self.radioButton()
        self.ui()

    def ui(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox1)
        # vbox.addWidget(self.groupBox2)
        self.setLayout(vbox)
        self.show()

    def radioButton(self):
        self.groupBox1 = QGroupBox("Select the Sensor type.")
        self.groupBox1.setFont(QtGui.QFont("Sanserif", 8))

        hbox = QHBoxLayout()

        self.rdbtn1 = QRadioButton("Accelerometer")
        hbox.addWidget(self.rdbtn1)
        self.rdbtn1.clicked.connect(self.call_accelerometer)

        self.rdbtn2 = QRadioButton("Gyroscope")
        hbox.addWidget(self.rdbtn2)

        self.rdbtn3 = QRadioButton("Magnetometer")
        hbox.addWidget(self.rdbtn3)

        self.groupBox1.setLayout(hbox)

    def call_accelerometer(self):
        acc = acc_ui.Accelerometer()
        acc.__init__()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()