import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../")

from langchain.tools import DuckDuckGoSearchRun
from langchain.llms import BaseLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
# my code
from botcore.setup import trace_palm2
from botcore.utils import parse_nested_json, build_prompt

def build_list_chain(MODEL: BaseLLM) -> LLMChain:
    inputs = ['para','country']
    outputs = {"chain": "always return 'find_food'",
               "food": "a js array of all the dishes in the given paragraph.",
               "desc": "a js array of dish descriptions. These descriptions must be short and concise."}
    TEMPLATE = """You are a {country} person. Given a paragraph about Vietnam's signature dishes delimited by triple backquotes.
    ```
    {para}
    ```
    Please do your best to complete the task as instructed.
    {format_instructions}
    Answer:"""
    
    prompt = build_prompt(inputs, outputs, TEMPLATE)
    chain = LLMChain(llm=MODEL, prompt=prompt, output_key='result')
    return chain

class FoodFinder:

    def __init__(self, model: BaseLLM):
        self.search_tool = DuckDuckGoSearchRun()
        self.chain = build_list_chain(model)
        print("Food finder is ready")

    def find(self, place: str):
        geo_place = place.strip()
        prompt = f"Top signature dishes in {geo_place}."
        print(f"Searching {prompt}")
        paragraph = self.search_tool(prompt)
        ans = self.chain({"para": paragraph, "country":geo_place})
        return parse_nested_json(ans['result'])
