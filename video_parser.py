# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:38:47 2022

@author: 32505
"""

#Twitch api to download video to specified folder

#parse frame by frame through video place markers on timestamps for sections with two qr codes on screen

#get tag from qr code and look up tag an character in PlayerData

#create thumbnail with tags and characters and name of tournament

#OPTIONAL Use smash.gg api to get game in the tournament

#use youtube api to upload each section with the names and characters as titles

import cv2
import numpy as np
import sys
import time
import csv

def read_player_data(filename):
    players = {}      
    with open(filename+'.csv',newline='') as csvfile:
              reader = csv.reader(csvfile, delimiter=',',quotechar='|')
              for row in reader:
                  players[row[0].lower()] = [row[1],None]
    return players

players = read_player_data('PlayerData')

def download_video():
    return

def make_thumbnail(p1, p2, game, tournament):
    return
    
def make_title(p1, p2, game, tournament):
    p1_char = players[p1][2]
    p2_char = players[p2][2]
    return tournament + ': ' + game + '  -  ' + p1 + ' ('+p1_char+') vs. ' + p2 + ' ('+p2_char+')'