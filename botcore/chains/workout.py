WORKOUT_SUGGEST_CHAIN = \
{"inputs":["time_unit", "timely", 'medical_record', 'health_goal', 'timeline', 'eating_habit'],
 "template": """You are a professional personal trainner.
  
 You have noted your customer's history medical record, eating habits and health goals.
Medical record: {medical_record}.
Eating habits: {eating_habit}.
Health goals: {health_goal}.

Mission: Based on what you have noted, please plan the next {time_unit} workout routine for {timeline}.
Requirements: You must adhere to the requirements listed in triple backquotes.
```
The workout routine should contain easy to do exercises that can be done at home.
You should note in mind your customer's health goals, in order to devise a suitable workout plan.
You should check carefully your customer's medical record before making any decision. Avoid including any exercises that your customer should not do.
```

Desired Format: Each {timely} workout routine output should follow the below format.

# {time_unit}_number: 
EXERCISE: <comma_separated_list_of_no_more_than_five_exercises_that_can_be_done_at_home>
DESC: <a_description_including_each_exercise's_health_usage_of_{time_unit}_number_workout_routine>
TARGET: <a_target_for_{time_unit}_number_workout_routine>

Output:"""}

from langchain import LLMChain, PromptTemplate
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../..")

def build_workout_suggest_chain(model, debug = False):
    inputs = WORKOUT_SUGGEST_CHAIN['inputs']
    template = WORKOUT_SUGGEST_CHAIN['template']
    prompt = PromptTemplate(input_variables=inputs, template=template)
    chain = LLMChain(llm=model, prompt=prompt, output_key='result', verbose=debug)
    return chain

