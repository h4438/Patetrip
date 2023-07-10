import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../..")
from botcore.chains.nutrition import build_nutri_suggest_chain
from botcore.utils import parse_nutri_list

from langchain.llms import BaseLLM
from typing import Dict

class HealthBot:
    
    def __init__(self, model: BaseLLM, debug = False):
        self.nutri = build_nutri_suggest_chain(model, debug)
    

