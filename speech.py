# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3
import gesture as gs

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

r = sr.Recognizer()

while(1):

    try:

        # use the microphone as source for input.
        # with sr.Microphone() as source2:
        #     r.adjust_for_ambient_noise(source2, duration=0.2)
        #     audio2 = r.listen(source2)
        #     MyText = r.recognize_google(audio2)
        #     MyText = MyText.upper()
        #     gs.implementGesture(MyText)
        #     print("Did you say "+MyText)
        #     SpeakText(MyText)

        # var = int(input("Enter Command to be performed : "))
        var = input('Enter Command : ')
        var = var.upper()
        gs.implementGesture(var)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
