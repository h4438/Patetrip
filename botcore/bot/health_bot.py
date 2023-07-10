import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../..")
from botcore.chains.nutri_suggest import build_nutri_suggest_chain
from botcore.chains.workout_suggest import build_workout_suggest_chain
from botcore.utils import CheckupMemory, parse_nested_json

from langchain.llms import BaseLLM
from typing import Dict

class HealthBot:

    def __init__(self, model: BaseLLM, debug=False):
        self.day = 1
        # nutrition
        self.nutri_mem = CheckupMemory(input_key='input', role="nutrition doctor")
        self.nutri_chain = build_nutri_suggest_chain(model, self.nutri_mem.get(), debug)
        # workout
        self.workout_mem = CheckupMemory(input_key='input', role="professional personal trainner")
        self.workout_chain = build_workout_suggest_chain(model, self.workout_mem.get(), debug)
        self.note = None
        self.suggestions = []
    
    def load_note(self, input_data: Dict):
        self.note = input_data

    def nutri_checkup(self):
        if self.day == 1:
            human_input = "Hello doctor"
        else:
            human_input = "I have followed your advise"
        inputs = {"time_unit": "week", "timely": "weekly",
                  "day_number": self.day, "input": human_input, **self.note}
        ans = self.nutri_chain(inputs)
        data = parse_nested_json(ans['result'])
        self.nutri_mem.load_conversation(data['reason'], self.day)
        return data

    def workout_checkup(self):
        if self.day == 1:
            human_input = "Hello"
        else:
            human_input = "I have followed your advise"
        inputs = {"time_unit": "week", "timely": "weekly", "day_number": self.day,
                "input": "Hello!", **self.note}
        ans = self.workout_chain(inputs)
        data = parse_nested_json(ans['result'])
        self.workout_mem.load_conversation(data['description'], self.day)
        return data

    def full_checkup(self):
        nutri = self.nutri_checkup()
        workout = self.workout_checkup()
        self.day += 1

        data = {"food_list": nutri['ingredients'], 'food_desc': nutri['reason'],
                'workout_list': workout['exercises'], 'workout_desc': workout['description']}

        self.suggestions.append(data)
        return nutri, workout

    def get(self, index: int):
        return self.suggestions[index]

    def getall(self):
        return self.suggestions
