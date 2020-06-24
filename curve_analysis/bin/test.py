import numpy as np
from curve_analysis.bin.config import DATA_PATH, SCORES_PATH
from curve_analysis.curve_analysis import lex_bounds, lex
import matplotlib.pyplot as plt

from curve_analysis.osu_dump import OsuDB
from curve_analysis.bin.process_dump import to_scores_table

dump = OsuDB(['random_2019_11_01'])
a = to_scores_table(dump.dbs[0])
np.save(SCORES_PATH + 'random_2019_11_01.npy', a)


