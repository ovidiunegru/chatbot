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
from rasa_sdk.forms import FormAction
import mysql.connector


class ActionExerciceSearch(Action):

    def name(self) -> Text:
        return "action_exercice_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Chifteabobo0228",
            database="testdatabase"
            #auth_plugin='mysql_native_password'
        )

        exercice = tracker.get_slot("exercice_type")
        muscularGroup = tracker.get_slot("muscular_group")

        cursor = mydb.cursor()
        query="SELECT * FROM Exercice where exercice_group = '%s'" % (muscularGroup)
        try:
            cursor.execute(query)
            if cursor.execute(query) == 0:
                print("Sorry There was an issue")
        except:
            print("Error 1: unable to retreive data")

        #dispatcher.utter_message("Here is the muscle group of the {}:{}".format(exercice,muscularGroup))
        dispatcher.utter_message("Here are some exercices for {}".format(muscularGroup))

        records = cursor.fetchall()

        for exercices in records:
            exerciceList = exercices[0],

        dispatcher.utter_message(str(exerciceList))
        return []


class ActionHelloWorldCustom(Action):

    def name(self) -> Text:
        return "action_hello_world_program"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World! SECOND custom action")

        return []


