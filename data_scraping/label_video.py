import os

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