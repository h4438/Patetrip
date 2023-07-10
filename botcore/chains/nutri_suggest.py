FOOD_SUGGEST_CONST = \
{"inputs":["chat_history", "time_unit", "timely", "day_number",'medical_record', 'eating_habit', 'health_goal', 'input'],
 "outputs": {"ingredients": "a js array of food ingredients for the diet plan. The length of the array should not be larger than 5.",
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
The {timely} diet plan should list the food ingredients that are used in each meal.
You should note in mind your patient's health goals, in order to devise a diet plan.
You should check carefully your patient's medical record before making any decision. Avoid including any thing that cause food allergy to your patient.
You should check carefully your patient's eating habit before making any decision. Try to find ingredients that your patient prefer.
```

{format_instructions}

Output:"""}

from langchain import LLMChain
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../..")
from botcore.utils import build_prompt

def build_nutri_suggest_chain(model, memory, debug=False):
    inputs = FOOD_SUGGEST_CONST['inputs']
    outputs = FOOD_SUGGEST_CONST['outputs']
    template = FOOD_SUGGEST_CONST['template']
    prompt = build_prompt(inputs, outputs, template)
    chain = LLMChain(llm=model, prompt=prompt, output_key='result', verbose=debug, memory=memory)
    return chain

