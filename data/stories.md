## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## master challange
* master_name
   - utter_mastername
   
## who is boss
* who_is_boss
   - utter_who_is_boss
   
## seach exercices + muscle group
* greet
   - utter_greet
* excercice_search_provider{"exercice_type": "workout"}
   - utter_ask_muscle_group
* inform{"muscle_group": "back"}
   - action_exercice_seach
* thanks
   - utter_goodbye
   
 ## seach exercices happy path
* greet
   - utter_greet
* excercice_search_provider{"exercice_type": "workout", "muscle_group": "back"}
   - action_exercice_seach
* thanks
   - utter_goodbye  
