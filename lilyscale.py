import soundwave
import sys

intervals = [[2,2,1,2,2,2,1],
                   [2,1,2,2,1,2,2],
                   [3,2,1,1,3,2]]

startNote = sys.argv[1]
if sys.argv[2] == "M":
    scaleSet = intervals[0]
elif sys.argv[2] == "N":
    scaleSet = intervals[1]
elif sys.argv[2] == "B":
    scaleSet = intervals[2]

aggregateHalftones = startNote
theScale = soundwave.Soundwave(startNote, 0.5, 1, 44100)

for note in range(len(scaleSet)):
    aggregateHalftones += scaleSet[note]
    newNote = soundwave.Soundwave(startNote+aggregateHalftones, 0.5,1,44100)
    theScale.concat(newNote)

soundwave.play(theScale)