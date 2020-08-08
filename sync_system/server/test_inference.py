import sys
import os

DIR = '/home/shchae7/UGRP/sync_system/server/user_voice'

file = open('./user_text/' + sys.argv[1], "r")
new_file = open(sys.argv[2] + "inference_test_" + str(len(os.listdir(DIR))) + ".txt", "w+")

for line in file.readlines():
    new_file.write(line)

new_file.write("\nInference Done")

file.close()
new_file.close()
