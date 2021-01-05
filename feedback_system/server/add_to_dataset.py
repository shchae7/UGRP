import os
import shutil

UGRP_PATH = os.getcwd()[:-23]

# moving wav files
SAT_FEEDBACK = os.getcwd() + '/sat_feedback/'
WAV_SOURCE = UGRP_PATH + '/sync_system/server/user_voice/'
WAV_DEST = UGRP_PATH + '/augmentation_system/data/'
FB_DEST = UGRP_PATH + '/augmentation_system/feedback/'

# writing to dataset
TXT_SOURCE = UGRP_PATH + '/sync_system/server/user_text/'
TXT_DEST = UGRP_PATH + '/tts/Tacotron2-Wavenet-Korean-TTS/datasets/son/son-recognition-All.json'

for filename in os.listdir(SAT_FEEDBACK):
    #print(filename)
    shutil.copy(WAV_SOURCE + filename[:-4] + '.wav', WAV_DEST)
    shutil.copy(TXT_SOURCE + filename[:-4] + '.txt', FB_DEST)

    # remove dealt w sat fbs
    os.remove(SAT_FEEDBACK + filename)