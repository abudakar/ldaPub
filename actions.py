# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if"data:"in (tracker.latest_message)['text'] and"pdf"in (tracker.latest_message)['text']: 
            print("entered the decoding function for PDF attachment")
            dispatcher.utter_message(text="Request Submitted for review")

        else:
            dispatcher.utter_message(text="sorry i can't understand you! ")

        return []

class ActionPDF(Action):

    def name(self) -> Text:
        return "action_pdf"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("[payslip.pdf](https://gisinter.online/wp-rasa-awamleh/wp-content/uploads/2020/07/payslippdf.pdf)")
        
        

        return []
        
class ActionAbsencesBalance(Action):

    def name(self) -> Text:
        return "action_img"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("[Absences Balance](https://gisinter.online/wp-rasa-awamleh/wp-content/uploads/2020/07/payslip.pdf)")
        
        

        return []


class ActionAbsencesBalanceAr(Action):

    def name(self) -> Text:
        return "action_img_ar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("- الرصيد الكلي: 14 يوم \n - الرصيد المستخدم: 2 يوم \n - الرصيد المتبقي: 12 يوم \n \n لاظهار رصيد الاجازات في صورة الرجاء الضغط على الرابط بالاسفل\n \n [رصيد الاجازات](https://gisinter.online/wp-rasa-awamleh/wp-content/uploads/2020/07/payslip.pdf)")
        
        

        return []
