import serial
from pyautogui import press, typewrite, hotkey

ser = serial.Serial('/dev/ttyACM0')
while True :
    line = ser.readline()
    print(line)
    #Start/Pause
    if line == b'FDA05F\r\n':
        press('space')
    #Volume up
    elif line == b'FD807F\r\n' :
        press('up')
    #Volume down
    elif line == b'FD906F\r\n' :
        press('down')
    #Skip
    elif line == b'FD609F\r\n' :
        press('right')
    #Return
    elif line == b'FD20DF\r\n' :
        press('left')
    #FullScreen
    elif line == b'FD40BF\r\n' :
        press('f')
    #Next in playlist
    elif line == b'FD50AF\r\n' :
        hotkey('shift','n')
    #Previous in playlist
    elif line == b'FD10EF\r\n' :
       hotkey('shift','p')
     #OFF
    elif line == b'FD00FF\r\n' :
        break
