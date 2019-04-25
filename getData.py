#!/usr/bin/env python
# -*- coding: utf-8 -*-


class getData:
    def __init__(self, sensor, ser):
        self.sensor = sensor
        self.ser = ser

    def getSamples(self, number):
        if number:
            data_b = self.getNRecords(number)

        else:
            data_b = self.getRecords()

        # for item in data_b:
        #     print(item)
        data_i = self.decodeData(data_b)
        return data_i

    def getNRecords(self, number):
        data_b = []

        if self.sensor == 'Acc':
            for i in range(3 * number):
                line = self.ser.readline().decode()
                if '0x01' in line:
                    data_b.append(line.split()[1:])

        elif self.sensor == 'Gyr':
            for i in range(3 * number):
                line = self.ser.readline().decode()
                if '0x02' in line:
                    data_b.append(line.split()[1:])

        elif self.sensor == 'Mag':
            for i in range(3 * number):
                line = self.ser.readline().decode()
                if '0x03' in line:
                    data_b.append(line.split()[1:])

        else:
            for i in range(3 * number):
                line = self.ser.readline().decode()
                if line:
                    data_b.append(line.split())

        for row in data_b:
            print(row)
        return data_b

    def getRecords(self):
        data_b = []
        print("Collecting samples for you. Stop me when you are sufficient.")
        if self.sensor == 'Acc':
            try:
                while True:
                    line = self.ser.readline().decode()
                    if '0x01' in line:
                        data_b.append(line.split()[1:])

            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                return data_b

        elif self.sensor == 'Gyr':
            try:
                while True:
                    line = self.ser.readline().decode()
                    if '0x02' in line:
                        data_b.append(line.split()[1:])

            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                return data_b

        elif self.sensor == 'Mag':
            try:
                while True:
                    line = self.ser.readline().decode()
                    if '0x03' in line:
                        data_b.append(line.split()[1:])

            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                return data_b

        else:
            try:
                while True:
                    line = self.ser.readline().decode()
                    if line:
                        data_b.append(line.split())

            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                for record in data_b:
                    print(record)
                return data_b

    def decodeData(self,data_b):
        data_i = []

        for record in data_b:
            data_r = []
            for sample in record:
                # convert to unsigned
                x = int(sample, 16)  # example (-65)
                # check sign bit
                if (x & 0xD000) == 0xD000:
                    x = -((x ^ 0xffff) + 1)  # if set, invert and add one to get the negative value,
                data_r.append(x)  # then add the negative sign
            data_i.append(data_r)

        return data_i