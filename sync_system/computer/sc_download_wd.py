import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os

USERID = 'shchae7'

HOME_DIR = os.getcwd()
WATCH_DIR = HOME_DIR + '/upload'
SOURCE = USERID + '@cse-cluster1.postech.ac.kr:/home/' + USERID + '/UGRP/sync_system/server/user_voice/'
DEST = HOME_DIR + '/download'

class Watcher:
    def __init__(self):
        self.observer = Observer()

    def run(self):
        print('CS upload dir Watcher for Download started running!')
        event_handler = Handler()
        self.observer.schedule(event_handler, WATCH_DIR, recursive=True)
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
            print("New file %s uploaded to SOURCE from APP wait for DOWNLOAD!!!" % event.src_path)

            txt_file_size = os.stat(event.src_path).st_size

            if txt_file_size < 50:
                print('txt file size < 50')
                time.sleep(100)
            elif txt_file_size < 100:
                print('txt file size < 100')
                time.sleep(100)
            elif txt_file_size < 150:
                print('txt file size < 150')
                time.sleep(100)
            else:
                print('txt file size > 150')
                time.sleep(100)

            print('slept')
            os.system('rsync -chavzP -e "ssh -p 7777" ' + SOURCE + '/* ' + DEST)


if __name__ == '__main__':
    w = Watcher()
    w.run()
