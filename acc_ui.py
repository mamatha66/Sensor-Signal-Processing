from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class Accelerometer(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Accelerometer Configuration")

        self.config_accelerometer()
        self.ui()

    def ui(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox2)
        self.setLayout(vbox)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.groupBox3, 1)
        hbox1.addWidget(self.groupBox4, 2)
        hbox1.addWidget(self.groupBox5, 3)
        self.groupBox2.setLayout(hbox1)

        self.show()

    def config_accelerometer(self):
        # ****************** Configuring Accelerometer ************************

        self.groupBox2 = QGroupBox("Configuring Accelerometer.")
        self.groupBox2.setFont(QtGui.QFont("Sanserif", 8))

        # *************** Accelerometer Range *************************

        self.groupBox3 = QGroupBox("Accelerometer Range.")
        self.groupBox3.setFont(QtGui.QFont("Sanserif", 8))

        vboxar = QVBoxLayout()

        self.rdbtnar1 = QRadioButton("2g")
        self.rdbtnar1.setChecked(True)
        vboxar.addWidget(self.rdbtnar1)

        self.rdbtnar2 = QRadioButton("4g")
        vboxar.addWidget(self.rdbtnar2)

        self.rdbtnar3 = QRadioButton("8g")
        vboxar.addWidget(self.rdbtnar3)

        self.rdbtnar4 = QRadioButton("16g")
        vboxar.addWidget(self.rdbtnar4)

        self.groupBox3.setLayout(vboxar)

        # *************** Accelerometer Bandwidth *************************

        self.groupBox4 = QGroupBox("Accelerometer Bandwidth.")
        self.groupBox4.setFont(QtGui.QFont("Sanserif", 8))

        vboxab = QVBoxLayout()

        self.rdbtnab1 = QRadioButton("8 Hz")
        vboxab.addWidget(self.rdbtnab1)

        self.rdbtnab2 = QRadioButton("16 Hz")
        vboxab.addWidget(self.rdbtnab2)

        self.rdbtnab3 = QRadioButton("31 Hz")
        vboxab.addWidget(self.rdbtnab3)

        self.rdbtnab4 = QRadioButton("63 Hz")
        vboxab.addWidget(self.rdbtnab4)

        self.rdbtnab5 = QRadioButton("125 Hz")
        vboxab.addWidget(self.rdbtnab5)

        self.rdbtnab6 = QRadioButton("250 Hz")
        vboxab.addWidget(self.rdbtnab6)

        self.rdbtnab7 = QRadioButton("500 Hz")
        vboxab.addWidget(self.rdbtnab7)

        self.rdbtnab8 = QRadioButton("1000 Hz")
        self.rdbtnab8.setChecked(True)
        vboxab.addWidget(self.rdbtnab8)

        self.groupBox4.setLayout(vboxab)

        # *************** Accelerometer Mode *************************

        self.groupBox5 = QGroupBox("Accelerometer Mode.")
        self.groupBox5.setFont(QtGui.QFont("Sanserif", 8))

        vboxam = QVBoxLayout()

        self.rdbtnam1 = QRadioButton("PM Normal")
        self.rdbtnam1.setChecked(True)
        vboxam.addWidget(self.rdbtnam1)

        self.rdbtnam2 = QRadioButton("Low Power 1")
        vboxam.addWidget(self.rdbtnam2)

        self.rdbtnam3 = QRadioButton("Suspend")
        vboxam.addWidget(self.rdbtnam3)

        self.rdbtnam4 = QRadioButton("Deep Suspend")
        vboxam.addWidget(self.rdbtnam4)

        self.rdbtnam5 = QRadioButton("Low Power 2")
        vboxam.addWidget(self.rdbtnam5)

        self.rdbtnam6 = QRadioButton("Standby")
        vboxam.addWidget(self.rdbtnam6)

        self.groupBox5.setLayout(vboxam)