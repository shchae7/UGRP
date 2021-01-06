import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os

USERPATH = 'parksbn812/2020ugrp/all-team/feature-script'
USERID = 'parksbn812'

SCRIPT_DIR = USERID + '@141.223.181.103:/home/' + USERPATH + '/UGRP/script/server'
# SCRIPT_DIR = '../server'
SCRIPT_TXT_ALL = SCRIPT_DIR + '/script_all.txt'
SCRIPT_TXT_LINE = SCRIPT_DIR + '/script_line'
DEST = './downloaded_script'

#with open(SCRIPT_TXT_ALL, 'r') as script_all:
#    fileline = len(script_all.readlines())
fileline = 0

class Watcher:
    def __init__(self):
     	self.observer = Observer()

    def run(self):
        print('sc_script_txt watcher running!')
        try:
            os.system('rsync -chavzP -e \'ssh -p 7777\' ' + SCRIPT_TXT_LINE + '/script_0000000.txt ' + '.')
            with open('./script_0000000.txt', 'r') as f_line:
                fileline_str = f_line.readline()
                fileline = int(fileline_str)
            while True:
                #print(len(os.listdir(SCRIPT_TXT_LINE)))
                if len(os.listdir(SCRIPT_TXT_LINE)) >= fileline:
                    print("all txt splited")
                    os.system('rsync -chavzP -e \'ssh -p 7777\' --exclude="script_0000000.txt" '+ SCRIPT_TXT_LINE + '/* ' + DEST)
                    break
                else:
                    time.sleep(5)
        except:
            self.observer.stop()
            print("observer stopped")

if __name__ == '__main__':
    w = Watcher()
    w.run()
