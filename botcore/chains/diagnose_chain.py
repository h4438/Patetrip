ALLERGEN_DIAGNOSE_CONST = \
{"inputs":["problem", "chat_history"],
 "outputs": {"chain": "return 'diagnose'.",
             "allergens": "a js array of allergens.",
             "reason": "a explanation for your diagnose.", 
             "guide": "a helpful guide to avoid the problem and also point out mistake that your patient is making."},
 "template": """You are a food allergist and you have asked your patient some questions about the problem "{problem}".
 {chat_history}

Mission: Based on what your patient have told, please diagose the allergen (or allergens) that causing the problem and explain the reason.

{format_instructions}

Output:"""}

from langchain.llms import BaseLLM
from langchain import LLMChain
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../..")
from botcore.utils import build_prompt
from botcore.setup import trace_palm2

def build_allergen_diagnose_chain(model: BaseLLM, memory):
    inputs = ALLERGEN_DIAGNOSE_CONST['inputs']
    outputs = ALLERGEN_DIAGNOSE_CONST['outputs']
    template = ALLERGEN_DIAGNOSE_CONST['template']
    prompt = build_prompt(inputs, outputs, template, include_parser=True)
    chain = LLMChain(llm=model, prompt=prompt, output_key='result', verbose=True, memory=memory)
    return chain

