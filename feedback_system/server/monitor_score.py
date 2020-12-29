import os
from watchdog.observers import Observer
import time

src = './score/'


class Watcher:
    def __init__(self):
     	self.observer = Observer()

    def run(self):
        print('Score dir Watcher started running!')
        try:
            while True:
                if len(os.listdir(src)) >= 5:
                    print("now we can add those data")
                    os.system('python3 need_dataset.py')
                    break
                else:
                    time.sleep(5)
        except:
            self.observer.stop()       
            print("observer stopped")

if __name__ == '__main__':
    w = Watcher()
    w.run()
