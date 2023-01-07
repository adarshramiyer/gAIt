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

    res = 'SR-' + overstride + '-' + forward + '-' + backward + '-' + sweep + '-' + low_arm + '-' + side + '-' + res
    return res

files = os.listdir('Self_Record_Cut')

already_labeled = 47

for i in range(len(files)):

    if (i < already_labeled):
        continue
    
    f = os.path.join('Self_Record_Cut', files[i])
    if (os.path.isfile(f) and (os.path.splitext(f)[1] == '.mp4')): # if f is an mp4 file
        print("working on " + str(f))

        overstride = int(input('overstride (0-9): '))
        if (overstride < 0): # enter a negative number if the training example is not good
            continue
        forward = int(input('forward lean (0-9): '))
        backward = int(input('backward lean (0-9): '))
        sweep = int(input('sweep (0-9): '))
        low_arm = int(input('low_arm (0-9): '))      
        side = input('entry side (L/R): ')
        
        new_name = videoName(i, overstride, forward, backward, sweep, low_arm, side)

        shutil.copy2(f, '.\\Self_Record_Labeled\\' + new_name + ".mp4")
        
