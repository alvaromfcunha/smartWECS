import serial

class Serial:
    def __init__(self, port, baud_rate):
        self.ser = serial.Serial(port, baud_rate)
        ser.reset_input_buffer()
    def read(self):
        ser.reset_input_buffer()
        return self.ser.read_until()
    def write(self, string):
        ser.reset_input_buffer()
        return self.ser.write(string)
