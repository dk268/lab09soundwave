import audio
import math


class Soundwave:
    def __init__(self, halftones=0, duration=0.0, amp=1, samplerate=44100):

        if isinstance(halftones,str) == True:
            self.samples = audio.read_file(halftones)
        else:
            self.length = duration
            self.maxvol = amp
            self.samplerate = samplerate
            self.samples = []
            freq = 440 * (2 ** ((halftones + 3) / 12))
            for i in range(int(self.length * self.samplerate)):
                self.samples.append(amp * math.sin(2 * math.pi * freq * i / samplerate))

    def play(self):
        audio.play(self.samples)
        # print (self.samples)

    def concat(self, s2):
        self.samples.extend(s2.samples)
        self.length += s2.length
        if self.maxvol < s2.maxvol:
            self.maxvol = s2.maxvol

    def plus(self, s2):
        # longerLen = 0
        if len(self.samples) > len(s2.samples):
            longerLen = self.length
            longerSample = self.samples
            shorterLen = len(s2.samples)
            shorterSample = s2.samples
        else:
            longerLen = s2.length
            longerSample = s2.samples
            shorterLen = len(self.samples)
            shorterSample = self.samples

        for i in range(len(shorterLen)):
            longerSample[i] = longerSample[i]+shorterSample[i]


        if self.maxvol > s2.maxvol:
            newvol = self.maxvol
        else:
            newvol = s2.maxvol

        sumWave = Soundwave(self, 0, longerLen, newvol, 44100)
        sumWave.samples = longerSample


