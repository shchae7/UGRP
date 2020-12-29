import sys
import os

SOURCE_DIR = os.getcwd() + '/feedback/'
TARGET_DIR = os.getcwd() + '/sat_feedback/'

with open(SOURCE_DIR + sys.argv[1], "r") as file:
    scores = []
    for line in file:
        scores.append(int(line))

#print(scores)
total_score = sum(scores)


# satisfactory wav feedback format
#1. total scores
#2. name of wav/feedback file corresponding to total score


if total_score >= 9:
    #print(total_score, "this is successful case")
    new_file = open(TARGET_DIR + sys.argv[1][:-4] + str(sys.argv[2]) + '.txt', 'w')
    new_file.write(str(total_score))
    new_file.write(sys.argv[1])
    new_file.close()