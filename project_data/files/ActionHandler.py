from datetime import datetime
from AppOpener import open
import requests

class ActionHandler:

    def __init__(self):
        # Initialize any necessary resources or APIs for action handling
        pass

    def handle_action(self, intent, entity):
        # Route the intent and entity to the appropriate action method
        if intent == 'time':
            return self.handle_time(entity)
        elif intent == 'weather':
            return self.handle_weather()
        elif intent == 'music':
            return self.handle_music(entity)
        else:
            return self.handle_default()

    def handle_time(self, entity):
        # Handle the time intent by returning the current time
        # or a specific time if provided in the entity

        now = datetime.now()

        format = '%Y-%m-%d %I:%M %p'
        dt_string = now.strftime(format)




        return dt_string

    def handle_weather(self):
        # Check if the entity specifies a location
        api_key = '8ef8a91be10e1df884c2d91a195ba2b5'
        url = f'https://api.openweathermap.org/data/2.5/forecast?q=Columbus&appid={api_key}'
        response = requests.get(url)
        print(response.status_code)
        print(response.text)
        data = response.json()

        # Extract the current weather information
        description = data['list'][0]['weather'][0]['description']
        temp = data['list'][0]['main'][0]['temp']
        feels_like = data['list'][0]['main'][0]['feels_like']

        return f"The current weather forecast in Columbus is {description} with a temperture of {temp} which feels like {feels_like}."

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
