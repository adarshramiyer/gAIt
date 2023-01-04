import os
import shutil

def videoName(i, overstride_score, forward_score, backward_score, sweep_score, low_arm_score, side):
    res = str(i)
    while len(i) < 4:
        res = '0' + i
    overstride = 'O' + str(overstride_score)
    forward = 'F' + str(forward_score)
    backward = 'B' + str(backward_score)
    sweep = 'S' + str(sweep_score)
    low_arm = 'L' + str(low_arm_score)

    res = 'WS-' + overstride + '-' + forward + '-' + backward + '-' + sweep + '-' + low_arm + '-' + side + '-' + res
    return res

files = os.listdir('Web_Scrape_Cut')

for i in range(len(files)):
    f = os.path.join('Web_Scrape_Cut', files[i])
    if (os.path.isfile(f) and (os.path.splitext(f)[1] == '.mp4')): # if f is an mp4 file
        print("working on " + str(f))

        overstride = int(input('overstride (0-9): '))
        forward = int(input('forward lean (0-9): '))
        backward = int(input('backward lean (0-9): '))
        sweep = int(input('sweep (0-9): '))
        low_arm = int(input('low_arm (0-9): '))      
        side = input('entry side (L/R): ')
        
        new_name = videoName(i, overstride, forward, backward, sweep, low_arm, side)

        shutil.copy2(f, '.\\Web_Scrape_Labeled\\' + new_name + ".mp4")
        
