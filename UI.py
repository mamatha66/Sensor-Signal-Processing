import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMF055")
        # self.setGeometry(50,50,1000,1000)

        self.radioButton()
        self.ui()

    def ui(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox1, 1)
        vbox.addWidget(self.groupBox2, 2)
        vbox.addWidget(self.groupBox6, 3)
        vbox.addWidget(self.groupBox10, 4)
        self.setLayout(vbox)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.groupBox3, 1)
        hbox1.addWidget(self.groupBox4, 2)
        hbox1.addWidget(self.groupBox5, 3)
        self.groupBox2.setLayout(hbox1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.groupBox7, 1)
        hbox2.addWidget(self.groupBox8, 2)
        hbox2.addWidget(self.groupBox9, 3)
        self.groupBox6.setLayout(hbox2)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.groupBox11, 1)
        hbox3.addWidget(self.groupBox12, 2)
        hbox3.addWidget(self.groupBox13, 3)
        self.groupBox10.setLayout(hbox3)

        self.show()

    def radioButton(self):
        self.groupBox1 = QGroupBox("Select the Sensor type.")
        self.groupBox1.setFont(QtGui.QFont("Sanserif", 8))

        hbox = QHBoxLayout()

        self.rdbtn1 = QRadioButton("Accelerometer")
        hbox.addWidget(self.rdbtn1)

        self.rdbtn2 = QRadioButton("Gyroscope")
        hbox.addWidget(self.rdbtn2)

        self.rdbtn3 = QRadioButton("Magnetometer")
        hbox.addWidget(self.rdbtn3)

        self.groupBox1.setLayout(hbox)

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

        # ****************** Configuring Gyroscope ************************

        self.groupBox6 = QGroupBox("Configuring Gyroscope.")
        self.groupBox6.setFont(QtGui.QFont("Sanserif", 8))

        # *************** Gyroscope Range *************************

        self.groupBox7 = QGroupBox("Gyroscope Range.")
        self.groupBox7.setFont(QtGui.QFont("Sanserif", 8))

        vboxgr = QVBoxLayout()

        self.rdbtngr1 = QRadioButton("125 deg/sec")
        vboxgr.addWidget(self.rdbtngr1)

        self.rdbtngr2 = QRadioButton("250 deg/sec")
        vboxgr.addWidget(self.rdbtngr2)

        self.rdbtngr3 = QRadioButton("500 deg/sec")
        vboxgr.addWidget(self.rdbtngr3)

        self.rdbtngr4 = QRadioButton("1000 deg/sec")
        vboxgr.addWidget(self.rdbtngr4)

        self.rdbtngr5 = QRadioButton("2000 deg/sec")
        self.rdbtngr5.setChecked(True)
        vboxgr.addWidget(self.rdbtngr5)

        self.groupBox7.setLayout(vboxgr)

        # *************** Gyroscope Bandwidth *************************

        self.groupBox8 = QGroupBox("Gyroscope Bandwidth.")
        self.groupBox8.setFont(QtGui.QFont("Sanserif", 8))

        vboxgb = QVBoxLayout()

        self.rdbtngb1 = QRadioButton("12 Hz")
        vboxgb.addWidget(self.rdbtngb1)

        self.rdbtngb2 = QRadioButton("23 Hz")
        vboxgb.addWidget(self.rdbtngb2)

        self.rdbtngb3 = QRadioButton("32 Hz")
        vboxgb.addWidget(self.rdbtngb3)

        self.rdbtngb4 = QRadioButton("47 Hz")
        vboxgb.addWidget(self.rdbtngb4)

        self.rdbtngb5 = QRadioButton("64 Hz")
        vboxgb.addWidget(self.rdbtngb5)

        self.rdbtngb6 = QRadioButton("116 Hz")
        vboxgb.addWidget(self.rdbtngb6)

        self.rdbtngb7 = QRadioButton("230 Hz")
        vboxgb.addWidget(self.rdbtngb7)

        self.rdbtngb8 = QRadioButton("523 Hz")
        self.rdbtngb8.setChecked(True)
        vboxgb.addWidget(self.rdbtngb8)

        self.groupBox8.setLayout(vboxgb)

        # *************** Gyroscope Mode *************************

        self.groupBox9 = QGroupBox("Gyroscope Mode.")
        self.groupBox9.setFont(QtGui.QFont("Sanserif", 8))

        vboxgm = QVBoxLayout()

        self.rdbtngm1 = QRadioButton("Normal")
        self.rdbtngm1.setChecked(True)
        vboxgm.addWidget(self.rdbtngm1)

        self.rdbtngm2 = QRadioButton("Deep Suspend")
        vboxgm.addWidget(self.rdbtngm2)

        self.rdbtngm3 = QRadioButton("Suspend")
        vboxgm.addWidget(self.rdbtngm3)

        self.rdbtngm4 = QRadioButton("Fast Power up")
        vboxgm.addWidget(self.rdbtngm4)

        self.rdbtngm5 = QRadioButton("Advanced Power saving")
        vboxgm.addWidget(self.rdbtngm5)

        self.groupBox9.setLayout(vboxgm)

        # ****************** Configuring Magnetometer ************************

        self.groupBox10 = QGroupBox("Configuring Magnetometer.")
        self.groupBox10.setFont(QtGui.QFont("Sanserif", 8))

        # *************** Magnetometer Range *************************

        self.groupBox11 = QGroupBox("Magnetometer Range.")
        self.groupBox11.setFont(QtGui.QFont("Sanserif", 8))

        vboxmr = QVBoxLayout()

        self.rdbtnmr1 = QRadioButton("Low Power")
        vboxmr.addWidget(self.rdbtnmr1)

        self.rdbtnmr2 = QRadioButton("Regular")
        self.rdbtnmr2.setChecked(True)
        vboxmr.addWidget(self.rdbtnmr2)

        self.rdbtnmr3 = QRadioButton("High frequency")
        vboxmr.addWidget(self.rdbtnmr3)

        self.rdbtnmr4 = QRadioButton("Enhanced")
        vboxmr.addWidget(self.rdbtnmr4)

        self.groupBox11.setLayout(vboxmr)

        # *************** Magnetometer Bandwidth *************************

        self.groupBox12 = QGroupBox("Magnetometer Bandwidth.")
        self.groupBox12.setFont(QtGui.QFont("Sanserif", 8))

        vboxmb = QVBoxLayout()

        self.rdbtnmb1 = QRadioButton("2 Hz")
        vboxmb.addWidget(self.rdbtnmb1)

        self.rdbtnmb2 = QRadioButton("6 Hz")
        vboxmb.addWidget(self.rdbtnmb2)

        self.rdbtnmb3 = QRadioButton("8 Hz")
        vboxmb.addWidget(self.rdbtnmb3)

        self.rdbtnmb4 = QRadioButton("10 Hz")
        self.rdbtnmb4.setChecked(True)
        vboxmb.addWidget(self.rdbtnmb4)

        self.rdbtnmb5 = QRadioButton("15 Hz")
        vboxmb.addWidget(self.rdbtnmb5)

        self.rdbtnmb6 = QRadioButton("20 Hz")
        vboxmb.addWidget(self.rdbtnmb6)

        self.rdbtnmb7 = QRadioButton("25 Hz")
        vboxmb.addWidget(self.rdbtnmb7)

        self.rdbtnmb8 = QRadioButton("30 Hz")
        vboxmb.addWidget(self.rdbtnmb8)

        self.groupBox12.setLayout(vboxmb)

        # *************** Magnetometer Mode *************************

        self.groupBox13 = QGroupBox("Magnetometer Mode.")
        self.groupBox13.setFont(QtGui.QFont("Sanserif", 8))

        vboxmm = QVBoxLayout()

        self.rdbtnmm1 = QRadioButton("Normal")
        self.rdbtnmm1.setChecked(True)
        vboxmm.addWidget(self.rdbtnmm1)

        self.rdbtnmm2 = QRadioButton("Forced")
        vboxmm.addWidget(self.rdbtnmm2)

        self.rdbtnmm3 = QRadioButton("Suspend")
        vboxmm.addWidget(self.rdbtnmm3)

        self.rdbtnmm4 = QRadioButton("Sleep")
        vboxmm.addWidget(self.rdbtnmm4)

        self.groupBox13.setLayout(vboxmm)


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()