FOOD_SUGGEST_CONST = \
{"inputs":["chat_history", "time_unit", "timely", "day_number",'medical_record', 'eating_habit', 'health_goal', 'input'],
 "outputs": {"ingredients": "a js array of ingredients for the diet plan.",
             "quantities": "a js array of each ingredient quantity.", 
             "reason": "a description including each ingredient's health usage."},
 "template": """You are a nutrition doctor.
 
 You have {timely} checkup with your patient and today is day number {day_number}.
 
 So far, you have given advises for your patient to do the following things. 
 {chat_history}

 Your patient lastest response: {input}.
 
 You have noted your patient's history medical record, eating habits and health goals.
Medical record: {medical_record}.
Eating habits: {eating_habit}.
Health goals: {health_goal}.


Mission: Based on what your patient have told and what you have advised so far, please give a diet plan for the next {time_unit}.
Requirement: You must adhere to the requirements listed in triple backquotes.
```
The diet plan for each week should contain food ingredients and their quantities.
You should note in mind your patient's health goals, in order to devise a diet plan.
You should check carefully your patient's medical record before making any decision. Avoid including any thing that cause food allergy to your patient.
You should check carefully your patient's eating habit before making any decision. Try to find ingredients that your patient prefer.
```

{format_instructions}

Output:"""}

from langchain.llms import BaseLLM
from langchain import LLMChain, PromptTemplate
import sys
import os
from typing import Dict
sys.path.append(f"{os.path.dirname(__file__)}/../..")
#sys.path.append('../')
from botcore.utils import build_prompt, CheckupMemory, parse_nested_json
from botcore.setup import trace_palm2

def build_food_suggest_chain(model, memory):
    inputs = FOOD_SUGGEST_CONST['inputs']
    outputs = FOOD_SUGGEST_CONST['outputs']
    template = FOOD_SUGGEST_CONST['template']
    prompt = build_prompt(inputs, outputs, template)
    chain = LLMChain(llm=model, prompt=prompt, output_key='result', verbose=True, memory=memory)
    return chain

class BotFoodDoctor:

    def __init__(self, model: BaseLLM):
        self.memory = CheckupMemory(input_key='input')
        self.chain = build_food_suggest_chain(model, self.memory.get())
        self.day = 1
    
    def load_note(self, input: Dict):
        self.note = input

    def checkup(self):
        if self.day == 1:
            human_input = "Hello doctor"
        else:
            human_input = "I have followed your advise"
        inputs = {"time_unit": "week", "timely": "weekly",
                  "day_number": self.day, "input": human_input, **self.note}
        ans = self.chain(inputs)
        data = parse_nested_json(ans['result'])
        self.memory.load_conversation(data['reason'], self.day)
        self.day += 1
        return data

