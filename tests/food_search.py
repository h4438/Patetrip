import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../")
from botcore.setup import trace_palm2
from botcore.food_search import FoodFinder
from pprint import pprint as ppt

def sample_use():
    model = trace_palm2(session='food_search', max_tokens=200)
    food_finder = FoodFinder(model)
    data = food_finder.find("South Vietnam")
    ppt(data)

if __name__ == '__main__':
    sample_use()
