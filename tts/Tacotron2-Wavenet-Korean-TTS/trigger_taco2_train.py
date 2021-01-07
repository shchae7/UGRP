import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

DATA = './data/user'
TRAIN_TXT = DATA + '/train.txt'

SCRIPT_DIR = '../server'
SCRIPT_TXT_ALL = '/script_all.txt'
SCRIPT_TXT_LINE = SCRIPT_DIR + '/script_line'
DEST = './downloaded_script'

with open(TRAIN_TXT, 'r') as train_txt:
    fileline = len(train_txt.readlines())
    print('How many lines in train.txt?: ' + str(fileline))

class Watcher:
    def __init__(self):
     	self.observer = Observer()

    def run(self):
        print('preprocessed DATA watcher running!')
        try:
            while True:
                list_data = len(os.listdir(DATA)) -1
                print(str(list_data))
                if list_data >= fileline:
                    print("ready to train")
                    #os.system('rsync -avz --rsh=\'ssh -p 7777\' ' + SCRIPT_TXT_LINE + '/* ' + DEST)
                    os.system ('sbatch taco_train.sh \'-u user\'')
                    break
                else:
                    time.sleep(5)
        except:
            self.observer.stop()
            print("observer stopped")

if __name__ == '__main__':
    w = Watcher()
    w.run()