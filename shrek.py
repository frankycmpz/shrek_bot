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
	#select random episode
	

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

    prevdmfile = open('/home/franky/shrekframecount.txt','w+')
    prevdmfile.write(str(count+stop))
    prevdmfile.close()

    #the rest of this code is basically just trying to download all of the frames of a movie
    #along with a loop that helps in the event that the program stops running, and u only get the first 40k of 100k frames

    #yes that happened to me



    #getting some random frame for a random bot
    '''
    timeSec = get_length(filename)
    print("length"+str(timeSec))
    timeMis = timeSec * 1000
    randTime = random.randint(0, timeMis)


    vidcap = cv2.VideoCapture(filename)
    vidcap.set(cv2.CAP_PROP_POS_MSEC,randTime)
    success,image = vidcap.read()
    '''

    #lets you catch up, in the event of a crash
    '''
    while some_undefined_frame_number > count:
        success = vidcap.read()
        count+=1
        if count%100 == 0:
            print(str(count))


    while success:

        screenCapFileName = "/media/franky/FDRIVE/shrek_movies/shrekframes/shrekframe"+str(count)+".JPEG"
        cv2.imwrite(screenCapFileName, image)     # save frame as JPEG file
        success,image = vidcap.read()
        count+=1

    #obv you gotta know
    print("total number of frames: "+ str(count))
    '''

    #if you just wanna attempt getting all of the frames in one go... go ahead
    '''
    filename = "/media/franky/FDRIVE/shrekmovies/shrek.mp4"
    count = 0

    vidcap = cv2.VideoCapture(filename)
    success,image = vidcap.read()

    marker = 0
    os.mkdir("/media/franky/FDRIVE/shrekframes/frames"+str(marker))

    while success:
        screenCapFileName = "/media/franky/FDRIVE/shrekframes/frames"+str(marker)+"/shframe"+str(count)+".JPEG"
        #print(screenCapFileName)
        cv2.imwrite(screenCapFileName, image)     # save frame as JPEG file
        success,image = vidcap.read()
        count+=1
        if count % 100 == 0:
            print(str(count))

        if count % 1000 == 0:
            marker += 1000
            os.mkdir("/media/franky/FDRIVE/shrekframes/frames"+str(marker))

    print("total number of frames: "+ str(count))

    '''

	#textformat if you had to use it, good for getting time stamps
    '''
    mstosec = randTime // 1000
    minutes = mstosec // 60
    secs = mstosec % 60
    int(minutes)
    int(secs)

    print("minutes="+str(minutes))
    print("seconds="+str(secs))

    if minutes > 9 and secs > 9:
        screenCap = str(minutes) +":" + str(secs)
    elif minutes > 9 and secs < 10:
        screenCap = str(minutes) +":0" + str(secs)
    elif minutes < 10 and secs > 9:
        screenCap = "0" +str(minutes) +":" + str(secs)
    else:
        screenCap = "0" +str(minutes) +":0" + str(secs)

    print(screenCap)
    text = "shrek (2001). " +screenCap+"."
	

    
    text = "shrek (2001). frame "+ str(count) +" of blank"
    #endtextformat

    filepath = screenCapFileName

    tweet(text, filepath)

    '''

def get_length(filename):
    return VideoFileClip(filename).duration

def tweet(text, filepath):
    api.update_with_media(filepath, text)


if __name__ == '__main__':
    finalScript()