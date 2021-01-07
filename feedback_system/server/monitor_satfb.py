import os
from watchdog.observers import Observer
import time

SOURCE = os.getcwd() + '/sat_feedback'

class Watcher:
    def __init__(self):
     	self.observer = Observer()

    def run(self):
        print('sat_feedback dir watcher running!')
        try:
            while True:
                print(SOURCE)
                print(len(os.listdir(SOURCE)))
                if len(os.listdir(SOURCE)) >= 5:
                    print("enough satisfactory feedbacks accumulated")
                    os.system('python3 add_to_dataset.py')
                else:
                    time.sleep(5)
        except:
            self.observer.stop()       
            print("observer stopped")

if __name__ == '__main__':
    w = Watcher()
    w.run()
