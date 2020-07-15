'''
INSTRUCTIONS

1. Download dumps, and create a database for each in mysql
2. Replace sql information below, and set paths for storage (minimum 5 GB)
3. Run process_dump.py. REQUIRED files must be saved to continue
4. Run sandbox.py, then feel free to mess around

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
