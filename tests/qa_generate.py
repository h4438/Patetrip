import sys
import os
from pprint import pprint as ppt

sys.path.append(f"{os.path.dirname(__file__)}/../")
from botcore.chains.qa_allergen import build_qa_allergen_chain
from botcore.setup import trace_palm2
from botcore.utils import parse_nested_json

def sample_use():
    chain = build_qa_allergen_chain(session='qa_gen_pate')
    problem = "My legs are hurt and I can't bend them, after I ate goat meat."
    ans = chain({"problem": problem})
    data = parse_nested_json(ans['result'])
    ppt(data)
    
if __name__ == '__main__':

    sample_use()

