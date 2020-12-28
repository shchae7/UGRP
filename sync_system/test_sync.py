import os
import time

print('test_sync started!')

count = 0

while True:
    time.sleep(15)

    file = open("./computer/upload/rsync_test_" + str(count) + ".txt", "w")
    file.write("안녕하세요 채승현입니다")
    file.close()

    print('rsync_test_' + str(count) + ' written to upload dir')

    count = count + 1
