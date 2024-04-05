from pyfirmata import Arduino, SERVO
from time import sleep


port = '/dev/cu.usbmodem11101'
board = Arduino(port)

board.digital[10].mode = SERVO

def openDoor():
    print("Opening")
    board.digital[10].write(120)
    print("Opening Finished")
    # sleep(2)

def closeDoor():
    print("Closing")
    board.digital[10].write(30)
    print("Closing Finished")
    # sleep(2)

# while True:
#     openDoor()
#     closeDoor()
