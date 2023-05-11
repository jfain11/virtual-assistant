import pyttsx3
import os

class TextToSpeech:
    """
    This class is responsible for converting text output into speech output.

    Attributes:
        engine: A text-to-speech engine to use for conversion (e.g., Google Text-to-Speech, Microsoft Speech API, etc.)
        volume: The volume level for speech output.
        voice: The selected voice for speech output.

    Methods:
        set_volume(level: float) -> None:
            Sets the volume level for speech output.

        set_voice(voice: str) -> None:
            Sets the selected voice for speech output.

        speak(text: str) -> None:
            Converts the given text into speech output and plays it.
    """

    def __init__(self):
        """
        Initializes the TextToSpeech object.

        Args:
            engine: A text-to-speech engine to use for conversion (e.g., Google Text-to-Speech, Microsoft Speech API, etc.)
        """
        self.engine = pyttsx3.init()
        self.volume = 1.0
        self.voices = self.engine.getProperty('voices')
        self.rate = self.engine.getProperty("rate")


    def set_volume(self, level: float) -> None:
        """
        Sets the volume level for speech output.
        """
        self.volume = level

    def set_rate(self, rate: int) -> None:
        """
        Sets the rate for speech output.
        """
        self.engine.setProperty("rate", rate)

    def set_voice(self, voice: str) -> None:
        """
        Sets the selected voice for speech output.
        """
        if voice.lower() == "male":
            self.engine.setProperty('voice', self.voices[0].id)
        elif voice.lower() == "female":
            self.engine.setProperty('voice', self.voices[1].id)


    def speak(self, text: str) -> None:
        """
        Converts the given text into speech output and plays it.

        Args:
            text: A string representing the text to be spoken.
        """
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()

