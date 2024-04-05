from pyfirmata import Arduino, OUTPUT
from time import sleep

port = '/dev/cu.usbmodem11101'
board = Arduino(port)

pin_number = 8  # Change this to your desired pin number
board.digital[pin_number].mode = OUTPUT

def turn_on():
    print("Turning on")
    board.digital[8].write(1)
    print("On")

def turn_off():
    print("Turning off")
    board.digital[8].write(0)
    print("Off")

# while True:
#     turn_on(pin_number)
#     sleep(2)
#     turn_off(pin_number)
#     sleep(2)
