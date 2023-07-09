import sys
import os
from pprint import pprint as ppt
sys.path.append(f"{os.path.dirname(__file__)}/../")
from botcore.utils import load_sample_qa, QAMemory

def sample_use():
    p, q, a = load_sample_qa()
    memory = QAMemory()
    memory.load_all(p, q, a)
    print(memory.memory)

if __name__ == '__main__':
    sample_use()

