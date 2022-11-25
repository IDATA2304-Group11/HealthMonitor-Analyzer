
'''
    ANALYZER

Represents a component of the application, which
is implemented in a Raspberry Pi Microcomputer.<p>

This program will be able to receive data from a
sensor. This data will be processed and wrapped
into a package which can be sent to the backend
part of the application.

@author 
    jorgenfinsveen
@version
    10-11-2022
@since
    10-11-2022
'''

# Modules
import pandas as pd
import numpy as np
import socket
import time



# Names of target column-labels.
ALIAS = {
    'id': 'Device Model Name',
    'sys': 'SYS',
    'dia': 'DIA',
    'pulse': 'Pulse',
    'date': 'Measurement Date'
}

# Server IP address and port number.
HOST = '10.24.90.151'
PORT = 8888

# Running iterations for testing.
running = 10
counter = 0



'''
    RECEIVING DATA - (dummy-data adjustment.)
'''

# Reading raw data from csv-file.
data = pd.read_csv('data/bp_log.csv')





'''
    PROCESSING DATA 
'''

# Converting date-column into pandas.Timestamp-objects.
data[ALIAS['date']] = pd.to_datetime(data[ALIAS['date']])

# NumPy Array for device model name.
mID = np.array(data[ALIAS['id']])

# NumPy Arrays for blood pressure sys/dia.
sys = np.array(data[ALIAS['sys']])
dia = np.array(data[ALIAS['dia']])

# NumPy Array for heart rate.
heartrate = np.array(data[ALIAS['pulse']])

# NumPy Array for each measurement date.
date = np.array(data[ALIAS['date']])




'''
    SENDING DATA 
'''

while (running > 0):

    time.sleep(2)

    packet = str(mID[counter]) + ';'
    packet += str(sys[counter]) + ';'
    packet += str(dia[counter]) + ';'
    packet += str(heartrate[counter]) + ';'
    packet += str(date[counter])

    running -= 1
    counter += 1

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(packet.encode("utf-8"))