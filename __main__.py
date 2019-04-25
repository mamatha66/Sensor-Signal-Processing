#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
from . import serial_port as s
from . import configureSensor
from . import getData
from . import generateFile


def main():

    global ser
    ser = s.serial_port()

    if ser.isOpen():
        try:
            sample_rate = configureSensor.configure(args.sensor, rate, ser)

            data = getData.getData(sensor, ser)
            data_i = data.getSamples(number)

            if args.file_path:
                generateFile.csvFile(args.file_path, sensor, sample_rate, data_i)

            else:
                print("Here're the requested samples:")
                for record in data_i:
                    print(record)
                print("{} samples printed.".format(len(data_i)))

        except():
            print("error")
    else:
        print("Cannot open serial port")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_path", help="Path to the output file")
    parser.add_argument("--sensor", help="Select the Sensor", choices=["Acc", "Gyr", "Mag"])
    parser.add_argument("--rate", help="Rate")
    parser.add_argument("--number", help="number of samples")
    args = parser.parse_args()

    if args.number:
        number = int(args.number)
    else:
        number = None

    if args.rate:
        rate = int(args.rate)
    else:
        rate = None

    if args.sensor:
        sensor = args.sensor
    else:
        sensor = None

    sys.exit(main())



