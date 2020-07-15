import numpy as np
import pandas as pd

from curve_analysis.curve_analysis.lex import lex_bounds


# Generates a list of (pp, score) data points from plays on a beatmap
# score_col: column in lex_table to be used as score
def bm_data(lex_table, user_lex, bm_id, score_col):
    data = []
    bm_bounds = lex_bounds(lex_table, [bm_id])
    for i in range(bm_bounds[0], bm_bounds[1]):
        play = lex_table[i]
        user_ix = lex_bounds(user_lex, [play[1]])[0]
        user_pp = user_lex[user_ix][1]
        score = play[score_col]

        data.append([user_pp, score])

    data.sort(key=lambda x: x[0])
    data = np.array(data)

    return data


# Bin beatmap data points by non-overlapping pp ranges
def bin_by_pp(data, minimum, maximum, step):
    bins = np.arange(minimum, maximum + step, step)
    intervals = pd.cut(data[:, 0], bins)
    ret = [[] for i in range(len(bins) - 1)]
    for i in range(len(data)):
        if str(intervals[i]) != 'nan':
            ix = int(intervals[i].left / step)
            ret[ix].append(data[i][1])
    return ret, bins


# Efficiently computes proportion of successful plays (score > min_score) in each pp range
# Complexity - O(N + 2M) [N: len(data), M: len(pp_ranges)]
def proportion_curve(data, pp_ranges, min_score):
    pp = data[:, 0]
    scores = data[:, 1]

    cuts = np.empty((len(pp_ranges) * 2, 2))
    for i in range(len(pp_ranges)):
        cuts[i * 2] = [pp_ranges[i][0], i]
        cuts[i * 2 + 1] = [pp_ranges[i][1], - (i + 1)]

    cuts = cuts[cuts[:, 0].argsort()]
    cuts = np.vstack([cuts, [0, 0]])
    ret = np.zeros((len(pp_ranges), 2))
    starts = set()
    score_i = 0

    passes = 0
    total = 0

    for i in range(len(cuts) - 1):
        range_i = int(cuts[i][1])
        pp_next = cuts[i + 1][0]

        if range_i < 0:
            range_i = - (range_i + 1)
            starts.remove(range_i)
            ret[range_i] += [passes, total]
        else:
            starts.add(range_i)
            ret[range_i] = -np.array([passes, total])

        while score_i < len(pp) and pp[score_i] < pp_next:
            if scores[score_i] >= min_score:
                passes += 1
            total += 1
            score_i += 1

    return ret
