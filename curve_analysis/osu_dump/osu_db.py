# Go ahead and replace db_names with how you named your dumps. Make sure it's in the same order
# Each dump should still start with osu_ ex. osu_random_2019_11_01
from curve_analysis.bin.config import *

import mysql.connector
from tqdm import tqdm


class OsuDB:
    password = SQL_PASSWORD
    host = SQL_HOST
    user = SQL_USER

    def __init__(self, names=None):
        self.dbs = []
        if names is None:
            self.names = SQL_DB_NAMES
        else:
            self.names = names

        for db_name in self.names:
            self.dbs.append(self.connect_db('osu_' + db_name))

    def connect_db(self, name):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            database=name
        )

    # Creates a 'super' table by combining calls on OsuDB.fetch for all dbs
    def fetch_all(self, table_name, columns=None):
        ret = []
        print('- Fetching {} from ({}) dumps'.format(columns, len(self.dbs)))
        for db in tqdm(self.dbs):
            table = OsuDB.fetch(db, table_name, columns)
            ret.extend(table)

        return ret

    # Takes a subset of columns from a table in db
    @staticmethod
    def fetch(db, table_name, columns=None):
        selection = '* '
        if columns is not None:
            selection = ''
            for i in range(len(columns)):
                selection += columns[i] + (', ' if i + 1 != len(columns) else ' ')

        cur = db.cursor(buffered=True)
        cur.execute('select ' + selection + 'from ' + table_name)
        return cur.fetchall()
