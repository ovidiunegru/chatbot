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
            passwd="p@ss123",
            database="testdatabase"
            #auth_plugin='mysql_native_password'
        )

        exercice = tracker.get_slot("exercice_type")
        muscularGroup = tracker.get_slot("muscular_group")

        cursor = mydb.cursor()
        query="SELECT * FROM exercises where exercise_group = '%s'" % muscularGroup
        try:
            cursor.execute(query)
            if cursor.execute(query) == 0:
                print("The data was extracted")
        except:
            print("mysql")

        #dispatcher.utter_message("Here is the muscle group of the {}:{}".format(exercice,muscularGroup))
        dispatcher.utter_message("Here are some exercises for {}".format(muscularGroup))
        records = cursor.fetchall()

        for exercices in records:
            dispatcher.utter_message(str(exercices[0]))

        return []

class ActionConfirmUserEmail(Action):

    def name(self) -> Text:
        return "action_confirm_user_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="p@ss123", database="testdatabase")   # # auth_plugin='mysql_native_password'
        userEmail = tracker.latest_message.get('text')
        print(userEmail)
        query = "select user_name from users where user_email = '{}';".format(userEmail)
        cursor = mydb.cursor()
        print(query)

        try:
            x = cursor.execute(query)
            if x == 0:
                print("Sorry, could not find you in the DB")
            else:
                result = cursor.fetchone()
                dispatcher.utter_message("Welcome back, {} !".format(str(result[0])))
        except:
            print("SQL statement could not be found")

        return []


class ActionHelloWorldCustom(Action):

    def name(self) -> Text:
        return "action_hello_world_program"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World! SECOND custom action")

        return []
