import numpy as np

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


# datetime to unix seconds
def unix_time_seconds(dt):
    return (dt - epoch).total_seconds()


# converts osu score sql row into uint32 numpy
def row_to_np(sql_row):
    try:
        ret = np.asarray(sql_row)
        ret[5] = ord(ret[5][0]) - ord('A')  # score rank to numeric
        ret[14] = unix_time_seconds(ret[14])  # datetime to unix seconds
        country = ret[-1].decode()  # from byte to country initials
        ret[-1] = (ord(country[0]) - ord('A')) * 26 + ord(country[1]) - ord('A')  # country to numeric
        ret[-4] = ret[-4] * 1000000  # Keeping 6 decimal accuracy of float pp by storing pp * 10^6
        return ret.astype('uint32')
    except:
        return None  # row format didn't match

