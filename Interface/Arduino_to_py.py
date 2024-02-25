import serial
import time
    
def read():
	ser = serial.Serial(
		port='/dev/cu.usbmodem1101',
		baudrate=115200,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
	)


	data = ser.readline().decode('utf-8').strip()
	data = data.split(',')
	for i in range(len(data)):
		if data[i] != '':
			data[i] = float(data[i])

	print(data)

	return [{'Heart_Value': data[0],
		   	 'Noise': data[1],
			 'Temperature': data[2],
			 'Humidity': data[3]}]

#read()

while True:
    read()
    time.sleep(1)
