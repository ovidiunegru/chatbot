# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

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
            # auth_plugin='mysql_native_password'
        )

        exercice = tracker.get_slot("exercice_type")
        muscularGroup = tracker.get_slot("muscular_group")

        cursor = mydb.cursor()
        query = "SELECT * FROM exercises where exercise_group = '%s'" % muscularGroup
        try:
            cursor.execute(query)
            if cursor.execute(query) == 0:
                print("The data was extracted")
        except:
            print("mysql")

        # dispatcher.utter_message("Here is the muscle group of the {}:{}".format(exercice,muscularGroup))
        dispatcher.utter_message("Here are some exercises for {}:".format(muscularGroup))
        records = cursor.fetchall()

        for counter, exercices in enumerate(records):
            dispatcher.utter_message(str(counter + 1))
            dispatcher.utter_message(str(exercices[0]))
            dispatcher.utter_message(
                "You should do {} reps with {} sets. {}".format(exercices[4], exercices[5], exercices[6]))

        return []


class ActionConfirmUserEmail(Action):

    def name(self) -> Text:
        return "action_confirm_user_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="p@ss123",
                                       database="testdatabase")  # # auth_plugin='mysql_native_password'
        userEmail = tracker.latest_message.get('text')
        print(userEmail)
        query = "select user_name from users where user_email = '{}';".format(userEmail)
        cursor = mydb.cursor()
        print(query)

        try:
            x = cursor.execute(query)
            if x == 0:
                print("Sorry, could not find you in the DB")
                dispatcher.utter_message("Sorry I could not find you by your email! :( ")
            else:
                result = cursor.fetchone()
                dispatcher.utter_message("Welcome back, {} !".format(str(result[0])))
                dispatcher.utter_message("How can I help you?")
        except:
            dispatcher.utter_message("Sorry I could not find you by your email! :( ")
        return []


class ActionFormUserInfo(FormAction):

    def name(self) -> Text:
        return "form_user"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["user_name", "user_age", "user_weight", "user_height", "user_sex", "user_scope", "user_times_at_gym",
                "user_email"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "user_name": [self.from_entity(entity="user_name", intent='user_name_inform'),
                          self.from_text()],
            "user_age": [self.from_entity(entity="user_age", intent='user_age_inform'),
                         self.from_text()],
            "user_weight": [self.from_entity(entity="user_weight", intent='user_weight_inform'),
                            self.from_text()],
            "user_height": [self.from_entity(entity="user_height", intent='user_height_inform'),
                            self.from_text()],
            "user_sex": [self.from_entity(entity="user_sex", intent='user_sex_inform'),
                         self.from_text()],
            "user_scope": [self.from_entity(entity="user_scope", intent='user_scope_inform'),
                           self.from_text()],
            "user_times_at_gym": [self.from_entity(entity="user_times_at_gym", intent="user_times_at_gym_inform"),
                                  self.from_text()],
            "user_email": [self.from_entity(entity="user_email", intent="email_inform"),
                           self.from_text()],
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
                  after all required slots are filled"""
        user_name = tracker.get_slot('user_name')
        user_age = tracker.get_slot('user_age')
        user_weight = tracker.get_slot('user_weight')
        user_height = tracker.get_slot('user_height')
        user_sex = tracker.get_slot('user_sex')
        user_scope = tracker.get_slot('user_scope')
        user_times_at_gym = tracker.get_slot('user_times_at_gym')
        user_email = tracker.get_slot('user_email')

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="p@ss123",
                                       database="testdatabase")
        query = "insert into users(user_name, user_age, user_weight, user_height, user_sex, user_scope, " \
                "user_times_at_gym, user_email) values ({},{},{},{},{},{},{},{});".format(user_name, user_age,
                                                                                          user_weight, user_height,
                                                                                          user_sex, user_scope,
                                                                                          user_times_at_gym, user_email)
        print(query)
        cursor = mydb.cursor()

        try:
            result = cursor.execute(query)
            dispatcher.utter_message(template="utter_submit", name=tracker.get_slot('user_name'),
                                     email=tracker.get_slot('user_email'))
        except:
            dispatcher.utter_message("Error!")

        return []

    # def validate(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
    #     userName=tracker.get_slot('user_name')
    #     dispatcher.utter_message(str(userName))


class ActionHelloWorldCustom(Action):

    def name(self) -> Text:
        return "action_hello_world_program"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World! SECOND custom action")

        return []
