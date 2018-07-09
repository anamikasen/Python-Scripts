import re
import json

with open('outputlog.log', 'r') as log_file:
    log_string = log_file.readlines()
    count = 0
    seqs = []
    predictions = []
    groupedSeq = []

    for line in log_string:
        count+=1
        if count%6!=0:
            seqs.append(line.strip())
        else:
            predictions.append(line)

    groupedSeq = [seqs[i:i + 5] for i in range(0, len(seqs), 5)]

    for foo in zip(groupedSeq, predictions):
        print(foo[0])

    # for line in log_string:
    #     print(line)