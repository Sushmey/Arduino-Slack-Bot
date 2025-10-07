from flask import Flask, render_template
from flask import request
import serial
import time

arduino_port = 'port/to/read/arduino' # Example for Linux/macOS
baud_rate = 9600

def getData(kind="both"):
	try:
	    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
	    time.sleep(2)  # Allow time for Arduino to reset after opening serial

	    print(f"Connected to Arduino on {arduino_port}")
	    data = []
	    while True:
	        if ser.in_waiting > 0:
	            for i in range(0,4):
	            	line = ser.readline().decode('utf-8').strip()
	            	print(f"Received from Arduino: {line}")
	            	data.append(line)
	            break
	        else: continue
	        break
	    if(val=="temp"):
	    	index = data.
	    return data


	except serial.SerialException as e:
	    print(f"Error: Could not open serial port {arduino_port}. {e}")
	except KeyboardInterrupt:
	    print("Program terminated by user.")
	finally:
	    if 'ser' in locals() and ser.is_open:
	        ser.close()
	        print("Serial port closed.")
	        if(data): return data


def get_temp():
