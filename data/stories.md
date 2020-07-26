## happy path
* greet
  - utter_greet
  - utter_greet_Questions_en

* mood_great
  - utter_happy

## WelcomingMsg
* greet
  - utter_greet
  - utter_greet_Questions_en

## sad path 1
* greet
  - utter_greet
  - utter_greet_Questions_en
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
  - utter_greet_Questions_en
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

## Salary_en
* salary
  - utter_salary_en

## paySlip_en
* paySlip
  - action_pdf

## employee_information_en
* employee_information
  - utter_employee_information_en

## bankAcc_information_en
* bankAcc_information
  - utter_bankAcc_information_en

## employees_attendance_for_Manager_en
* employees_attendance_for_Manager
  - utter_employees_attendance_for_Manager_en

## notification_for_manager_en
* notification_for_manager
  - utter_notification_for_manager_en

## absences_balance_en
* absences_balance
  - utter_absences_balance_en
  - action_img

## arabic_salary
* salary_ar
  - utter_salary_ar
 
## arabic_paySlip
* paySlip_ar
  - action_pdf
 
## arabic_absences_balance
* absences_balance_ar
  - action_img_ar
 
## arabic_employee_information
* employee_information_ar
  - utter_employee_information_ar
 
## arabic_bankAcc_information
* bankAcc_information_ar
  - utter_bankAcc_information_ar
 
## arabic_employees_attendance_for_Manager
* employees_attendance_for_Manager_ar
  - utter_employees_attendance_for_Manager_ar
 
## arabic_notification_for_manager
* notification_for_manager_ar
  - utter_notification_for_manager_ar


## services_menu_en
* help_en
  - utter_greet_Questions_en

## ar_services_menu_ar
* help_ar
  - utter_greet_Questions_ar

## expense_en_scenario
* expense_en
  - utter_expense_en
  

## ar_expense_ar_scenario
* expense_ar
  - utter_expense_ar
  



## falback Scenario
* out_of_scope
  - action_default_fallback





