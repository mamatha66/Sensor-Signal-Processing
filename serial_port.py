#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial.tools.list_ports


def serial_port():
    port = [p.device for p in serial.tools.list_ports.comports()]
            #if 'Silicon Labs CP210x USB to UART Bridge' in p.description]

    if not port:
        raise IOError("No USB-to-Serial device found")

    ser = serial.Serial(port=port[0],
                        baudrate=115200,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        timeout=None)

    try:
        ser.isOpen()
        print("Serial port is open")
        return ser
    except():
        print("ERROR")
        exit()