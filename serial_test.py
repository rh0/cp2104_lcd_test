import curses
import serial
from time import sleep

# Create a simple curses screen.
stdScr = curses.initscr()
curses.cbreak()
curses.noecho()
stdScr.keypad(1)

# CP2104 shows up as ttyUSB0 on my system, this may need to be adjusted on others.
ser = serial.Serial('/dev/ttyUSB0', 9600)

# A few of the commands for serLCD
COMMAND     = 0xFE
CLEAR       = 0x01
BLINK_ON    = 0x0D
BLINK_OFF   = 0x0D
UL_ON       = 0x0E
UL_OFF      = 0x0C

def serCmd(bits):
    ser.write(bytes([COMMAND]))
    ser.write(bytes([bits]))
    sleep(.1)

serCmd(CLEAR)
serCmd(UL_ON)

stdScr.addstr(0,0,"Send characters to " + ser.name)
stdScr.addstr(1,0,"press <esc> to exit.")

# Send key presses to serial, kill the loop on <esc>.
key = ''
while key != 27:
    key = stdScr.getch()
    if key == ord('\n'):
        serCmd(CLEAR)
    else:
        ser.write(bytes([key]))

curses.endwin()
ser.close()
exit()
