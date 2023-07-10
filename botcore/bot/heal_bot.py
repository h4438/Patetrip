import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../..")
from botcore.chains.nutrition import build_nutri_suggest_chain
from botcore.chains.workout import build_workout_suggest_chain
from botcore.utils import parse_nutri_list, parse_workout_list

from langchain.llms import BaseLLM
from typing import Dict

class HealthBot:
    
    def __init__(self, model: BaseLLM, debug = False):
        self.nutri = build_nutri_suggest_chain(model, debug)
        self.work = build_workout_suggest_chain(model, debug)

    def checkup(self, input_data: Dict):
        inputs = {"time_unit": "month", "timely": "monthly", **input_data}
        nutri = self.nutri(inputs)
        nutritions = parse_nutri_list(nutri['result'])
        work = self.work(inputs)
        workout = parse_workout_list(work['result'])
        data = [{**n, **w} for n,w in zip(nutritions, workout)]
        return data

