import os

from machine import UART

uart = UART(0, 115200)

os.dupterm(uart)
