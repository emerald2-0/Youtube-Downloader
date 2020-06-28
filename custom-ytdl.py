import os, sys, time
from pytube import YouTube

#Accept user input
user_link = input("Enter the video's link: ")
#Pass the link to the youtube class?
yt = YouTube(user_link)

#Information on the video:
print("Video title is: ", yt.title)

#Number of views from the video
print("Video has ", yt.views, " views" )

#Video description:- Hii imekuwa refu kwa videos kadhaa...eating memory
#print("Video is described as: ", yt.description)

#Video Rating:
print("Video is rated: ", yt.rating)

print("Available Streams are....")

print("/")
print("\b \b \b")

time.sleep(2)
#Print the streams
stream_list = yt.streams 

for strm in stream_list:
	print(str(strm) + " \n")

time.sleep(0.5)

print("Audio streams: ..")

#Filter audio streams
audio_streams = stream_list.filter(only_audio=True)

for audi_strm in audio_streams:
	print(str(audi_strm) + " \n")


time.sleep(1)
print("Video Streams:..")
time.sleep(0.5)

#Filter Video streams
vid_streams = stream_list.filter(only_video=True)

for vid_strm in vid_streams:
	print(str(vid_strm) + " \n")

#Progressive streams filter - vs Dash streams: - Youtube content kwa documentation
print("Progressive streams filter:...")
Progressive_streams = stream_list.filter(progressive = True)

for prgrsv in Progressive_streams:
	print( str(prgrsv) + " \n")


time.sleep(0.5)
print("Getting Lowest resolution....")
#Get lowest resolution: --MBs hukuwa issue:)
ys = stream_list.get_lowest_resolution()
time.sleep(0.5)
print("Lowest resolution attained...")

video_size = ys.filesize/1000000

print(str(video_size) + "mbs is filesize")

time.sleep(4)

print("...Downloading video(s)")
ys.download()
print("...Completed Downloading")

#Irax marker @ Emerald