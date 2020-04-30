## happy path
* greet
  - utter_how_can_I_help
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_how_can_I_help
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_how_can_I_help
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
* exercice_search_provider{"exercice_type": "workout"}
   - utter_ask_muscle_group
* exercice_inform{"muscle_group": "back"}
   - action_exercice_search
   - slot{"muscle_group":"chest"}
* goodbye
   - utter_goodbye
   
 ## search exercices happy path
* greet
   - utter_how_can_I_help
* exercice_search_provider{"exercice_type": "workout", "muscle_group": "back"}
   - action_exercice_search
   - slot{"muscle_group":"chest"}
* goodbye
   - utter_goodbye  

## custom helloworld action
* helloworld_action
   -action_hello_world_program
