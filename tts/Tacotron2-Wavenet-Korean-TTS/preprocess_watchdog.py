import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import AudioAugmentation
import threading

import os
#python preprocess.py --num_workers 10 --name son 
# --in_dir D:\hccho\multi-speaker-tacotron-tensorflow-master\datasets\son --out_dir .\data\son
SOURCE = './datasets'
SOURCE_LENGTH = len(SOURCE) + 2
DEST = './data'
#TODO : Test this

FILE_NUM = 0 # Keep track of number of files in user_text dir --> for string indexing

class Watcher:
    def __init__(self):
        self.observer = Observer()

    def run(self):
        print('Augmentation dir Watcher started running!')
        event_handler = Handler()
        self.observer.schedule(event_handler, SOURCE, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Augmentation Dir Stopped!")

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.event_type == 'created':
            print("New file %s uploaded to augmentation data(input)." % event.src_path)
            if len(os.listdir(SOURCE)) <= 10:  # rsync_test starts from 0
                fname = event.src_path[SOURCE_LENGTH:65]
            else:
                fname = event.src_path[SOURCE_LENGTH:66]
        thread = Threading.Thread(target = AudioAugmentation.run_augmentation, args = (fname,))
        thread.start()
 

if __name__ == '__main__':
    w = Watcher()
    w.run()