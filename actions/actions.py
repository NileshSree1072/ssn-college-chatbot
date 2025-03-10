from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHelloWorld(Action):
    def name(self) -> str:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        # This is a simple example action that sends a custom response
        dispatcher.utter_message(text="Hello from a custom action! How can I assist you with SSN College?")
        return []