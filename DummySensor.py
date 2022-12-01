import HealthDataGenerator
import socket

port = 58912 
address = ('172.20.10.2',port)

""" 
Creates a socket and connects to specified adress 
"""
def connect():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(address)
    return s

"""
Sends medicaldata which are extracted from a datagenerator
"""
def sendMedicalData(duration):
    
    print("Trying to establish connection")
    
    connection = connect()
    
    print("Connection established")
    
    AllPatientData = HealthDataGenerator.generateRegisteredSensorData(duration)
        
    for data in AllPatientData:
        
        packet = data
        
        connection.send(packet.encode("utf-8"))
        
                       
               
sendMedicalData(5)        
        
      


