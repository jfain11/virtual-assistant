from datetime import datetime
from AppOpener import open

class ActionHandler:

    def __init__(self):
        # Initialize any necessary resources or APIs for action handling
        pass

    def handle_action(self, intent, entity):
        # Route the intent and entity to the appropriate action method
        if intent == 'time':
            return self.handle_time(entity)
        elif intent == 'weather':
            return self.handle_weather(entity)
        elif intent == 'music':
            return self.handle_music(entity)
        else:
            return self.handle_default()

    def handle_time(self, entity):
        # Handle the time intent by returning the current time
        # or a specific time if provided in the entity
        date_string = '2009-11-29 03:17 PM'
        format = '%Y-%m-%d %I:%M %p'
        my_date = datetime.strptime(date_string, format)

        # This prints '2009-11-29 03:17 AM'
        date = my_date.strftime(format)
        return "time"

    def handle_weather(self, entity):
        # Handle the weather intent by returning the current weather
        # or a forecast if requested in the entity
        return "weather"

    def handle_music(self, entity):
        # Handle the music intent by playing the requested song,
        # artist, or playlist on a music streaming service

        return "music"

    def handle_search(self, query):
        # Handle a web search by opening a browser and performing the query

        return "search"

    def handle_reminder(self, time, message):
        # Handle setting a reminder by scheduling a notification
        # or sending an email or text message
        return "reminder"

    def handle_default(self):
        # Handle any unrecognized intent by providing a default response
        return "sorry, i could not understand your request"
