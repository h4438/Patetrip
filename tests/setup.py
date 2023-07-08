import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../")
from botcore.setup import trace_palm2

model = trace_palm2(session='food_search')

print(model)
