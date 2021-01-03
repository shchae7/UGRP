import os
import shutil

# moving wav files
USERID = 'shchae7'
SAT_FEEDBACK = '/home/' + USERID + '/UGRP/feedback_system/server/sat_feedback/'
WAV_SOURCE = '/home/' + USERID + '/UGRP/sync_system/server/user_voice/'
#WAV_DEST = '/home/' + USERID + '/UGRP/tts/Tacotron2-Wavenet-Korean-TTS/datasets/son/audio/'
WAV_DEST = '/home/' + USERID + '/augmentation_system/data/'
FB_DEST = 'home/' + USERID + '/augmentation_system/feedback/'
REL_WAV_DEST = './datasets/son/audio/'

# writing to dataset
TXT_SOURCE = '/home/' + USERID + '/UGRP/sync_system/server/user_text/'
TXT_DEST = '/home/' + USERID + '/UGRP/tts/Tacotron2-Wavenet-Korean-TTS/datasets/son/son-recognition-All.json'

for filename in os.listdir(SAT_FEEDBACK):
    #print(filename)
    shutil.copy(WAV_SOURCE + filename[:-4] + '.wav', WAV_DEST)
    shutil.copy(TXT_SOURCE + filenmae[:-4] + '.txt', FB_DEST)

    # user_txt_file = open(TXT_SOURCE + filename, "r")
    # user_text = user_txt_file.readlines()
    # #print(user_text)

    # ori_recog_file = open(TXT_DEST, "r")
    # ori_lines = ori_recog_file.readlines()
    # ori_recog_file.close()
    # #print(ori_lines)

    # del_line_recog_file = open(TXT_DEST, "w")
    # count = 0
    # for line in ori_lines:
    #     if count == len(ori_lines) - 2:
    #         del_line_recog_file.write(line.strip('\n') + ',\n')
    #     else:
    #         if line.strip('\n') != '}':
    #             del_line_recog_file.write(line)
    #     count = count + 1
    # del_line_recog_file.close()

    # recog_file = open(TXT_DEST, "a")
    # for line in user_text:
    #     recog_file.write('    ' + '\"' + REL_WAV_DEST + filename[:-4] + '.wav\": ' + '\"' + line + '\"\n')
    # recog_file.write("}")
    # recog_file.close()

    os.remove(SAT_FEEDBACK + filename)