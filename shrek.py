# franky campuzano
# shrek frame generator
# jan 11 2021
# all rights reserved

import random
import tweepy
import math

import os
import sys

import cv2
import subprocess
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


# *** shrek account keys go here ***

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def finalScript():
	
    countfile = open('/home/franky/shrekframecount.txt','r')
    count = countfile.readlines()
    count = int(count[0])
    print(count)

    stop = 0
    marker = int(count/1000) * 1000
    print (str(marker))
    while stop < 5:
        filename = "/media/franky/FDRIVE/shrekframes/frames"+ str(marker)+"/shframe"+str(count+stop)+".JPEG"
        text = "Shrek (2001)\n\nFrame "+ str(count+stop) +" of 129575"
        stop+= 1
        #endtextformat
        tweet(text, filename)

	
    countfile.close()

    file_marker = open('/home/franky/shrekframecount.txt','w+')
    file_marker.write(str(count+stop))
    file_marker.close()

def tweet(text, filepath):
    api.update_with_media(filepath, text)


if __name__ == '__main__':
    finalScript()
