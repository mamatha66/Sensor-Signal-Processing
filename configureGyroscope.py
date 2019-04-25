#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import serial


def configure_gyro(rate, ser):
    sample_rate = None

    # Stop the Data Stream
    command = 0x00
    send_command(command, ser)

    # Select Gyroscope
    command = 0xBB
    print('Gyroscope selected')
    send_command(command, ser)

    # Configure range
    command = 0x00                 # default value 2000°/s
    print('Default value: 2000°/s')
    send_command(command, ser)

    # Select Bandwidth
    if rate:
        if rate <= 12:
            command = 0x05
            print('Bandwidth: 12Hz')
            send_command(command, ser)
            sample_rate = 12

        elif rate <= 23:
            command = 0x04
            print('Bandwidth: 23Hz')
            send_command(command, ser)
            sample_rate = 23

        elif rate <= 32:
            command = 0x07
            print('Bandwidth: 32Hz')
            send_command(command, ser)
            sample_rate = 32

        elif rate <= 47:
            command = 0x03
            print('Bandwidth: 47Hz')
            send_command(command, ser)
            sample_rate = 47

        elif rate <= 64:
            command = 0x06
            print('Bandwidth: 64Hz')
            send_command(command, ser)
            sample_rate = 64

        elif rate <= 116:
            command = 0x02
            print('Bandwidth: 116Hz')
            send_command(command, ser)
            sample_rate = 116

        elif rate <= 230:
            command = 0x01
            print('Bandwidth: 230Hz')
            send_command(command, ser)
            sample_rate = 230

        else:
            command = 0x00
            print('Bandwidth: 523Hz')
            send_command(command, ser)
            sample_rate = 523

    else:                               # Default - 523Hz
        command = 0x00
        print('Bandwidth: 523Hz')
        send_command(command, ser)
        sample_rate = 523

    # Select Mode
    command = 0x00                    # PM Normal Mode(Default)
    print('Mode: Normal Mode (Default)')
    send_command(command, ser)

    # Start the Data Stream again
    command = 0x01
    send_command(command, ser)

    return sample_rate


def send_command(command, ser):
    time.sleep(0.1)
    ser.flushInput()
    ser.write(serial.to_bytes([command, 0x0D, 0x0A]))
    time.sleep(0.01)
    response = ser.read(ser.inWaiting()).decode()
    print(response)