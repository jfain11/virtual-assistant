# Controls the voice recognition for the virtual assistant.

import speech_recognition as sr

class SpeechRecognizer:

    def __init__(self):

        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()




    def listen(self) -> str:

        with self.mic as source:
            audio = self.recognizer.listen(source)

        response = {
                "success": True,
                "error": None,
                "transcription": None
        }
        try:
            response["transcription"] = self.recognizer.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
            return response["error"]

        except sr.UnknownValueError:
                # speech was unintelligible
                response["error"] = "Unable to recognize speech"
                return response["error"]

        return response["transcription"]



