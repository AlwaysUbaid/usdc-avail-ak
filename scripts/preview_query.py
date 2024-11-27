import os
from dune_client.client import DuneClient
from dotenv import load_dotenv
import sys
import pandas as pd

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# Initialize Dune client
dune = DuneClient.from_env()

# Get query ID from the command line
id = sys.argv[1]

# Path to queries folder
queries_path = os.path.join(os.path.dirname(__file__), '..', 'queries')
files = os.listdir(queries_path)
found_files = [file for file in files if str(id) in file.split('___')[-1].split('.')[0]]

if len(found_files) != 0:
    query_file = os.path.join(queries_path, found_files[0])

    print(f'Previewing query {id}...')

    with open(query_file, 'r', encoding='utf-8') as file:
        query_text = file.read()

    # Run the query
    results = dune.run_sql(f'SELECT * FROM ({query_text}) LIMIT 20')
    results_df = pd.DataFrame(data=results.result.rows)

    print(results_df.head(20))
else:
    print('Query ID not found.')
