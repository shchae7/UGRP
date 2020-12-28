import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os

SOURCE = '/home/shchae7/UGRP/sync_system/server/user_text'
SOURCE_LENGTH = len(SOURCE) + 2
DEST = '/home/shchae7/UGRP/sync_system/server/user_voice/'

FILE_NUM = 0 # Keep track of number of files in user_text dir --> for string indexing

class Watcher:
    def __init__(self):
        self.observer = Observer()

    def run(self):
        print('User text dir Watcher started running!')
        event_handler = Handler()
        self.observer.schedule(event_handler, SOURCE, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped!")

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.event_type == 'created':
            print("New file %s uploaded to SOURCE from COMPUTER!!!" % event.src_path)
            if len(os.listdir(SOURCE)) <= 10:  # rsync_test starts from 0
                print(event.src_path[SOURCE_LENGTH:65])
                os.system('python3 test_inference.py ' + event.src_path[SOURCE_LENGTH:65] + ' ' + DEST)
            else:
                print(event.src_path[SOURCE_LENGTH:66])
                os.system('python3 test_inference.py ' + event.src_path[SOURCE_LENGTH:66] + ' ' + DEST)
 

if __name__ == '__main__':
    w = Watcher()
    w.run()
