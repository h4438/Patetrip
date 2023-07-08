import sys
import os
from pprint import pprint as ppt

sys.path.append(f"{os.path.dirname(__file__)}/../")
from botcore.chains.qa_generate import build_qa_generate_chain
from botcore.setup import trace_palm2
from botcore.utils import parse_nested_json

def sample_use():
    model = trace_palm2()
    chain = build_qa_generate_chain(model)
    problem = "My legs are hurt and I can't bend them, after I ate goat meat."
    ans = chain({"problem": problem})
    data = parse_nested_json(ans['result'])
    ppt(data)
    
if __name__ == '__main__':

    sample_use()

