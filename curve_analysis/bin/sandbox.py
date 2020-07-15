from curve_analysis.curve_analysis import *
from curve_analysis.osu_dump import OsuDB
from curve_analysis.bin.config import DATA_PATH, SCORES_PATH

import numpy as np
import matplotlib.pyplot as plt
from pygam import PoissonGAM, LinearGAM, s, f
from scipy.optimize import curve_fit

if __name__ == '__main__':
    dump = OsuDB()

    print('EXTRACTING FROM DATA SETS')
    beatmaps = lex(np.array(dump.fetch_all('osu_beatmaps', ['beatmap_id', 'difficultyrating'])))

    print('- Generating lex tables for user scores & user pp')
    all_scores = np.load(SCORES_PATH + 'all_scores.npy')
    u_pp_lex = lex(np.load(DATA_PATH + 'u_pp_revised.npy'))

    acc_scores = all_scores[:, [-9, 1, 2, -1]]  # cols: mods, bm_id, user_id, acc
    acc_scores = lex(acc_scores)

    print('- Subsetting NM scores')
    acc_scores_subset = np.concatenate((lex_2d(lex_bounds(acc_scores, [0], get="all")),
                                        lex_2d(lex_bounds(acc_scores, [1], get="all"))), axis=0)
    acc_scores_subset = acc_scores_subset[:, 1:4]

    acc_scores_subset = acc_scores_subset.astype('float32')
    acc_scores_subset[:, 2] /= 1000000  # converting pp * 10^6 back to float pp
    acc_scores_subset = lex(acc_scores_subset)

    print('- Finding beatmaps w/ most samples')
    bm_samples = freq_keys(acc_scores_subset)[:100]

    N = 1000
    x = np.arange(0, 16000 - N)

    print('\nPLOTTING BEATMAPS')
    for bm_id in bm_samples[:10, 0]:
        stars = lex_bounds(beatmaps, [bm_id], get="one")[1]
        ranges = [[i, i + N] for i in range(0, 16000 - N)]
        data = bm_data(acc_scores_subset, u_pp_lex, bm_id, 2)

        prop_curve = proportion_curve(data, ranges, .95)

        plt.figure(figsize=(15, 6))
        plt.plot(np.arange(0, 16000 - N), prop_curve[:, 1])
        plt.show(block=False)

        prop_curve[prop_curve[:, 1] == 0] = -1
        props = prop_curve[:, 0] / prop_curve[:, 1]
        props = np.column_stack((x, props))
        props = props[prop_curve[:, 1] > 20].T

        plt.figure(figsize=(15, 6))

        plt.plot(props[0], props[1])

        # Choose a curve fitting method (Sigmoid only works on > 5* maps):

        # Curve fitting with pyGAM
        gam = LinearGAM(s(0, n_splines=13, constraints='monotonic_inc')).fit(props[0], props[1])
        plt.plot(x, gam.predict(x))

        # Curve fitting with sigmoid
        # popt, pcov = curve_fit(sigmoid, props[0], props[1], p0=[-.001, 1, -1])
        # a, b, k = popt
        # median = - b / a
        # plt.plot(x, sigmoid(x, *popt))
        # print('{} - Median: {}'.format(int(bm_id), median))

        plt.xlabel('Total PP')
        plt.ylabel('% Players')

        plt.title('{} ({:.1f}*): Proportion of players w/ 90% acc'.format(int(bm_id), stars))
        plt.show()
