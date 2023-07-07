import serial
import time
from serialPorts import serial_ports
import numpy as np
import matplotlib.pyplot as plt

ports = serial_ports()
# print(ports)
print("Connecting to "+ports[-1]+"...")
arduino = serial.Serial(ports[-1], 9600)
print("Connected")
def log(splitTime, totalTime): #in seconds
    sleepTime = splitTime/10.0
    print("Start log...")
    data = []
    startTime = time.time()
    while (time.time()<startTime+totalTime):
        while (time.time()-startTime) % splitTime > sleepTime:
            time.sleep(sleepTime)
        tdata = arduino.readline().decode().strip("\n").strip("\r").split(" ")
        for i in range(len(tdata)):
            tdata[i] = float(tdata[i])/1024.0 * 5.0
        data.append([time.time()-startTime]+tdata)
        # print([time.time()-startTime]+tdata)
        
        time.sleep(sleepTime)
    print("Log complete.")
    return data

data = np.array(log(0.001,5))

plt.figure(figsize=(10,5))
# print(data[:,0])
plt.plot(data[:, 0], data[:, 1])
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.show()

arduino.close()



