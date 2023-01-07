from moviepy.editor import *
import os

def videoName(i):
    ret = str(i)
    while (len(ret) < 4):
        ret = '0' + ret
    return "SR-NL-C-" + ret

clip_num = 163    # stores file name counter, manually change if program is restarted
files = os.listdir('Self_Record_Precut')

for i in range(len(files)):
    f = os.path.join('Self_Record_Precut', files[i])
    if (os.path.isfile(f) and (os.path.splitext(f)[1] == '.mp4')): # if f is an mp4 file
        print("working on " + str(f))
        clip = VideoFileClip(f)
        while True:
            cmd = input("enter command: ")

            if (cmd.lower() == 'q'):
                clip.close() 
                break

            elif (cmd.lower() == 'cp'):
                min = int(input())
                sec = float(input())
                clip = clip.subclip(t_start=(min,sec))
                print('cut previous with t = ' + str(min) + ':' + str(sec))

            elif (cmd.lower() == 'ca'):
                min = int(input())
                sec = float(input())
                clip = clip.subclip(t_end=(min,sec))
                print('cut after with t = ' + str(min) + ':' + str(sec))

            elif (cmd.lower() == 'gc'):
                min1 = int(input())
                sec1 = float(input())
                length = float(input())
                sec2 = sec1 + length
                min2 = min1
                if sec2 > 60.0:
                    min2 += 1
                    sec2 -= 60.0

                clip = clip.subclip(t_start=(min1,sec1), t_end=(min2,sec2))
                clip.write_videofile(".\\Web_Scrape_Cut\\" + videoName(clip_num) + ".mp4", audio=False)
                clip_num += 1

            elif (cmd.lower() == 'b'):
                clip = VideoFileClip(f)
                
            else:
                print('invalid command, try again')


