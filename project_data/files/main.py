from SpeechToText import *
from TextToSpeech import *
from IntentClassifier import *
from ActionHandler import *

from VirtualAssistantGUI import *

testObj = VirtualAssistantGUI()
testObj.add_response("hello, how may I assist you?", "assistant")
testObj.mainloop()