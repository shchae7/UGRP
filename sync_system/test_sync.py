import os
import time

count = 0

while True:
    time.sleep(30)

    file = open("./computer/upload/rsync_test_" + str(count) + ".txt", "w")
    file.write("User inputted text")
    file.close()

    count = count + 1
