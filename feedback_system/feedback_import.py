import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os

SOURCE = 'feedback/'

class Watcher:
    def __init__(self):
        self.observer = Observer()

    def run(self):
        print('feedback dir Watcher started running!')
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
            print("New feedback file %s uploaded to SOURCE from COMPUTER!!!" % event.src_path)
            os.system('python3 score_count.py ' + event.src_path + ' ' + str(len(os.listdir('./score'))+1))
            print(event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()

