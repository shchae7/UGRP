import os
from watchdog.observers import Observer
import time
import json

# USERID = parksbn812
# SOURCE = '/home/' + USERID + '/UGRP/tts/Tacotron2-Wavenet-Korean-TTS/datasets/user/audio/'

AUDIO_SOURCE = 'datasets/user/audio/'
JSON_SOURCE = 'datasets/user/user-recognition-All.json'

# getting the # of wav file(line)s from 'user-recognition-All.json
with open(JSON_SOURCE, 'r') as JSON:
    json_data = json.load(JSON)
    linenum = len(json_data)
    print('How many lines in .json?: ' + str(linenum))

# monitoring 'audio'
class Watcher:
    def __init__(self):
        self.observer = Observer()
    def run(self):
        print('audio dir watcher running!')
        print('How many audio files are ready?')
        try:
            while True:
                print(str(len(os.listdir(AUDIO_SOURCE))) + '/' + str(linenum))
                if len(os.listdir(AUDIO_SOURCE)) >= linenum:
                    print('All audio files are ready! Now start preprocessing.')
		# trigger preprocessing!
                    os.system('python preprocess.py --num_workers 8 --name user --in_dir ./datasets/user --out_dir ./data/user')
                    break
                else:
                    time.sleep(1)
        except:
            self.observer.stop()
            print('observer stopped')

if __name__ == '__main__':
    w = Watcher()
    w.run()


