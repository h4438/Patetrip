FOOD_SUGGEST_CONST = \
{"inputs":["time_unit", "timely", "timeline", 'medical_record', 'eating_habit', 'health_goal'],
 "outputs": {"ingredients": "a js array of food ingredients for the diet plan. The length of the array should not be larger than 5.",
             "reason": "a description including each ingredient's health usage."},
 "template": """You are a nutrition doctor.
  
 You have noted your patient's history medical record, eating habits and health goals.
Medical record: {medical_record}.
Eating habits: {eating_habit}.
Health goals: {health_goal}.


Mission: Based on what you have noted, please make a {timely} diet plan for {timeline}.
Requirement: You must adhere to the requirements listed in triple backquotes.
```
The {timely} diet plan for each {time_unit} should list the food ingredients. 
You should note in mind your patient's health goals, in order to devise a suitable diet plan.
You should check carefully your patient's medical record before making any decision. Avoid including any thing that cause food allergy to your patient.
You should check carefully your patient's eating habit before making any decision. Try to find ingredients that your patient prefer.
```

Desired Format: Each {timely} diet plan output should follow the below format.

# {time_unit}_number: 
FOOD: <comma_separated_list_of_no_more_than_five_food_ingredients>
DESC: <a_description_including_each_ingredient's_health_usage_of_{time_unit}_number_diet_plan>
TARGET: <a_target_for_{time_unit}_number_diet_plan>


Output:"""}

from langchain import LLMChain, PromptTemplate
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../..")

def build_food_suggest_chain(model, debug = True):
    inputs = FOOD_SUGGEST_CONST['inputs']
    template = FOOD_SUGGEST_CONST['template']
    prompt = PromptTemplate(input_variables=inputs, template=template)
    chain = LLMChain(llm=model, prompt=prompt, output_key='result', verbose=debug)
    return chain
