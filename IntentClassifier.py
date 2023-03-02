import re


class IntentClassifier:
    def __init__(self):
        # Define the patterns
        self.patterns = {
            'time': re.compile(r'.*(what\stime\s(is\sit|time\sis\sit|is\sit)\snow|what\'s\sthe\stime).*', re.IGNORECASE),
            'weather': re.compile(r'.*(what(\'s| is))?\s*(the)?\s*(weather|forecast)\s*(like)?\s*(today|tonight|tomorrow)?\s*(right now|at the moment|currently)?\s*(\?)?.*', re.IGNORECASE),
            'app': re.compile(r'.*(open|start)\s?(spotify|chrome|notepad|calculator).*', re.IGNORECASE)
        }

    # Define the function to parse the input
    def parse_input(self, input_str):
        for intent, pattern in self.patterns.items():
            match = pattern.match(input_str)
            if match:
                return intent, match.group(0)

        return None, None


# Test the function with some example inputs
intent_classifier = IntentClassifier()

input_str = 'What is the weather?'
intent, entity = intent_classifier.parse_input(input_str)
print(f'Intent: {intent}, Entity: {entity}')

input_str = 'Open Spotify'
intent, entity = intent_classifier.parse_input(input_str)
print(f'Intent: {intent}, Entity: {entity}')

input_str = 'What time is it now?'
intent, entity = intent_classifier.parse_input(input_str)
print(f'Intent: {intent}, Entity: {entity}')
