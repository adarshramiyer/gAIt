from moviepy.editor import *
import os

def videoName(i):
    ret = str(i)
    while (len(ret) < 4):
        ret = '0' + ret
    return ret

clip_num = 0    # stores file name counter
files = os.listdir('Web_Scrape_Precut')

for i in range(len(files)):
    f = os.path.join('Web_Scrape_Precut', files[i])
    if (os.path.isfile(f) and (os.path.splitext(f)[1] == '.mp4')): # if f is an mp4 file
        print("working on " + str(f))


