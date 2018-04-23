import audio
import soundwave
import sys
import math
import random

minuets = open("mTable.txt", "r").readlines()
for index in range(len(minuets)):
    minuets[index] = " ".join(str(minuets[index]))

trios = open("tTable.txt", "r").readlines()
for index in range(len(trios)):
    trios[index] = " ".join(str(trios[index]))


snippetList = []


def minuetSequence():
    for i in range(16):
        rand = random.randint(0, 10)
        snippetList.append(minuets[i][rand])

def trioSequence():
    for j in range(17, 32):
        rand = random.randint(0, 5)
        snippetList.append(trios[j][rand])



mintrio = soundwave.Soundwave("M"+snippetList[0]+".wav")
for x in range(1, 16):
    mintrio.concat("M"+snippetList[x]+".wav")

for y in range(16, 32):
    mintrio.concat("T"+snippetList[y]+".wav")


soundwave.play(mintrio)