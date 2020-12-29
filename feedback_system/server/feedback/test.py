# make copies of a successful feedback file!

import shutil
import os
import time

count = 1
src = 'feedback_example.txt'
#dest = 'feedback_copy_' + str(count) + '.txt'

print("reproducting.....")

while True:
    shutil.copy2(src, 'feedback_copy_' + str(format(count, '02')) + '.txt')
    count += 1
    time.sleep(5)
