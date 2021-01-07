import os
import shutil

UGRP_PATH = os.getcwd()[:-23]
SYNC_SYS_PATH = UGRP_PATH + '/sync_system/server/'
AUG_SYS_PATH = UGRP_PATH + '/augmentation_system/'

SAT_FEEDBACK = os.getcwd() + '/sat_feedback/'
WAV_SOURCE = SYNC_SYS_PATH + 'user_voice/'
WAV_DEST = AUG_SYS_PATH + 'data/'
FB_DEST = AUG_SYS_PATH + 'feedback/'
TXT_SOURCE = SYNC_SYS_PATH + 'user_text/'

for filename in os.listdir(SAT_FEEDBACK):
    #print(filename)
    shutil.copy(WAV_SOURCE + filename[:-4] + '.wav', WAV_DEST)
    shutil.copy(TXT_SOURCE + filename[:-4] + '.txt', FB_DEST)

    # remove dealt w sat fbs
    os.remove(SAT_FEEDBACK + filename)