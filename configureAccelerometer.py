#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import serial


def configure_accl(rate, ser):
    sample_rate = None

    # Stop the Data Stream
    command = 0x00
    send_command(command, ser)

    # Select Accelerometer
    command = 0xAA
    print('Accelerometer selected')
    send_command(command, ser)

    # Configure range
    command = 0x03                 # default value +-2g
    print('Default value: +-2g')
    send_command(command, ser)

    # Select Bandwidth
    if rate:
        if rate <= 8:
            command = 0x08
            print('Bandwidth: 8Hz')
            send_command(command, ser)
            sample_rate = 8

        elif rate <= 16:
            command = 0x09
            print('Bandwidth: 16Hz')
            send_command(command, ser)
            sample_rate = 16

        elif rate <= 31:
            command = 0x0A
            print('Bandwidth: 31Hz')
            send_command(command, ser)
            sample_rate = 31

        elif rate <= 63:
            command = 0x0B
            print('Bandwidth: 63Hz')
            send_command(command, ser)
            sample_rate = 63

        elif rate <= 125:
            command = 0x0C
            print('Bandwidth: 125Hz')
            send_command(command, ser)
            sample_rate = 125

        elif rate <= 250:
            command = 0x0D
            print('Bandwidth: 250Hz')
            send_command(command, ser)
            sample_rate = 250

        elif rate <= 500:
            command = 0x0E
            print('Bandwidth: 500Hz')
            send_command(command, ser)
            sample_rate = 500

        else:
            command = 0x0F
            print('Bandwidth: 1KHz')
            send_command(command, ser)
            sample_rate = 1000

    else:
        command = 0x0F                  # Default
        print('Bandwidth: 1KHz')
        send_command(command, ser)
        sample_rate = 1000

    # Select Mode
    command = 0x00                    # PM Normal Mode(Default)
    print('Mode: PM Normal Mode (Default)')
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