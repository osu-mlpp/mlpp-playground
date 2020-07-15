import numpy as np


# lex_table: user_id, bm_id, pp, ...
def pp_rank(lex_table, bound_low, bound_high):
    unique_bms = 0
    top_pps = []

    for i in range(bound_low, bound_high):
        if i == bound_high - 1 or lex_table[i][1] != lex_table[i + 1][1]:
            top_pps.append(lex_table[i][2])
            unique_bms += 1

    top_pps.sort(reverse=True)
    performance_score = 0
    multiplier = 1
    for i in range(min(len(top_pps), 100)):
        performance_score += multiplier * top_pps[i]
        multiplier *= .95

    bonus_score = 416.6667 * (1 - (0.9994 ** unique_bms))

    return performance_score + bonus_score


def sigmoid(x, a, b, k):
    j = k * ((1 / (1 + np.exp(-(a * x + b)))) - (1 / (1 + np.exp(-b))))
    return j
