import speech_recognition as sr
audiofile = "audiofile.wav"
r=sr.Recognizer()

with sr.AudioFile(audiofile) as source:
    aud=r.record(source)

try:
    print("audio file", r.recognize_google(aud))
except sr.UnknownValueError:
    print("google speech recognition cant understand ")
except sr.RequestError:
    print("couldnt find the results from google recognition")
