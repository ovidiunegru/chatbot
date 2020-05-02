# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionExerciceSearch(Action):

    def name(self) -> Text:
        return "action_exercice_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        exercice = tracker.get_slot("exercice_type")
        muscularGroup = tracker.get_slot("muscular_group")
        dispatcher.utter_message("Here is the muscle group of the {}:{}".format(exercice,muscularGroup))

        return []


class ActionHelloWorldCustom(Action):

    def name(self) -> Text:
        return "action_hello_world_program"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World! First custom action")

        return []
