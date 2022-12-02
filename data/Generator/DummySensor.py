import HealthDataGenerator
import socket
import time

port = 9852 
address = ('10.24.90.91',port)

""" 
Creates a socket and connects to specified adress 
"""
def connect():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(address)
    return s

"""
Sends medicaldata which are extracted from a data-generator
"""
def sendMedicalData(duration):
    
    print("Trying to establish connection")
    
    connection = connect()
    
    print("Connection established")
    
    AllPatientData = HealthDataGenerator.generateRegisteredSensorData(duration)
        
    for data in AllPatientData:
        
        packet = data
        
        connection.send(packet.encode("utf-8"))

        time.sleep(1)

        print("Packet sent")

    print("Data sent")
               
sendMedicalData(5)        
        
      


