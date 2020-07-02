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
   - utter_how_can_I_help
   
 ## search exercices happy path
* exercice_search_provider{"exercice_type": "workout", "muscular_group": "back"}
   - action_exercice_search
   - slot{"muscular_group":"chest"}
* goodbye
   - utter_how_can_I_help  

## custom helloworld action
* helloworld_action
   -action_hello_world_program

## search for gym
* gym_search_provider
  -action_search_gym
* thanks
  - utter_you_are_welcome

## authentificating the user by email
* greet
  - utter_have_we_met
* affirm
  - utter_ask_mail_address
* user_email_inform{"user_email": "ovidiu.negru47@gmail.com"}
  - slot{"user_email":"sasgae@asdawd.com"}
  - action_confirm_user_email
  - utter_how_can_I_help

  ## just asking a questions
* greet
  - utter_have_we_met
* deny
  - utter_ask_create_account
* deny
  - utter_how_can_I_help 
  
## create a new user
* greet
  - utter_have_we_met
* deny
  - utter_ask_create_account
* affirm
  - form_user
  - form{"name": "form_user"}
  - form{"name": null}
* affirm
  - utter_how_can_I_help
  
## interactive_story_1
* greet
    - utter_have_we_met
* deny
    - utter_ask_create_account
* affirm
    - form_user
    - form{"name": "form_user"}
    - slot{"requested_slot": "user_name"}
* form: user_name_inform{"user_name": "John Doe"}
    - form: form_user
    - slot{"user_name": "John Doe"}
    - slot{"requested_slot": "user_age"}
* form: user_age_inform{"user_age": "28"}
    - form: form_user
    - slot{"user_age": "28"}
    - slot{"requested_slot": "user_weight"}
* form: user_weight_inform{"user_weight": "78"}
    - form: form_user
    - slot{"user_weight": "78"}
    - slot{"requested_slot": "user_height"}
* form: user_height_inform{"user_height": "185"}
    - form: form_user
    - slot{"user_height": "185"}
    - slot{"requested_slot": "user_sex"}
* form: user_sex_inform{"user_sex": "M"}
    - form: form_user
    - slot{"user_sex": "M"}
    - slot{"requested_slot": "user_scope"}
* form: user_scope_inform{"user_scope": "loose weight"}
    - form: form_user
    - slot{"user_scope": "loose weight"}
    - slot{"requested_slot": "user_times_at_gym"}
* form: user_times_at_gym_inform{"user_times_at_gym": "4"}
    - form: form_user
    - slot{"user_times_at_gym": "4"}
    - slot{"requested_slot": "user_email"}
* form: user_email_inform{"user_email": "johndoe69@gmail.com"}
    - form: form_user
    - slot{"user_email": "johndoe69@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_goodbye
* stop

## get recipe from api happy path
* recipe_search_provider{"main_ingredient": "chicken"}
  - action_search_recipe
  - slot{"main_ingredient": "pork"}
* thanks

## get meal search
* calories_search_provider
  - utter_ask_meal
* ingredient_inform{"main_ingredient": "pork"}
  - action_search_meal
* thanks

## interactive_story_1
* calories_search_provider
    - utter_ask_meal
* meal_inform{"main_ingredient": "avocados"}
    - slot{"main_ingredient": "avocados"}
    - action_search_meal
* thanks
