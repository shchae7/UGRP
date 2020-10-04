import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

import datetime

USERID = 'shchae7'
SOURCE = '/home/' + USERID + '/UGRP/sync_system/server/user_text'
SOURCE_LENGTH = len(SOURCE) + 2  # 1 when testing using mv command
DEST = '/home/' + USERID + '/UGRP/sync_system/server/user_voice/'
FILE_NUM = 0 # Keep track of number of files in user_text dir --> for string indexing


TACOTRON_HOME = '/home/' + USERID + '/UGRP/tts/Tacotron2-Wavenet-Korean-TTS/'

class Watcher:
    def __init__(self):
        self.observer = Observer()
    def run(self):
        print('User text dir Watcher started running!')
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
            print("New file %s uploaded to SOURCE from COMPUTER!!!" % event.src_path)
            source = event.src_path[SOURCE_LENGTH:74]

            src = open('./user_text/' + source, "r")
            line = src.readline().rstrip()
            src.close()

            currentDT = datetime.datetime.now()
            formatted_time = currentDT.strftime('%Y-%m-%d_%H-%M-%S')

            sh = open(TACOTRON_HOME + 'inference_' + formatted_time + '.sh', 'w')
            sh.write("#!/bin/sh\n\n")

            sh.write("#SBATCH -J KTacoSyn\n")
            sh.write("#SBATCH -o out/KTacoSyn.%j.out\n")
            sh.write("#SBATCH -p gpu-2080ti-8\n")
            sh.write("#SBATCH -t 2:00:00\n")
            sh.write("#SBATCH --gres=gpu:2\n\n")

            sh.write('echo "Start Syntehsizing Wav File"\n')
            sh.write('echo "SLURM_SUBMIT_DIR = $SLURM_SUBMIT_DIR"\n')
            sh.write('echo "CUDA_HOME = $CUDA_HOME"\n')
            sh.write('echo "CUDA_VISIBLE_DEVICES = $CUDA_VISIBLE_DEVICES"\n')
            sh.write('echo "CUDA_VERSION=$CUDA_VERSION"\n\n')

            sh.write('srun -l /bin/hostname\n')
            sh.write('srun -l /bin/pwd\n')
            sh.write('srun -l /bin/date\n\n')

            sh.write('conda init bash\n')
            sh.write('activate tf1-gpu-py36\n\n')

            sh.write('python3 synthesizer.py --load_path logs_tacotron2/son_2020-08-20_01-22-11 --num_speakers 1 --speaker_id 0 --text ' + '"' + line + '"\n\n')

            sh.write('date\n\n')

            sh.write('conda deactivate\n\n')

            sh.write("squeue --job $SLURM_JOBID\n")
            sh.write('echo "##    END    ##"')
            sh.close()

            print(TACOTRON_HOME + 'inference_' + formatted_time + '.sh written')

            os.system('sbatch ' + TACOTRON_HOME + 'inference_' + formatted_time + '.sh')


if __name__ == '__main__':
    w = Watcher()
    w.run()
