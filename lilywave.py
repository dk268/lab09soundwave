import audio


class Soundwave:
    def __init__(self, halftones, duration, amp, samplerate):
        self.length = duration
        self.maxvol = amp
        self.samplerate = samplerate
        self.samples = []


