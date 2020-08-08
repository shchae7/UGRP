import os
import time

print('test_sync started!')

count = 0

while True:
    time.sleep(15)

    file = open("./computer/upload/rsync_test_" + str(count) + ".txt", "w")
    file.write("User inputted text from APP!")
    file.close()

    print('rsync_test_' + str(count) + ' written to upload dir')

    count = count + 1
