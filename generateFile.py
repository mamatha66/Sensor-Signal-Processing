#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import csv


class fileDetails:
    def __init__(self, sample_rate, number, sensor):
        self.sample_rate = sample_rate
        self.number = number
        self.sensor = sensor

    def getFileName(self):
        if self.sensor == 'Acc':
            filename = "Accelerometer_data@" + time.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"

        elif self.sensor == 'Gyr':
            filename = "Gyroscope_data@" + time.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"

        elif self.sensor == 'Mag':
            filename = "Magnetometer_data@" + time.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"

        else:
            filename = "Sensor_data@" + time.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"

        return filename

    def getFileInfo(self):
        if self.sensor == 'Acc':
            file_info = ('#' + 'ACCELERATION' + "\n" + '#' + 'SAMPLE_RATE = ' + str(self.sample_rate) + ' Hz' + "\n"
                         + '#' + 'Recorded at: ' + time.strftime("%Y-%m-%d-%H:%M:%S") +
                         "\n" + '#' + 'Number of samples = ' + str(self.number) + "\n" + "\n")

        elif self.sensor == 'Gyr':
            file_info = ('#' + 'ANGULAR VELOCITY' + "\n" + '#' + 'SAMPLE_RATE = ' + str(self.sample_rate) + ' Hz' + "\n"
                         + '#' + 'Recorded at: ' + time.strftime("%Y-%m-%d-%H:%M:%S") +
                         "\n" + '#' + 'Number of samples = ' + str(self.number) + "\n" + "\n")

        elif self.sensor == 'Mag':
            file_info = ('#' + 'MAGNETIC FIELD' + "\n" + '#' + 'SAMPLE_RATE = ' + str(self.sample_rate) + ' Hz' + "\n"
                         + '#' + 'Recorded at: ' + time.strftime("%Y-%m-%d-%H:%M:%S") +
                         "\n" + '#' + 'Number of samples = ' + str(self.number) + "\n" + "\n")

        else:
            file_info = ('#' + 'Samples from Accelerometer, Gyroscope and Magnetometer' + "\n"
                         + '#' + 'Recorded at: ' + time.strftime("%Y-%m-%d-%H:%M:%S") +
                         "\n" + '#' + 'Number of samples = ' + str(self.number) + "\n" + "\n")

        return file_info


def csvFile(file_path, sensor, sample_rate, data_i):
    number = len(data_i)
    if os.path.exists(file_path):
        print("Generating csv file.")
        file = fileDetails(sample_rate, number, sensor)
        filename = file.getFileName()
        f = open(os.path.join(file_path, filename), 'w+')
        file_info = file.getFileInfo()
        f.write(file_info)
        wr_acc = csv.writer(f, dialect='excel')

        for record in data_i:
            wr_acc.writerow(record)
        f.close()
        print("File generated with {} samples.".format(number))
        print("Check your destination folder. Thank you.")