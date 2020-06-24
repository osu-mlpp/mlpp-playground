'''
NOTE: I have converted my .ipynb files to py here, but I recommend you execute these scripts
on a Jupyter notebook, splitting the scripts up into cells as appropriate.

Helper scripts:
sql_connector - Makes retrieving data from dumps more convenient
curve_analysis - Contains plotting methods and lex table methods

Execute scripts in this order to ensure you have the necessary data to move on to the next one:
1. dump_compression.py - converts dumps in npy files
2. aggregate_scores.py - Combines npy files and calculates acc
3. formulas.py - Recalculates user pp entirely, as dump is missing 50% of pp values

Once you have the necessary data by running the scripts above, run sandbox.py, which
will give you a better understanding of the methods in lex.py
'''

# Information about your sql database
SQL_PASSWORD = "password"
SQL_HOST = "localhost"
SQL_USER = "root"
SQL_DB_NAMES = ['random_2019_11_01', 'random_2019_12_01', 'random_2020_01_01', 'random_2020_02_01',
                'random_2020_03_01', 'random_2020_04_01', 'top_2020_04_01']  # Replace with your own db names

# Path where you would like to store data on scores
SCORES_PATH = "./scores/"

# Path where you would like to store processed data
DATA_PATH = "./data/"
