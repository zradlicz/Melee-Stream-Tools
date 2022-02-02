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

def disp_player(im, player, p1):
    print('pressed')
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
    #im[org[1]-45:org[1]-45+qr.shape[0], org[0]-70:org[0]-70+qr.shape[1],0] = qr
    #im[org[1]-45:org[1]-45+qr.shape[0], org[0]-70:org[0]-70+qr.shape[1],1] = qr
    #im[org[1]-45:org[1]-45+qr.shape[0], org[0]-70:org[0]-70+qr.shape[1],2] = qr
    #im[org[1]:org[1]+qr.shape[0], org[0]:org[0]+qr.shape[1],1] = qr
    #im[org[1]:org[1]+qr.shape[0], org[0]:org[0]+qr.shape[1],2] = qr
    cv2.imshow('Results',im)
    return im

def clear(im):
    im = np.zeros((1000,1000,3))
    cv2.imshow('Results',im)

def read_player_data(filename):
    players = {}      
    with open(filename+'.csv',newline='') as csvfile:
              reader = csv.reader(csvfile, delimiter=',',quotechar='|')
              for row in reader:
                  players[row[0].lower()] = [row[1],None]
    return players

players = read_player_data('PlayerData')

# Create a new window with the title "Address Entry Form"
window = tk.Tk()
window.title("CHECKIN")

# Create a new frame `frm_form` to contain the Label
# and Entry widgets for entering address information.
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Pack the frame into the window
frm_form.pack()

# Create the Label and Entry widgets for "First Name"
lbl_p1 = tk.Label(master=frm_form, text="Player 1:")
ent_p1 = tk.Entry(master=frm_form, width=50)
#p1 = ent_p1.get()

p1 = 'DARTS'
# Use the grid geometry manager to place the Label and
# Entry widgets in the first and second columns of the
# first row of the grid
lbl_p1.grid(row=0, column=0, sticky="e")
ent_p1.grid(row=0, column=1)

# Create the Label and Entry widgets for "Last Name"
lbl_p2 = tk.Label(master=frm_form, text="Player 2:")
ent_p2 = tk.Entry(master=frm_form, width=50)
p2 = ent_p2.get()
# Place the widgets in the second row of the grid
lbl_p2.grid(row=1, column=0, sticky="e")
ent_p2.grid(row=1, column=1)

# Create a new frame `frm_buttons` to contain the
# Submit and Clear buttons. This frame fills the
# whole window in the horizontal direction and has
# 5 pixels of horizontal and vertical padding.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# Create the "Submit" button and pack it to the
# right side of `frm_buttons`
im = np.zeros((1000,1000,3))

btn_disp = tk.Button(master=frm_buttons, text="Display", command=disp_player(im,p1,True))
btn_disp.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Create the "Clear" button and pack it to the
# right side of `frm_buttons`
btn_clear = tk.Button(master=frm_buttons, text="Clear", command=clear(im))
btn_clear.pack(side=tk.RIGHT, ipadx=10)

# Start the application
window.mainloop()