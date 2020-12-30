import os
import shutil

# moving wav files
USERID = 'shchae7'
SAT_FEEDBACK = '/home/' + USERID + '/UGRP/feedback_system/server/sat_feedback/'
WAV_SOURCE = '/home/' + USERID + '/UGRP/sync_system/server/user_voice/'
WAV_DEST = '/home/' + USERID + '/UGRP/tts/Tacotron2-Wavenet-Korean-TTS/datasets/son/audio/'

for filename in os.listdir(SAT_FEEDBACK):
    print(filename)
    shutil.copy(WAV_SOURCE + filename[:-4] + '.wav', WAV_DEST)
    os.remove(SAT_FEEDBACK + filename)

# writing to dataset
#TXT_SOURCE = '/home/' + USERID + '/UGRP/sync_system/server/user_text/'
