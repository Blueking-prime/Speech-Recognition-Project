#!/usr/bin/env python3
import sys
import speech_recognition as speech


# Initializes recognizer
rec = speech.Recognizer()

if len(sys.argv) > 1:
    # Read from audio file
    print('Reading audio from audio file')
    audio_file = speech.AudioFile(sys.argv[1])
    with audio_file as source:
        # Noise adjustment removed as it severely impacts the accuracy
        # rec.adjust_for_ambient_noise(track)
        audio = rec.record(source)
else:
    # Read from Microphone
    print('Recording audio. Speak into the mic...')
    mic = speech.Microphone()
    with mic as source:
        audio = rec.listen(source)
    print('Recorded audio')


# Transcribes audio using Google's STT API
try:
    print('Transcribing audio using Google...')
    text = rec.recognize_google(audio)
    print(text)
except speech.RequestError:
    print('Unable to contact the API')
except speech.UnknownValueError:
    print('Unable to transcribe audio data')
