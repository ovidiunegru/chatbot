## happy path
* mood_great
  - utter_happy

## sad path 1
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
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
   
## seach exercices + muscle group
* exercice_search_provider{"exercice_type": "workout"}
   - utter_ask_muscle_group
* exercice_inform{"muscular_group": "back"}
   - action_exercice_search 
   - slot{"muscular_group":"chest"}
* goodbye
   - utter_goodbye
   
 ## search exercices happy path
* exercice_search_provider{"exercice_type": "workout", "muscular_group": "back"}
   - action_exercice_search
   - slot{"muscular_group":"chest"}
* goodbye
   - utter_goodbye  

## custom helloworld action
* helloworld_action
   -action_hello_world_program


## authentificating the user
* greet
  - utter_have_we_met
* affirm
  - utter_ask_mail_address
* email_inform{"user_email": "ovidiu.negru47@gmail.com"}
  - slot{"user_email":""}
  - action_confirm_user_email
  