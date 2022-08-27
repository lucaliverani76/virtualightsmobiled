#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 13:32:50 2021

@author: lucaliverani
"""

import socket
import sys
import cv2
import numpy as np
import time
import threading
import json

global color
global stoppa



color = [[255, 45, 36],[255, 45, 36],[255, 45, 36],[255, 45, 36],\
         [255, 45, 36]]
stoppa = False


def substrbetween(stringa):
    car1=-1
    car2=-1
    for u in range(0,len(stringa)):
        if stringa[u]=="{":
            car1=u
        if car1>-1 and stringa[u]=="}":
            car2=u
            break
    if car1>-1 and car2>-1:
        return stringa[car1:car2+1]
    else:
        return ""



def runcolor(index_):
    global stoppa
    global color
    
    if 1:
        myThread = threading.Thread(target=Runserver, args =(index_,))
        myThread.start()
    
    print("sono qui")
    # Center coordinates
    center_coordinates = (256, 256)
    
    # Window name in which image is displayed
    window_name = 'Light' + str(index_+1)
    
    # Create a black image
    img = np.zeros((512,512,3), np.uint8)
     
    # Radius of circle
    radius = 100
      
    # Blue color in BGR
    
    #colorx=color[2]
    # Line thickness of 2 px
    thickness = 110
      
    # Using cv2.circle() method
    # Draw a circle with blue line borders of thickness of 2 px

    while True:
    #    colorx=colorx+stepx
    #    if colorx==255:
    #        stepx=-1
    #    if colorx==0:
    #        stepx=1
    #    y = list(color)
    #    y[2] = colorx
    #    color = tuple(y)
    
        colorx=color[index_]

        image = cv2.circle(img,center_coordinates, radius, tuple(colorx), thickness)

          # Displaying the image 
        
        cv2.imshow(window_name, image) 

        if cv2.waitKey(1) == ord('q'):
            break
            stoppa=True
    
    cv2.destroyAllWindows()
    
    


#android=0       
#if android:
    
def Runserver(index_):    
    global stoppa
    global color
  
    # Create a TCP/IP socket
#    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#    
#    # Bind the socket to the port
#    server_address = ('192.168.1.4', 10002)
#    print (sys.stderr, 'starting up on %s port %s' % server_address)
#    sock.bind(server_address)
    
    
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    hostname = socket. gethostname()
    local_ip = socket. gethostbyname(hostname)
    server_address = (local_ip, 10001+index_)
    print (sys.stderr, 'starting up on %s port %s' % server_address)
    sock.bind(server_address)
        
    
    # Listen for incoming connections
    #sock.listen(1)
    myjason=""
    while True and stoppa==False:
        # Wait for a connection
        print (sys.stderr, 'waiting for a connection')
        #connection, client_address = sock.accept()
    
        #try:
        if 1:
            #print (sys.stderr, 'connection from', client_address)
    
            # Receive the data in small chunks and retransmit it
            while True:
                data, address = sock.recvfrom(4096)
                #data = connection.recv(32).decode()
                print(str(data))
                myjason=myjason + str(data)
                #print(myjason + "--->")
                temp=substrbetween(myjason)
                if temp!="":
                    #print (myjason)
                    #print("H")
                    try:
                        #print(temp)
                        decoded_hand = json.loads(temp)
                        # print(decoded_hand)
                        color[index_][2]= decoded_hand["red"]
                        color[index_][0]= decoded_hand["blue"]
                        color[index_][1]= decoded_hand["green"]
                        # print(color)
                        myjason=""
                    except:
                        print("che minchia e' sta robba!")
                        
                #print (myjason)
                if data:
                    pass
                else:
                    break
                
        #finally:
            # Clean up the connection
            #connection.close()

            sock.close()
            




for k in range(0,4):
    threading.Thread(target=runcolor, args=(k,)).start()




