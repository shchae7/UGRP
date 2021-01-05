import os
import json

# mapping wav names and text lines & writing user-recognition-All.json


######## SERVER PATHS ########

# USERID = 'parksbn812'

# SOURCE_DIR = '/home/' + USERID + '/2020ugrp/all-team/feature-script/UGRP/script/server'
# TXT_SOURCE = SOURCE_DIR + '/script_all.txt'

# DEST_DIR   =  '/home/' + USERID + '/2020ugrp/all-team/feature-script/UGRP/tts/Tacotron2-Wavenet-Korean-TTS/datasets/user/
# JSON_DEST = DEST_DIR + 'user-recognition-All.json'

# WAV_HEAD = './datasets/user/audio/script_'
# WAV_TAIL = '.wav'


######## TEST PATHS ########

TXT_SOURCE = 'script_all.txt'
JSON_DEST = '../../tts/Tacotron2-Wavenet-Korean-TTS/datasets/user/user-recognition-All.json'

WAV_HEAD = './datasets/user/audio/script_'
WAV_TAIL = '.wav'

data = {}

linenum = 0

with open(TXT_SOURCE, 'r', encoding = 'utf8') as ScriptAll:
    for line in ScriptAll.readlines():
        x = line
        print(x)
        WAV_TAG = "%07d" % (linenum)
        data.setdefault(WAV_HEAD + WAV_TAG + WAV_TAIL, x.rstrip('\n'))
        linenum = linenum + 1
    ScriptAll.close()
  
with open(JSON_DEST, 'w', encoding = 'utf8') as RecogAllJson:
    json.dump(data, RecogAllJson, ensure_ascii=False)
RecogAllJson.close()

