import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os

SOURCE = '/Users/seunghyunchae/UGRP/sync_system/computer/upload'
DEST = 'shchae7@141.223.181.14:/home/shchae7/UGRP/sync_system/server/user_text' 

class Watcher:
    def __init__(self):
        self.observer = Observer()

    def run(self):
        print('CS upload dir Watcher started running!')
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
            print("New file %s uploaded to SOURCE from APP!!!" % event.src_path)
            os.system('rsync -avz --rsh=\'ssh -p 7777\' --password-file=rsync_pass ' + SOURCE + '/* ' + DEST)


if __name__ == '__main__':
    w = Watcher()
    w.run()	
