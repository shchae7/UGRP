import os

# split whole script in each line
USERPATH = 'parksbn812/2020ugrp/all-team/feature-script'
SCRIPT_SOURCE = '/home/' + USERPATH + '/UGRP/script/server'
SCRIPT_TXT_ALL = SCRIPT_SOURCE + '/script_all.txt'
SCRIPT_TXT_LINE_DEST = SCRIPT_SOURCE + '/script_line'

filenum = 0
with open(SCRIPT_TXT_ALL, 'r') as f_script_all:
    for line in f_script_all.readlines():
        x = line
        # print(x)
        filenum = filenum + 1
        str_filenum = "%07d" % (filenum)
        with open(SCRIPT_TXT_LINE_DEST + '/script_'+ str_filenum+'.txt', 'w') as f_script_line:
            f_script_line.write(x)
            # print(x)


