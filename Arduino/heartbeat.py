# import serial
# import time


# def read():
# 	ser = serial.Serial(
# 		port='/dev/cu.usbmodem101',
# 		baudrate=9600,
# 		parity=serial.PARITY_NONE,
# 		stopbits=serial.STOPBITS_ONE,
# 		bytesize=serial.EIGHTBITS,
# 	)


# 	data = ser.readline().decode('utf-8').strip()
# 	data = data.split(',')
# 	for i in range(len(data)):
# 		if data[i] != '':
# 			data[i] = int(data[i])

# 	print(data)

# 	return [{'Loudness': data[0]}]

# read()





# import serial
# import time

# def read():
#     ser = serial.Serial(
#         port='/dev/cu.usbmodem101',
#         baudrate=9600,
#         parity=serial.PARITY_NONE,
#         stopbits=serial.STOPBITS_ONE,
#         bytesize=serial.EIGHTBITS,
#     )

#     # Variables for peak detection
#     prev_loudness = 0
#     peak_count = 0
#     start_time = time.time()

#     while True:
#         data = ser.readline().decode('utf-8').strip()
#         data = data.split(',')
#         if len(data) > 0 and data[0] != '':
#             loudness = int(data[0])

#             # Check for a peak
#             if loudness > prev_loudness:
#                 peak_count += 1

#         # Reset peak count every minute
#         if time.time() - start_time >= 6:
#             start_time = time.time()
#             print({'Heartbeat Peaks': peak_count})  # Print total peaks per minute
#             peak_count = 0  # Reset peak count

#         prev_loudness = loudness

# read()






import serial
import time

def read():
    ser = serial.Serial(
        port='/dev/cu.usbmodem101',
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
    )

    interval = 10  # Set the interval to 10 seconds
    peak_threshold = 200  # Adjust this threshold based on your sensor characteristics
    peak_count = 0
    start_time = time.time()

    while True:
        try:
            data = ser.readline().decode('utf-8').strip()
            data = data.split(',')
            for i in range(len(data)):
                if data[i] != '':
                    data[i] = int(data[i])

            #print(data)

            # Check for a peak (heartbeat)
            if data[0] > peak_threshold:
                peak_count += 1

            # Calculate heart rate and reset peak count at the end of each interval
            elapsed_time = time.time() - start_time
            if elapsed_time >= interval:
                heart_rate = (peak_count / elapsed_time) * 60.0  # Calculate beats per minute
                print(f"Heart Rate (BPM): {heart_rate}")
                with open("data.txt", 'a') as file:
                    file.write(heart_rate + "\n")

                peak_count = 0  # Reset peak count
                start_time = time.time()  # Reset the timer

        except KeyboardInterrupt:
            break

    ser.close()

read()
