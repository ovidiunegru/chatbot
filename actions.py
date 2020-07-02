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

from urllib.request import urlopen
import json

import googlemaps
import time




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

        print('action_exercice_search')
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

        print("action_confirm_user_email")
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
            "user_name": [self.from_text()],
            "user_age": [self.from_text()],
            "user_weight": [self.from_text()],
            "user_height": [self.from_text()],
            "user_sex": [self.from_text()],
            "user_scope": [ self.from_text()],
            "user_times_at_gym": [self.from_text()],
            "user_email": [self.from_text()],
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
                "user_times_at_gym, user_email) values ('{}',{},{},{},'{}','{}',{},'{}');".format(user_name, user_age,
                                                                                          user_weight, user_height,
                                                                                          user_sex, user_scope,
                                                                                          user_times_at_gym, user_email)
        print(query)
        cursor = mydb.cursor()

        try:
            result = cursor.execute(query)
            mydb.commit()
            dispatcher.utter_message(template="utter_submit", name=tracker.get_slot('user_name'),
                                     email=tracker.get_slot('user_email'))
        except:
            dispatcher.utter_message("Error!")

        return []

    # def validate(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
    #     userName=tracker.get_slot('user_name')
    #     dispatcher.utter_message(str(userName))


class ActionRecipeSearch(Action):

    def name(self) -> Text:
        return "action_search_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("action_search_recipe")

        app_id = 'ff85071b'
        app_key = 'd3efa4ef3ec092ef2cc016bb530897f4'


        recipeIngredients = tracker.get_slot('main_ingredient')

        if not recipeIngredients:
            print(recipeIngredients)
        else:
            print(recipeIngredients)
            url = "https://api.edamam.com/search?q='%s'&app_id=ff85071b&app_key=d3efa4ef3ec092ef2cc016bb530897f4&from=0&to=3" %recipeIngredients
            
            data = json.load(urlopen(url))
            print(url)

            for d in data['hits']:
                recipe = d['recipe']
                recipeName = recipe.get('label')
                ingredients = recipe.get('ingredientLines')
                ingredient = ingredients[0]
                recipeUrl = recipe.get('url')

                dispatcher.utter_message(text="Recipe: {}".format(recipeName))
                dispatcher.utter_message(text="Main ingredients: {}".format(ingredient))
                dispatcher.utter_message(text="More informations here: {}".format(recipeUrl))

                print("Recipe name: ",recipeName)
                print("Recipe ingredients: " , ingredient)


        return []


class ActionMealSearch(Action):

    def name(self) -> Text:
        return "action_search_meal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("action_search_meal")
        app_id = '2ae12d8e'
        app_key = '1c41fde6eeefe0f9f39d1100d3eed619'


        #mealIngredients = tracker.latest_message.get("text", "")
        mealIngredients = tracker.get_slot('main_ingredient')

        if not mealIngredients:
            print(mealIngredients)
        else:
            print(mealIngredients)

            editedText = mealIngredients.replace(" ", "%20")
            print(editedText)
            url = "https://api.edamam.com/api/nutrition-data?app_id=2ae12d8e&app_key=1c41fde6eeefe0f9f39d1100d3eed619&ingr=1%20" + editedText
            
            data = json.load(urlopen(url))
            print(url)

            proteins = data.get('calories')
            print(proteins)

            dispatcher.utter_message(text="Your meal is about: {} calories".format(proteins))


        return []


class ActionGymSearch(Action):

    def name(self) -> Text:
        return "action_search_gym"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sure! Just a second")



        # Define the API Key.
        API_KEY = 'AIzaSyCa-lfc1U7no3J5vgEquiMrHsWEoQrq0WQ'

        # Define the Client
        gmaps = googlemaps.Client(key = API_KEY)

        # Do a simple nearby search where we specify the location
        # in lat/lon format, along with a radius measured in meters
        places_result  = gmaps.places_nearby(location='44.451893, 26.123038', radius = 2000, open_now =False , type = 'gym')

        time.sleep(2)

        place_result  = gmaps.places_nearby(page_token = places_result['next_page_token'])

        stored_results = []

        counter = 0

        # loop through each of the places in the results, and get the place details.
        for place in places_result['results']:

            if counter == 10:
                break

            # define the place id, needed to get place details. Formatted as a string.
            my_place_id = place['place_id']

            # define the fields you would liked return. Formatted as a list.
            my_fields = ['name','formatted_phone_number','website']

            # make a request for the details.
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)

            # print the results of the details, returned as a dictionary.
            print(places_details['result'])

            dispatcher.utter_message(places_details['result'].get("name"))
            dispatcher.utter_message(places_details['result'].get("formatted_phone_number"))
            dispatcher.utter_message(places_details['result'].get("website"))
            dispatcher.utter_message()

            counter = counter + 1

            # store the results in a list object.
            # stored_results.append(places_details['result'])


        return []



class ActionHelloWorldCustom(Action):

    def name(self) -> Text:
        return "action_hello_world_program"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sit on the bench holding two dumbbells at shoulder height with an overhand grip. Press the weights up above your head until your arms are fully extended. Return slowly to the start position.")
        dispatcher.utter_message(text="https://www.youtube.com/watch?v=0JfYxMRsUCQ")

        return []
