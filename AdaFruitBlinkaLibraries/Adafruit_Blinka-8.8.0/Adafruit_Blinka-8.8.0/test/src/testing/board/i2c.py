# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
from adafruit_blinka import agnostic

if agnostic.board in ("feather_m0_express", "feather_huzzah"):
    from bitbangio import I2C
elif agnostic.board == "pyboard":
    from busio import I2C
else:
    raise NotImplementedError("Board not supported")
