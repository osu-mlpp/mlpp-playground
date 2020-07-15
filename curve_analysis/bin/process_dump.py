from curve_analysis.osu_dump import *
from curve_analysis.curve_analysis import *

import numpy as np
from tqdm import tqdm, trange


# Converts sql scores db to 2d numpy table
def to_scores_table(sql_db):
    cursor = sql_db.cursor(buffered=True)
    cnt = 0

    cursor.execute('select * from osu_scores_high')
    scores_high = cursor.fetchall()

    scores_np = np.empty((len(scores_high), len(scores_high[0])), dtype='uint32')

    for i in range(len(scores_high)):
        np_score = row_to_np(scores_high[i])
        if np_score is not None:
            scores_np[cnt] = np_score
            cnt += 1

    return scores_np[:cnt, :]


# Appends 3 columns to a standard scores_table:
# counts: Weighted accuracy score
# max_counts: Maximum possible accuracy score
# acc: Accuracy
def stack_acc_columns(scores_table):
    # calculating accuracy statistics
    max_counts = (scores_table[:, 6] + scores_table[:, 7] + scores_table[:, 8] + scores_table[:, 9]) * 300
    counts = scores_table[:, 6] * 50 + scores_table[:, 7] * 100 + scores_table[:, 8] * 300
    acc = ((counts / max_counts) * 1000000).astype('uint32')

    # adding accuracy columns to table
    return np.hstack((scores_table, np.column_stack((counts, max_counts, acc))))


# Computes all user's pp given a table of scores
# scores_lex: user_id, bm_id, pp, ...
def calc_user_pp(scores_lex):
    score_iter = lex_iterator(scores_lex, 0)
    num_users = len(score_iter) - 1

    pp_table = np.empty((num_users, 2), dtype="uint32")
    for i in trange(num_users):
        low = score_iter[i]
        high = score_iter[i + 1]

        pp_table[i] = [int(scores_lex[low][0]), pp_rank(scores_lex, low, high)]

    return pp_table


# Revises pp table from dump by replacing with recomputed user pp
# scores_lex: user_id, bm_id, pp, ...
# user_lex: user_id, rank_pp, ...
def revise_user_pp(scores_lex, user_lex):
    user_iter = lex_iterator(user_lex, 0)

    pp_dict = {}

    for i in range(len(user_iter) - 1):
        low = user_iter[i]
        high = user_iter[i + 1]

        pp_dict[int(user_lex[low][0])] = user_lex[high - 1][1]

    print('- Recalculating user PP')
    revised_pp_table = calc_user_pp(scores_lex)
    revised_dict = {row[0]: row[1] for row in revised_pp_table}

    # Filling in missing users from user_lex
    print('- Replacing missing users from user_lex')
    for user_id, pp in pp_dict.items():
        if user_id not in revised_dict:
            revised_dict[user_id] = pp

    return np.array([[key, value] for key, value in revised_dict.items()], dtype='uint32')


def permit_save(subject, path, importance=None):
    prefix = '({})'.format(importance) if importance is not None else ''
    print('* {} Save {} in {}? [y/n]:'.format(prefix, subject, path), end=' ')
    return input() == 'y'


if __name__ == '__main__':
    print('CONNECTING TO SQL')
    dump = OsuDB(SQL_DB_NAMES.remove('top_2020_04_01'))

    print('\nCONSTRUCTING AGGREGATED SCORE TABLE')

    print('- Converting ({}) dumps to numpy (This may take a while):'.format(len(dump.dbs)))
    score_tables = []
    for db in tqdm(dump.dbs):
        score_tables.append(to_scores_table(db))

    if permit_save('numpy-converted dumps', SCORES_PATH, 'RECOMMENDED'):
        for i in range(len(score_tables)):
            np.save(SCORES_PATH + dump.names[i] + '.npy', score_tables[i])
    #
    score_tables = []
    for name in dump.names:
        score_tables.append(np.load(SCORES_PATH + name + '.npy'))
    print('- Combining score tables')
    all_scores = np.vstack(tuple(score_tables))

    print('- Appending columns: counts, max_counts, accuracy...')
    all_scores = stack_acc_columns(all_scores)

    if permit_save('aggregated score table', 'SCORES_PATH', 'REQUIRED'):
        np.save(SCORES_PATH + 'all_scores.npy', all_scores)

    print('\nREVISING USER PP VALUES')

    user_stats = np.array(dump.fetch_all('osu_user_stats', ['user_id', 'rank_score']))
    user_lex = lex(user_stats)

    print('- Constructing scores_lex WITH [cols: user_id, bm_id, pp] FROM all_scores')
    scores_lex = all_scores[:, [2, 1, -7]]
    scores_lex = scores_lex.astype('float32')
    scores_lex[:, 2] /= 1000000
    scores_lex = lex(scores_lex)

    u_pp = revise_user_pp(scores_lex, user_lex)

    if permit_save('revised user pp table', 'DATA_PATH', 'REQUIRED'):
        np.save(DATA_PATH + 'u_pp_revised.npy', u_pp)
