#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import serial


def configure_mag(rate, ser):
    sample_rate = None

    # Stop the Data Stream
    command = 0x00
    send_command(command, ser)

    # Select Magnetometer
    command = 0xCC
    print('Magnetometer selected')
    send_command(command, ser)

    # Configure preset
    command = 0x02                 # default - regular
    print('Preset Regular selected')
    send_command(command, ser)

    # Select Bandwidth
    if rate:
        if rate <= 2:
            command = 0x01
            print('Bandwidth: 2Hz')
            send_command(command, ser)
            sample_rate = 2

        elif rate <= 6:
            command = 0x02
            print('Bandwidth: 6Hz')
            send_command(command, ser)
            sample_rate = 6

        elif rate <= 8:
            command = 0x03
            print('Bandwidth: 8Hz')
            send_command(command, ser)
            sample_rate = 8

        elif rate <= 10:
            command = 0x00
            print('Bandwidth: 10Hz')
            send_command(command, ser)
            sample_rate = 10

        elif rate <= 15:
            command = 0x04
            print('Bandwidth: 15Hz')
            send_command(command, ser)
            sample_rate = 15

        elif rate <= 20:
            command = 0x05
            print('Bandwidth: 20Hz')
            send_command(command, ser)
            sample_rate = 20

        elif rate <= 25:
            command = 0x06
            print('Bandwidth: 25Hz')
            send_command(command, ser)
            sample_rate = 25

        elif rate <= 30:  # Default
            command = 0x07
            print('Bandwidth: 30Hz')
            send_command(command, ser)
            sample_rate = 30

        else:
            command = 0x00
            print('Default Bandwidth: 10Hz')
            send_command(command, ser)
            sample_rate = 10

    else:
        command = 0x00              # Default
        print('Bandwidth: 10Hz')
        send_command(command, ser)
        sample_rate = 10

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