import config
import rfm69
import board
import time
import busio
import digitalio

spi = busio.SPI(board.GP2, MOSI=board.GP3, MISO=board.GP0)
cs = digitalio.DigitalInOut(board.GP1)
reset = digitalio.DigitalInOut(board.GP4)
rfm69 = rfm69.RFM69(spi, cs, reset, config.FREQUENCY)

def getGPS():
    return ("10.284638, 89.473057")

def sendHello():
    gps = getGPS()
    return rfm69.send(data = bytes(gps, "utf-8"), destination = config.BROADCAST, packetType = config.HELLO)
    
while True:
    print(sendHello())
    time.sleep(1)