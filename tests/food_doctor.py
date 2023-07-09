import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../")

from botcore.bot.food_doctor import BotFoodDoctor
from botcore.utils import load_example_input
from botcore.setup import trace_palm2

model = trace_palm2()

input_note = load_example_input()
doctor = BotFoodDoctor(model)
doctor.load_note(input_note)

data = doctor.checkup()
print(data)

