import pandas as pd
import numpy as np


chat_id = 706100023 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    from scipy.stats import scist

    n = np.sum(x_success) + np.sum(y_success)
    p1 = np.sum(x_success) / np.sum(x_cnt)
    p2 = np.sum(y_success) / np.sum(y_cnt)
    p = (np.sum(x_success) + np.sum(y_success)) / (np.sum(x_cnt) + np.sum(y_cnt))
    cf = np.sqrt(n) * (p2 - p1) / np.sqrt(p * (1 - p))
    print(cf)

    alpha = 0.02
    df = 1
    critical_value = scist.ppf(1 - alpha, df)
    print(critical_value)

    if cf > critical_value:
        rez = 1 #
    else:
        rez = 0 #
    return bool(rez)
