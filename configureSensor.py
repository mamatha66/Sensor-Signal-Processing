#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import configureAccelerometer
from . import configureGyroscope
from . import configureMagnetometer


def configure(sensor, rate, ser):
    if sensor == 'Acc':
        sample_rate = configureAccelerometer.configure_accl(rate, ser)

    elif sensor == 'Gyr':
        sample_rate = configureGyroscope.configure_gyro(rate, ser)

    elif sensor == 'Mag':
        sample_rate = configureMagnetometer.configure_mag(rate, ser)

    else:
        sample_rate = None

    return sample_rate