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

    def __init__(self, engine: str):
        """
        Initializes the TextToSpeech object.

        Args:
            engine: A text-to-speech engine to use for conversion (e.g., Google Text-to-Speech, Microsoft Speech API, etc.)
        """
        self.engine = engine
        self.volume = 1.0
        self.voice = None

    def set_volume(self, level: float) -> None:
        """
        Sets the volume level for speech output.

        Args:
            level: A float between 0.0 and 1.0 representing the desired volume level.
        """
        self.volume = level

    def set_voice(self, voice: str) -> None:
        """
        Sets the selected voice for speech output.

        Args:
            voice: A string representing the desired voice.
        """
        self.voice = voice

    def speak(self, text: str) -> None:
        """
        Converts the given text into speech output and plays it.

        Args:
            text: A string representing the text to be spoken.
        """

