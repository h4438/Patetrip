ASK_ALLERGEN_CONST = \
{"inputs":["problem"],
 "outputs": {"chain": "return 'checkup'.","questions": """a js array of questions accompanied by a list of no more than 4 answer options for each question."""},
 "template": """You are a food allergist.
Your patient is having a problem: {problem}.

Your job is trying to determine what allergens are causing your patient's problem. 
You will need to ask questions which can help you confidently identify what allergens are causing your user problem.
Each question asked should be accompanied by a list of answer options.

{format_instructions}

Questions:"""}

from langchain.llms import BaseLLM
from langchain import LLMChain
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../..")
from botcore.utils import build_prompt

def build_qa_generate_chain(model: BaseLLM):
    inputs = ASK_ALLERGEN_CONST['inputs']
    outputs = ASK_ALLERGEN_CONST['outputs']
    template = ASK_ALLERGEN_CONST['template']
    prompt = build_prompt(inputs, outputs, template, include_parser=True)
    chain = LLMChain(llm=model, prompt=prompt, output_key='result')
    return chain
