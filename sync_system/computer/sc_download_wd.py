import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os

WATCH_DIR = '/Users/seunghyunchae/UGRP/sync_system/computer/upload'
SOURCE = 'shchae7@141.223.181.14:/home/shchae7/UGRP/sync_system/server/user_voice'
DEST = '/Users/seunghyunchae/UGRP/sync_system/computer/download'

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
                time.sleep(3)
            elif txt_file_size < 100:
                print('txt file size < 100')
                time.sleep(6)
            elif txt_file_size < 150:
                print('txt file size < 150')
                time.sleep(9)
            else:
                print('txt file size > 150')
                time.sleep(12)

            print('slept')
            os.system('rsync -chavzP -e "ssh -p 7777" ' + SOURCE + '/* ' + DEST)


if __name__ == '__main__':
    w = Watcher()
    w.run()
