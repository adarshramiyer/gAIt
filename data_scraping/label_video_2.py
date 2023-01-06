import os
import shutil

def videoName(i, overstride_score, forward_score, backward_score, sweep_score, low_arm_score, side):
    res = str(i)
    while len(res) < 4:
        res = '0' + res
    overstride = 'O' + str(overstride_score)
    forward = 'F' + str(forward_score)
    backward = 'B' + str(backward_score)
    sweep = 'S' + str(sweep_score)
    low_arm = 'L' + str(low_arm_score)

    res = 'WS-' + overstride + '-' + forward + '-' + backward + '-' + sweep + '-' + low_arm + '-' + side + '-' + res
    return res

files = os.listdir('Web_Scrape_Labeled')

already_labeled = 0

for i in range(len(files)):

    if (i < already_labeled):
        continue
    
    f = os.path.join('Web_Scrape_Labeled', files[i])
    if (os.path.isfile(f) and (os.path.splitext(f)[1] == '.mp4')): # if f is an mp4 file
        print("working on " + str(files[i][20:]))

        prev_o = int(files[i][4])
        prev_f = int(files[i][7])
        prev_b = int(files[i][10])
        prev_s = int(files[i][13])
        prev_l = int(files[i][16])
        prev_s = files[i][18]

        overstride = int(input('overstride (0-9): '))
        if (overstride < 0): # enter a negative number if the training example is not good
            continue
        forward = int(input('forward lean (0-9): '))
        backward = int(input('backward lean (0-9): '))
        sweep = int(input('sweep (0-9): '))
        low_arm = int(input('low_arm (0-9): '))      
        side = input('entry side (L/R): ')

        if abs(overstride - prev_o) > 2:
            overstride = int(input('you previously rated overstride as ' + str(prev_o) + ' and now rate it ' + str(overstride) + '. Enter your final choice:'))
        else:
            overstride = int((overstride + prev_o + 1) / 2)
        
        if abs(forward - prev_f) > 2:
            forward = int(input('you previously rated forward lean as ' + str(prev_f) + ' and now rate it ' + str(forward) + '. Enter your final choice:'))
        else:
            forward = int((forward + prev_f + 1) / 2)

        if abs(backward - prev_b) > 2:
            backward = int(input('you previously rated backward lean as ' + str(prev_b) + ' and now rate it ' + str(backward) + '. Enter your final choice:'))
        else:
            backward = int((backward + prev_b + 1) / 2)

        if abs(sweep - prev_s) > 2:
            sweep = int(input('you previously rated sweeping as ' + str(prev_s) + ' and now rate it ' + str(sweep) + '. Enter your final choice:'))
        else:
            sweep = int((sweep + prev_s + 1) / 2)

        if abs(low_arm - prev_l) > 2:
            low_arm = int(input('you previously rated low arms as ' + str(prev_l) + ' and now rate it ' + str(low_arm) + '. Enter your final choice:'))
        else:
            low_arm = int((low_arm + prev_l + 1) / 2)

        if (side != prev_s):
            side = input('Entry side entered (' + str(side) + ') differs from previous side. Enter your final choice:')
        
        
        new_name = videoName(i, overstride, forward, backward, sweep, low_arm, side)

        shutil.copy2(f, '.\\Web_Scrape_Labeled_2\\' + new_name + ".mp4")