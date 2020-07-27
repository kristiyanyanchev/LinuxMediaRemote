# Media Remote for Linux
## How to use Media Remote
### Setup
1. Connect arduino and IR sensor as showed in Arduino Scheme
2. Verify and upload code via Arduino IDE
3. Run the script(remote.py)
4. Get some ir remote(tv remote, ac remote or some remote with LED-like bulb on front, your car remote most probably wont work)
5. Check if your button codes are same(they are different for each type of remote eg. Samsung, Sony, LG )
6. If they are same and your remote works, Enjoy your remote controlled media. Else press any button, in terminal where script is running will be shown button code (Hex code). Replace it in the script under action you want.
### Errors that can occur
```python
serial.serialutil.SerialException: [Errno 16] could not open port /dev/ttyACM0: [Errno 16] Device or resource busy: '/dev/ttyACM0'
```
You most probably unpluged your divice and pluged it back. Serial port(tty) changed its name from ttyACM0 to ttyACM1 or some other ttyACM port.
Reboot your system or reupload Arduino code via Arduino IDE.

## Arudino Scheme
![alt text](https://raw.githubusercontent.com/kristiyanyanchev/LinuxMediaRemote/master/ArduinoScheme.png "Logo Title Text 1")
