#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:11:01 2021

@author: lucaliverani
"""

import socket
import time
import numpy as np

# import subprocess

# wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
# data = wifi.decode('utf-8')


DEFAULT_PORT = 10003


if 0:


    
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # Set a timeout so the socket does not block
    # indefinitely when trying to receive data.
    server.settimeout(0.2)
    #server.bind(("", 0))
    server.bind(('<broadcast>', DEFAULT_PORT))
    message = b"y"
    while True:
        a=server.sendto(message, ('<broadcast>', DEFAULT_PORT-1))
        print(a)
        print("message sent!")
        time.sleep(1)
        
        

if 0:
    localIP     = "127.0.0.1"
    
    localPort   = 10004
    
    bufferSize  = 1024
    
     
    
    msgFromServer       = "Hello UDP Client"
    
    bytesToSend         = str.encode(msgFromServer)
    
     
    
    # Create a datagram socket
    
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    
     
    
    # Bind to address and ip
        
    if 0:
        broadportAddressPort= ("255.255.255.255", DEFAULT_PORT)
        UDPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    else:
        broadportAddressPort= (localIP, localPort)
    
    #UDPServerSocket.bind((localIP, localPort))
    UDPServerSocket.bind(broadportAddressPort)

    
     
    
    print("UDP server up and listening")
    
     
    
    # Listen for incoming datagrams
    
    while(True):
    
        if 0:
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        
            message = bytesAddressPair[0]
        
            address = bytesAddressPair[1]
        
            clientMsg = "Message from Client:{}".format(message)
            clientIP  = "Client IP Address:{}".format(address)
            
            print(clientMsg)
            print(clientIP)
    
       
    
        # Sending a reply to client
    
        UDPServerSocket.sendto(bytesToSend, broadportAddressPort)
        print(bytesToSend)
        
        time.sleep(1)
        
        
        
        
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_A=s.getsockname()[0]
print()
s.close()
     
        
import uuid

mac_A=':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1])
    
    

localIP     = "127.0.0.1"
hostname = socket. gethostname()
local_ip = socket. gethostbyname(hostname)
print(local_ip)

DEFAULT_PORT = 8232

bufferSize  = 1024

#$%LL%$**Light1**192.168.1.4**8232** 

#msgFromServer       = "$%LL%$**Light1**" + ip_A + "**" + mac_A +"**"+ str(DEFAULT_PORT)
cc=0
msgFromServer       = "$%LL%$**Light" +str(cc)+ "**" + local_ip + "**" + str(DEFAULT_PORT) +"**"
bytesToSend         = str.encode(msgFromServer)

 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
UDPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

 

# Bind to address and ip

UDPServerSocket.bind((local_ip, DEFAULT_PORT))
#UDPServerSocket.bind(('<broadcast>', DEFAULT_PORT-1))



print("UDP server up and listening")
sendingport=10001
 

# Listen for incoming datagrams

while(True):

    if 0: 
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    
        message = bytesAddressPair[0]
    
        address = bytesAddressPair[1]
    
        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
        
        print(clientMsg)
        print(clientIP)

   

    cc=0
    while cc<4:
        battery=str(int(np.round(100*np.random.random(1))[0]))
        msgFromServer       = "$%LL%$**Light" +str(cc+1)+ "**" + local_ip + "**" + str(sendingport+cc) +"**"+\
        "Vodafone-75"+"**"+battery+"**"
        bytesToSend         = str.encode(msgFromServer)
        cc=cc+1

        UDPServerSocket.sendto(bytesToSend,("192.168.1.255", DEFAULT_PORT))
        time.sleep(0.2)
        
    time.sleep(2)
    
    print("message "+ msgFromServer+ " sent!")
    # time.sleep(1)
        
        
        
        
        
