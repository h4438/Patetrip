WORKOUT_SUGGEST_CHAIN = \
{"inputs":["chat_history", "time_unit", "timely", "day_number", 'medical_record', 'health_goal', 'timeline', 'input'],
 "outputs": {"exercises": "a js array of excercises for the workout routine.",
             "frequency": "a js array of each excercise frequency.",
             "description": "a description including the health usage of each excercise."},
 "template": """You are a professional personal trainner.
 
 You have {timely} checkup with your customer and today is day number {day_number}.
 {chat_history}
 
 Your customer response to you: "{input}".
 
 You have noted your customer's history medical record and health goals.
Medical record: {medical_record}.
Health goals: {health_goal}.

Mission: Based on what your customer have told and what you have advised so far, please plan the next {time_unit} workout routine for your customer.
Requirements: You must adhere to the requirements listed in triple backquotes.
```
The workout routine should contain easy to do exercises that can be done at home.
You should note in mind your customer's health goals, in order to devise a suitable workout plan.
You should check carefully your customer's medical record before making any decision. Avoid including any exercises that your customer should not do.
Your workout routine should be fully thought and well planned so that your customer can achieve the health goal in {timeline} provided that your customer do the routine {timely}. 
```

{format_instructions}

Output:"""}

from langchain import LLMChain
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../..")
from botcore.utils import build_prompt

def build_workout_suggest_chain(model, memory, debug=False):
    inputs = WORKOUT_SUGGEST_CHAIN['inputs']
    outputs = WORKOUT_SUGGEST_CHAIN['outputs']
    template = WORKOUT_SUGGEST_CHAIN['template']
    prompt = build_prompt(inputs, outputs, template)
    chain = LLMChain(llm=model, prompt=prompt, output_key='result', verbose=debug, memory=memory)
    return chain
