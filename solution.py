import pandas as pd
import numpy as np


chat_id = 453878141 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    mu = sum(np.log(x - 395) / len(x))
    return mu 
