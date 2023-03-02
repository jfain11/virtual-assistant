# Controls the voice recognition for the virtual assistant.

import speech_recognition as sr

r = sr.Recognizer()



mic = sr.Microphone()


input("press when ready")git 
with mic as source:
    audio = r.listen(source)


response = {
        "success": True,
        "error": None,
        "transcription": None
}
try:
    response["transcription"] = r.recognize_google(audio)
except sr.RequestError:
    # API was unreachable or unresponsive
    response["success"] = False
    response["error"] = "API unavailable"

except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

print(response)