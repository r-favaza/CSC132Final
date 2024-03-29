############################################
# Name: Cooper Wooten, Ray Favaza, Matthew Christensen, Keahi Temple
# Date: 4-24-2023
# Description: Paper piano (v3).
############################################
import RPi.GPIO as GPIO
from math import pi, sin
from time import sleep, time
import pygame
from array import array
from waveform_vis import WaveformVis

MIXER_FREQ = 44100
MIXER_SIZE = -16
MIXER_CHANS = 1
MIXER_BUFF = 1024

def lerp(a:float, b:float, f:float) -> float:
    """Linear interpolation between a and b by fraction f"""
    return (1 - f) * a + f * b

# the note generator class
class Note(pygame.mixer.Sound):

    # note that volume ranges from 0.0 to 1.0
    def __init__(self, frequency, volume, type):
        self.frequency = frequency
        # initialize the note using an array of sample
        pygame.mixer.Sound.__init__(self, buffer=self.build_samples(type))
        self.set_volume(volume)
        self.type = type

    def squareWave(self, period, amplitude, samples):
        for t in range(period):
            if (t < period / 2):
                samples[t] = amplitude
            else:
                samples[t] = -amplitude

    def triangleWave(self, period, amplitude, samples):
        for t in range(period):
            # start
            if (t < period / 4):
                samples[t] = round(amplitude * lerp(0, 1, t / (period / 4)))
            # middle section
            elif (t < 3*period / 4):
                samples[t] = round(amplitude * lerp(1, -1, (t - period / 4) / (period / 2)))
            # end section
            else:
                samples[t] = round(amplitude * lerp(-1, 0, (t - 3*period / 4) / (period / 4)))

    def sawtoothWave(self, period, amplitude, samples):
        for t in range(period):
            if (t < period / 2):
                samples[t] = round(amplitude * lerp(0, 1, t / (period / 2))) # peak
            else:
                samples[t] = round(amplitude * lerp(-1, 0, (t - period / 2) / (period / 2))) # drop

    def sinWave(self, period, amplitude, samples):
        for t in range(period):
            fraction = t / period
            samples[t] = round(amplitude * sin(2*pi*fraction)) # sin has a period of 2pi so we multiply by that

    # builds an array of samples for the current note
    def build_samples(self, type):
        # the wave generation functions
        waveTypes = {"square":self.squareWave, "triangle":self.triangleWave, "sawtooth":self.sawtoothWave, "sin":self.sinWave}

        # calculate the period and amplitude of the note's wave
        period = int(round(MIXER_FREQ / self.frequency))
        amplitude = 2 ** (abs(MIXER_SIZE) - 1) - 1
        # initialize the note's samples (using an arrot of signed 16-bit "shorts")
        samples = array("h", [0] * period)
        
        # build the note's samples based on the type of wave
        waveTypes[type](period, amplitude, samples)
        
        vis = WaveformVis()
        vis.visSamples(samples, type)

        return samples
    
# waits until a note is pressed
def wait_for_note_start():
    while(True):
         # first, check for notes
         for key in range(len(keys)):
            if (GPIO.input(keys[key])):
                return key
            # next, check for the play button
            if (GPIO.input(play)):
                # debounce the switch
                while (GPIO.input(play)):
                    sleep(0.01)
                return "play"
            # finally, check for the record button
            if (GPIO.input(record)):
                # debounce the switch
                while (GPIO.input(record)):
                    sleep(0.01)
                return "record"
            sleep(0.01)

# waits until a note is released
def wait_for_note_stop(key):
    pass
    while (GPIO.input(key)):
        sleep(0.1)

# plays a recorded song
def play_song():
    # each element in the song list is a list composed of two
    # parts: a note (or silence) and a duration
    for part in song:
        note, duration = part
        # if it's a silence, delay for its duration
        if (note == "SILENCE"):
            sleep(duration)
        # otherwise, play the note for its duration
        else:
            notes[note].play(-1)
            sleep(duration)
            notes[note].stop()

# preset mixer initialization arguments: frequency (44.1K), size
# (16 bits signed), channels (mono), and buffer size (1KB)
# then, initialize the pygame library
pygame.mixer.pre_init(MIXER_FREQ, MIXER_SIZE, MIXER_CHANS, MIXER_BUFF)
pygame.mixer.init()
pygame.init()

# use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)

# setup the pins and frequencies for the notes (C, E, G, B)
keys = [20, 16, 12, 26]
freqs = [261.6, 329.6, 392.0, 493.9]
waves = ["square", "triangle", "sawtooth", "sin"]
notes = []

# setup the button pins
play = 19
record = 21

# setup the LED pins
red = 27
green = 18
blue = 17 # if red is too dim, use blue

# setup the input puns
GPIO.setup(keys, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(play, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(record, GPIO.IN, GPIO.PUD_DOWN)

# setup the output pins
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# begin in a non-recording state and initialize the song
recording = False
song = []

# the main part of a program
print("Welcome to Paper Piano!")
print("Press Ctrl+C to exit...")

'''validTypes = ["square", "triangle", "sawtooth", "sin"]

waveType = None

while waveType == None:
    selection = input("Input what wave type you want (square, triangle, sawtooth, sin):")
    if selection in validTypes:
        waveType = selection
        print(f"You have choosen {selection}")
    else:
        print("Invalid selection, the valid types are:", validTypes)

# create the actual notes
for n in range(len(freqs)):
    notes.append (Note(freqs[n], 1, waveType))''' # change your note type here

# create the actual notes with different wave forms
for n in range(len(freqs)):
    notes.append(Note(261.6, 1, waves[n])) # change your note type here

# detect when Ctrl+C is pressed so that we can reset the GPIO pins
try:
    while(True):
        # start a timer
        start = time()
        # play a note when pressed...until released (also
        # detect play/record)
        key = wait_for_note_start()
        # note the duration of the silence
        duration = time() - start
        # if recording, append the duration of the silence
        if (recording):
            song.append(["SILENCE", duration])
            # if the record button was pressed
            if (key == "record"):
                # if not previously recording, reset the song
                if (not recording):
                    song = []
                # note the recording state and turn on the red LED
                recording = not recording
                GPIO.output(red, recording)
                # if the play button was pressed
            elif (key == "play"):
                # if recording, stop
                if (recording):
                    recording = False
                # turn on the green LED
                GPIO.output(red, False)
                GPIO.output(green, True)
                # play the song
                play_song()
                GPIO.output(green, False)
            # otherwise, a piano key was pressed
            else:
                # start the timer and play the note
                start = time()
                notes[key].play(-1)
                wait_for_note_stop(keys[key])
                notes[key].stop()
                # once the note is released, stop the timer
                duration = time() - start
                # if recording, append the note and its duration
                if (recording):
                    song.append([key, duration])
except KeyboardInterrupt:
    # reset the GPIO pins
    GPIO.cleanup()