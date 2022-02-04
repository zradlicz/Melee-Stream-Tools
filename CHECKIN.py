# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 16:07:16 2022

@author: 32505
"""

import cv2
import numpy as np
import sys
import time
import csv
import tkinter as tk
import png
import pyqrcode

global QR

QR = False

def disp():
    im = np.zeros((300,1250,3))
    p1 = ent_p1.get()
    p2 = ent_p2.get()
    
    
        
    try:
        p1_props = players[p1.lower()]
    except:
        qr = pyqrcode.create(p1.lower())
        qr.png("QR/"+p1+".png", scale = 5)
        qrim = cv2.imread('QR/'+p1+'.png')
        p1_props = ['They/Them',qrim]
    p1_tag = p1
    p1_pronouns = p1_props[0]
    p1_qr = p1_props[1]
    
    try:
        p2_props = players[p2.lower()]
    except:
        qr = pyqrcode.create(p2.lower())
        qr.png("QR/"+p2+".png", scale = 5)
        qrim = cv2.imread('QR/'+p2+'.png')
        p2_props = ['They/Them',qrim]
    p2_tag = p2
    p2_pronouns = p2_props[0]
    p2_qr = p2_props[1]
    
    p1_org = (75,50)
    p1_color = (255,255,255)
    
    p2_org = (650,50)
    p2_color = (255,255,255)
    
    font = cv2.FONT_HERSHEY_TRIPLEX
    fontScale = 1
    thickness = 2
    
    im = cv2.putText(im, p1_tag+' | '+p1_pronouns, p1_org, font, 
                   fontScale, p1_color, thickness, cv2.LINE_AA)
    im = cv2.putText(im, p2_tag+' | '+p2_pronouns, p2_org, font, 
                   fontScale, p2_color, thickness, cv2.LINE_AA)
    
    #p1_props[1] = cv2.resize(p1_props[1],(64,64),interpolation = cv2.INTER_AREA)
    #p2_props[1] = cv2.resize(p2_props[1],(64,64),interpolation = cv2.INTER_AREA)
    
    if QR:
        im[p1_org[1]+45:p1_org[1]+45+p1_props[1].shape[0], p1_org[0]+70:p1_org[0]+70+p1_props[1].shape[1]] = p1_props[1]
        #im[p1_org[1]-45:p1_org[1]-45+p1_props[1].shape[0], p1_org[0]-70:p1_org[0]-70+p1_props[1].shape[1],1] = p1_props[1]
        #im[p1_org[1]-45:p1_org[1]-45+p1_props[1].shape[0], p1_org[0]-70:p1_org[0]-70+p1_props[1].shape[1],2] = p1_props[1]
        
        im[p2_org[1]+45:p2_org[1]+45+p2_props[1].shape[0], p2_org[0]+70:p2_org[0]+70+p2_props[1].shape[1]] = p2_props[1]
        #im[p2_org[1]-45:p2_org[1]-45+p2_props[1].shape[0], p2_org[0]-70:p2_org[0]-70+p2_props[1].shape[1],1] = p2_props[1]
        #im[p2_org[1]-45:p2_org[1]-45+p2_props[1].shape[0], p2_org[0]-70:p2_org[0]-70+p2_props[1].shape[1],2] = p2_props[1]
    
   
    
    
    cv2.imshow('Players',im)
    
def qr_en():
    global QR
    if QR:
        QR = False
    else:
        QR = True
    disp()
    

def clear():
    im = np.zeros((300,1500,3))
    cv2.imshow('Players',im)

def read_player_data(filename):
    players = {}      
    with open(filename+'.csv',newline='') as csvfile:
              reader = csv.reader(csvfile, delimiter=',',quotechar='|')
              for row in reader:
                  tag = row[0].lower()
                  qr = pyqrcode.create(tag)
                  qr.png("QR/"+tag+".png", scale = 5)
                  qrim = cv2.imread('QR/'+tag+'.png')
                  players[row[0].lower()] = [row[1],qrim]
    return players






players = read_player_data('PlayerData')

window = tk.Tk()
window.title("CHECKIN")


frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

lbl_p1 = tk.Label(master=frm_form, text="Player 1:")
ent_p1 = tk.Entry(master=frm_form, width=50)


lbl_p1.grid(row=0, column=0, sticky="e")
ent_p1.grid(row=0, column=1)


lbl_p2 = tk.Label(master=frm_form, text="Player 2:")
ent_p2 = tk.Entry(master=frm_form, width=50)


lbl_p2.grid(row=1, column=0, sticky="e")
ent_p2.grid(row=1, column=1)


frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)


btn_disp = tk.Button(master=frm_buttons, text="Display", command=disp)
btn_disp.pack(side=tk.RIGHT, padx=10, ipadx=10)


btn_clear = tk.Button(master=frm_buttons, text="Clear", command=clear)
btn_clear.pack(side=tk.RIGHT, padx=10, ipadx=10)


btn_qr = tk.Button(master=frm_buttons, text="QR Toggle", command=qr_en)
btn_qr.pack(side=tk.RIGHT, ipadx=10)
window.mainloop()




