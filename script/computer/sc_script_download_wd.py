import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

USERID = 'shchae7'

SCRIPT_DIR = USERID + '@cse-cluster1.postech.ac.kr:/home/' + USERID + '/UGRP/script/server'
SCRIPT_TXT_ALL = SCRIPT_DIR + '/script_all.txt'
SCRIPT_TXT_LINE = SCRIPT_DIR + '/script_line'
DEST = './downloaded_script'

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
                print("GOGO:", fileline)
            while True:
                os.system('rsync -chavzP -e \'ssh -p 7777\' \'--exclude="script_0000000.txt"\' '+ SCRIPT_TXT_LINE + '/* ' + DEST)
                break
        except:
            self.observer.stop()
            print("observer stopped")

    def run2(self):
        print('Wait for creation of endfile')
        event_handler = Handler()
        self.observer.schedule(event_handler, SCRIPT_TXT_LINE, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped!")

        self.observer.join()

    def run3(self):
        while True:
            time.sleep(45)
            os.system('rsync -chavzP -e \'ssh -p 7777\' ' + SCRIPT_TXT_LINE + '/end_of_training.txt ' + DEST)
            break


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.event_type == 'created':
            print("New file %s uploaded to SOURCE from APP!!!" % event.src_path)
            os.system('rsync -chavzP -e \'ssh -p 7777\' ' + SCRIPT_TXT_LINE + '/end_of_training.txt ' + DEST)

if __name__ == '__main__':
    w = Watcher()
    w.run()
    w.run3()

