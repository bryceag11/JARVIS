
#return input volts
def get_voltage(ser):
    ser.write(bytearray([0, 38]))
    return ser.read(1) #TODO convert this to int?

def get_mode(ser):
    ser.write(bytearray([0, 43]))
    return ser.read(1) #TODO covert thsi to int?

#motor 1 or both depending on mode
def set_speed1(ser, speed):
    ser.write(bytearray([0, 49, speed])) #TODO convert to int?

#motor 2 or turn value depending on mode
def set_speed2(ser, speed):
    ser.write(bytearray([0, 50, speed])) #TODO convert to int?

# 0 (reverse), 128 (stop), 255 (forward), individual motor controls
def set_mode0(ser):
    ser.write(bytearray([0, 52, 0]))

# -128 (reverse), 0 (stop), 127 (forward), individual motor controls
def set_mode1(ser):
    ser.write(bytearray([0, 52, 1]))

# same as mode_0, speed1 controls both motors, speed2 controls turn
def set_mode2(ser):
    ser.write(bytearray([0, 52, 2]))

# same as mode_1, speed1 controls both motors, speed2 controls turn
def set_mode3(ser):
    ser.write(bytearray([0, 52, 3]))

def set_mode(ser, mode):
    ser.write(bytearray([0, 52, mode]))

#set encoder values back to 0
def zero_encoders(ser):
    ser.write(bytearray([0, 53]))

def disable_regulator(ser):
    ser.write(bytearray([0, 54]))

def enable_regulator(ser):
    ser.write(bytearray([0, 55]))

#motors timeout after 2 seconds if no command has been received via UART
def disable_timeout(ser):
    ser.write(bytearray([0, 56]))

def enable_timeout(ser):
    ser.write(bytearray([0, 57]))

