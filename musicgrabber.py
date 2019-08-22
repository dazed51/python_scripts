#!/usr/bin/python

#script will ask for input and loop through the input, then append to a file where youtube-dl will be used to download the music"

#using some system specifc modules
import os
import sys
import time

#open song file
song_file = open('/mnt/data/ent/musiclist.txt', 'w')

#enter song  input
song_list = []

print("enter up to 5 songs")
time.sleep(3)

#enter up to 5 songs
for i in range (1, 6):
    print("enter song by copying url from youtube: ")
    line = input()
    song_list.append(line + "\n")

song_file.writelines(song_list)
song_file.close()

#check file for songs
'''
TODO:
if song has 5 songs, then yes songs are there
else, no songs in file see what wrong
'''
#TODO: call youtube-dl to extract audio
time.sleep(2)
print("extracting mp3 from list of youtube lists using youtube-dl")
os
    