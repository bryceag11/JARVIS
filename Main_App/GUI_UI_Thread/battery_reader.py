import serial
import time

# Simulation of Arduino variables
reference_volts = 5
resistor1 = 976000
resistor2 = 98500
battery_pin = "A0"  # Simulating analog pin A0

# Simulated buffer for voltage readings
voltage_battery = [0.0] * 10
count = 1
index = 0

# Find and open the serial port for Arduino
ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600,timeout=.015)
print("//waiting for Serial connection...")

def find_charge(battery_voltage):
    # Your battery percentage calculation logic here based on voltage
    if battery_voltage <= 45.5:
        return 0
    elif battery_voltage <= 46.04:
        return 10
    elif battery_voltage <= 46.64:
        return 20
    elif battery_voltage <= 47.24:
        return 30
    elif battery_voltage <= 47.84:
        return 40
    elif battery_voltage <= 48.40:
        return 50
    elif battery_voltage <= 48.96:
        return 60
    elif battery_voltage <= 49.48:
        return 70
    elif battery_voltage <= 50:
        return 80
    elif battery_voltage <= 50.48:
        return 90
    elif battery_voltage <= 50.92:
        return 100
    else:
        return 100  # Default to 100 if voltage exceeds the upper limit

while True:
    # Simulated analog read
    ser.write(b'A')
    val_bytes = ser.readline()
    value = val_bytes.decode().strip()
    print(value)
    value = float(value)
    voltage_reading = (value / 1024.0) * reference_volts
    # Calculate voltage across resistor 2
    voltage_battery[index] = voltage_reading * ((resistor1 + resistor2) / resistor2)
    voltage_battery[index] = voltage_battery[index] * (5.0 / 4.9)  # Adjust for inaccuracies

    # Calculate average voltage reading
    voltage_battery_avg = sum(voltage_battery) / count

    # Calculate battery charge percentage
    battery_charge = find_charge(voltage_battery_avg)

    # Simulated serial print
    print("Battery Charge:", battery_charge)

    # Increment count and index
    if count < 10:
        count += 1

    if index < 9:
        index += 1
    else:
        index = 0

    time.sleep(0.5)  # Simulating delay(500) for half a second
