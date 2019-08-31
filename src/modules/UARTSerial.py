import serial

class Serial:
    def __init__(self, port, baud_rate):
        self.ser = serial.Serial(port, baud_rate)
        self.ser.reset_input_buffer()
    def read(self):
        self.ser.reset_input_buffer()
        return self.ser.read_until()
    def write(self, string):
        self.ser.reset_input_buffer()
        return self.ser.write(string)
