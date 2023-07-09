import sys
import os
from langchain.llms import BaseLLM
from typing import List
sys.path.append(f"{os.path.dirname(__file__)}/../..")

from botcore.chains.allergen_diagnose_chain import build_allergen_diagnose_chain
from botcore.utils import QAMemory, parse_nested_json

class FoodAdvisor:

    def __init__(self, model: BaseLLM, problem:str, questions: List[str], answers: List[str]):
        self.memory = QAMemory(input_key='verb')
        self.memory.load_all(problem, questions, answers)
        self.diagnose = build_allergen_diagnose_chain(model, self.memory.memory)
        print("Food advisor is ready")

    def advise(self):
        ans = chain({"verb": "diagnose"})
        data = parse_nested_json(ans['result'])
