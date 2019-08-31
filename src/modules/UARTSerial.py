import serial

class Serial:
    def __init__(self, port, baud_rate):
        self.ser = serial.Serial(port, baud_rate)
    def read(self):
        return self.ser.read_until(expected="\n\r")
    def write(self, string):
        return self.ser.write(string)
