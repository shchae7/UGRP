import os
import shutil

# moving wav files
wsrc = './wav_source'
wdest = './datasets/choi/audio'

uw = os.listdir(wsrc)

for w in uw:
    shutil.move(os.path.join(wsrc, w), wdest)


# writing sync
tsrc = './user_text/'
tdest = './datasets/choi-recognition-All.txt'
for root, subdirs, files in os.walk(tsrc):
    for file in files:
        ut = open(tsrc + file, 'r')
        print(tsrc+file)
        texts =  ut.readlines()
        dt = open(tdest, 'a')
        dt.write('\n'.join(texts))
        dt.close()

