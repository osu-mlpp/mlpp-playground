import numpy as np

"""
Make sure you understand this section well, otherwise you won't be able to efficiently access the
score data from the numpy files generated. The idea is to lexicographically sort
the rows of the numpy scores table like how a dictionary works. This enables quick lookups
for specific subsets or single scores.
"""


# converts 2d table to lex table (1d array of sortable tuples, with each tuple being a score)
def lex(np_table):
    data = np_table[np.lexsort(np.rot90(np_table, 1))]
    dt = [('', data.dtype) for i in range(data.shape[1])]
    return np.ascontiguousarray(data).view(dt).squeeze(-1)


# reverts from lex table to 2d table
def lex_2d(lex_table):
    return lex_table.view(dtype=lex_table.dtype[0]).reshape(-1, len(lex_table.dtype))


# Lexicographic binary searches a subset of rows from a lex table
# get = 'all': copies all rows in subset to a new lex table
# get = 'one': returns first row in subset
def lex_bounds(lex_table, dmin, dmax=None, get=None):
    if dmax is None:
        dmax = dmin.copy()
        dmax[-1] += 1

    cols = len(lex_table[0])

    low = np.zeros((cols,))
    low[:len(dmin)] = dmin

    high = np.zeros((cols,))
    high[:len(dmax)] = dmax

    low = np.searchsorted(lex_table, np.array(tuple(low), lex_table.dtype))
    high = np.searchsorted(lex_table, np.array(tuple(high), lex_table.dtype))
    if get:
        if lex_2d(lex_table[low:low + 1])[0, 0:len(dmin)] == dmin:
            if get == "all":
                return lex_table[low:high]
            elif get == "one":
                return lex_table[low]
    else:
        return low, high

    return None


# Iterates across all unique keys in column (col) of a lex table
def lex_iterator(lex_table, col):
    ret = []
    i = 0
    while i != lex_table.shape[0]:
        bound_low, bound_high = lex_bounds(lex_table, [lex_table[i][col]])
        ret.append(bound_low)
        i = bound_high

    ret.append(lex_table.shape[0])
    return np.array(ret)


# Returns unique keys in first column of lex table, sorted by frequency
def freq_keys(lex_table):
    score_iterator = lex_iterator(lex_table, 0)
    ret = np.zeros((len(score_iterator) - 1, 2))

    for i in range(len(ret)):
        low = score_iterator[i]
        high = score_iterator[i + 1]
        ret[i] = [lex_table[int(low)][0], high - low]

    return ret[ret[:, 1].argsort()[::-1]]
