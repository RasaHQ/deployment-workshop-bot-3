"""Custom action for exam project of the deployment workshop

Do NOT modify this code.
"""
import os
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHi(Action):
    """The action that says hi

    It expects it's name go be defined in the environment variable: MY_NAME"""

    def name(self) -> Text:
        return "action_hi"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hi, from custom action 'action_hi' !")
        dispatcher.utter_message(text="How are you?")

        # get my name from an environment variable
        my_name = os.environ.get("MY_NAME")
        if my_name:
            dispatcher.utter_message(text=f"My name is {my_name}")
        else:
            dispatcher.utter_message(
                text=(
                    "I do not know my name, "
                    "please set it in the environment variable 'MY_NAME'"
                )
            )

        return []
