import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 938988157 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.02
    
    w = y_success / y_cnt
    p0 = x_success / s_cnt
    denom = (p0 * (1 - p0)) ** 0.5
    
    U = ((w - p0) * y_cnt**0.5) / denom
    
    Ucr = norm.ppf(1/2 - alpha
    
    return U >= Ucr
