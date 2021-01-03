import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os

USERID = 'shchae7'

SOURCE = os.getcwd() + '/data'

class Watcher:
    def __init__(self):
        self.observer = Observer()

    def run(self):
        print('Augmentation upload dir Watcher started running!')
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
            dr = event.src_path
            print("New file %s uploaded to SOURCE from APP!!!" % dr)
            os.system('python3 augmentation.py ' + dr + ' ' + dr[len(SOURCE)+1])


if __name__ == '__main__':
    w = Watcher()
    w.run()
