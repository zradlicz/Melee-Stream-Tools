# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 19:41:40 2022

@author: zradlicz
"""

import cv2
import numpy as np
import sys
import time
import csv

players = {'darts':['He/Him',None],
           'strad':['They/Them',None],
           'drats':['She/Her',None]}
  
def read_player_data(filename):
    players = {}      
    with open(filename+'.csv',newline='') as csvfile:
              reader = csv.reader(csvfile, delimiter=',',quotechar='|')
              for row in reader:
                  players[row[0].lower()] = [row[1],None]
    return players

players = read_player_data('PlayerData')

vid = cv2.VideoCapture(0)

def display(im,bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[(j+1) % n][0]),(255,0,0),3)
        cv2.imshow('Results',im)
        
def disp_player(im, player, p1):
    props = players[player.lower()]
    tag = player
    pronouns = props[0]
    qr = props[1]
    
    font = cv2.FONT_HERSHEY_TRIPLEX
    if(p1):
        org = (75,50)
        color = (255, 255, 255)
    else:
        org = (75,450)
        color = (255,255,255)
    
    fontScale = 1
    
    thickness = 2
    #print(tag)
    
    im = cv2.putText(im, tag+' | '+pronouns, org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
    im[org[1]-45:org[1]-45+qr.shape[0], org[0]-70:org[0]-70+qr.shape[1],0] = qr
    im[org[1]-45:org[1]-45+qr.shape[0], org[0]-70:org[0]-70+qr.shape[1],1] = qr
    im[org[1]-45:org[1]-45+qr.shape[0], org[0]-70:org[0]-70+qr.shape[1],2] = qr
    #im[org[1]:org[1]+qr.shape[0], org[0]:org[0]+qr.shape[1],1] = qr
    #im[org[1]:org[1]+qr.shape[0], org[0]:org[0]+qr.shape[1],2] = qr
    cv2.imshow('Results',im)
    return im
    

p1 = None
p2 = None

count = 0
while(True):
    ret, frame = vid.read()
    print(p1,p2)
    qrDecoder = cv2.QRCodeDetector()
    data,bbox,rectifiedImage = qrDecoder.detectAndDecode(frame)
    
    # Display the resulting frame
    #cv2.imshow('frame', frame)
    if len(data)>0:
        recifiedImage = np.uint8(rectifiedImage)
        rectifiedImage = cv2.resize(rectifiedImage,(64,64),interpolation = cv2.INTER_AREA)
        if(p2 and (format(data)!=p1 and format(data)!=p2)):
            p1 =format(data)
            players[p1.lower()][1] = rectifiedImage
            players[p2.lower()][1] = None
            p2=None
            
        if(not p1):
            p1 = format(data)
            players[p1.lower()][1] = rectifiedImage
        if format(data)!=p1:
            p2 = format(data)
            players[p2.lower()][1] = rectifiedImage
        
        #print('decoded data: {}'.format(data))
        #display(frame,bbox)
        
        
         #cv2.imshow('Rectified QRCode',rectifiedImage)
         
    
    if(p1):
        frame = disp_player(frame,p1,True)
    if(p2):
        frame = disp_player(frame,p2,False)
    
    else:
        #print("No QR Code")
        cv2.imshow('Results', frame)
        
    #cv2.imwrite('video\example_frame'+str(count)+'.jpg',frame)
    cv2.imwrite('video\example_frame_'+str(count).zfill(4)+'.jpg',frame)
    count+=1
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()