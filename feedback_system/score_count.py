import sys
import os

DIR = 'score/'

with open(sys.argv[1], "r") as file:
    scores = []
    for line in file:
        scores.append(int(line))

print(scores)
total_score = sum(scores)

if total_score >= 45:
    print(total_score, "this is successful case")
    new_file = open(DIR + 'feedback_success_' + str(sys.argv[2]) + '.txt', 'w')
    new_file.write(str(total_score))
    new_file.close()

