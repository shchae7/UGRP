import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os

SOURCE = os.getcwd() + '/feedback'

class Watcher:
    def __init__(self):
        self.observer = Observer()

    def run(self):
        print('server feedback dir watcher running')
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
            print("New feedback file %s uploaded to feedback/server/feedback from COMPUTER!!!" % event.src_path)
            #print(event.src_path[len(SOURCE) + 2 : len(SOURCE) + 10])
            os.system('python3 check_feedback.py ' + event.src_path[len(SOURCE) + 2 : len(SOURCE) + 10] + ' ' + str(len(os.listdir('./sat_feedback'))+1))


if __name__ == '__main__':
    w = Watcher()
    w.run()

