from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain import PromptTemplate, LLMChain
import json
from typing import List, Dict
from langchain.memory import ConversationBufferMemory


def load_sample_input():
    data_1 = {"medical_record": "No chronic diseases or food allergies.",
            "eating_habit": "Likes fast food and quick-prep meals but wants to switch to a healthier eating regimen",
            "health_goal": "Weight loss and improving overall cardiovascular health.",
            "timeline": "2 to 3 months."}

    return data_1

def parse_nested_json(text: str) -> Dict:
    a = text.strip()
    json_data = a.strip().replace('```json', '').strip()
    json_data = json_data.strip().replace('```', '').strip()
    data = json.loads(json_data)
    return data


def build_prompt(inputs:list, outputs:dict, template:str, include_parser: bool = True) -> PromptTemplate:
    response_schema = [ResponseSchema(name=k, description=outputs[k])\
            for k in outputs]
    output_parser = StructuredOutputParser.from_response_schemas(response_schema)
    format_instructions = output_parser.get_format_instructions()
    if include_parser:
        prompt = PromptTemplate(template=template, input_variables=inputs,\
                          output_parser=output_parser,\
                          partial_variables={"format_instructions": format_instructions})
    else:
        prompt = PromptTemplate(template=template, input_variables=inputs,\
                          partial_variables={"format_instructions": format_instructions})
    return prompt



class QAMemory():

    def __init__(self, input_key: str = 'problem'):

        self.memory = ConversationBufferMemory(memory_key="chat_history", input_key=input_key)
             
    
    def load_qa_to_memory(self, questions: List[str], answers: List[str]):
        for q, a in zip(questions, answers):
            self.memory.chat_memory.add_ai_message(q)
            self.memory.chat_memory.add_user_message(a)
        return True
    
    def load_all(self, product: str, questions: List[str], answers: List[str]):
        self.load_product_context(product)
        self.load_qa_to_memory(questions, answers)
        print("Load done")
    
    def load_product_context(self, problem: str):
        symptomp = problem.strip() 
        message = f"I having a problem. {symptomp}."
        self.memory.chat_memory.add_user_message(message)



def load_sample_qa():
    problem = "Eating peanuts made my face swollen."
    data = {'chain': 'checkup',
 'questions': [{'question': 'What other foods have you eaten recently?',
   'answerOptions': ['Peanuts',
    'Tree nuts',
    'Seafood',
    'Dairy',
    'Eggs',
    'Gluten',
    'Soy',
    'Other']},
  {'question': 'Have you had any other symptoms besides swelling?',
   'answerOptions': ['Hives',
    'Diarrhea',
    'Nausea',
    'Vomiting',
    'Chest pain',
    'Shortness of breath',
    'Other']},
  {'question': 'How long did it take for your symptoms to start after eating the peanuts?',
   'answerOptions': ['Less than 1 hour',
    '1-2 hours',
    '2-4 hours',
    '4-8 hours',
    '8-12 hours',
    'More than 12 hours']},
  {'question': 'How severe were your symptoms?',
   'answerOptions': ['Mild', 'Moderate', 'Severe']},
  {'question': 'Have you had any previous allergic reactions?',
   'answerOptions': ['Yes', 'No']},
  {'question': 'Do you have any family history of allergies?',
   'answerOptions': ['Yes', 'No']}]}

    questions = [q['question'] for q in data['questions']]
    answers = [q['answerOptions'][0] for q in data['questions']]
    return problem, questions, answers



