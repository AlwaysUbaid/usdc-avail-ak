import os
import yaml
from dune_client.client import DuneClient
from dotenv import load_dotenv
import sys
import codecs

# Set the default encoding to UTF-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# Initialize Dune client
dune = DuneClient.from_env()

# Load queries.yml
queries_yml = os.path.join(os.path.dirname(__file__), '..', 'queries.yml')
with open(queries_yml, 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)

query_ids = [query['id'] for query in data['queries']]

for id in query_ids:
    queries_path = os.path.join(os.path.dirname(__file__), '..', 'queries')
    files = os.listdir(queries_path)
    found_files = [file for file in files if str(id) in file.split('___')[-1].split('.')[0]]
    
    if found_files:
        query_file = os.path.join(queries_path, found_files[0])
        with open(query_file, 'r', encoding='utf-8') as file:
            query_sql = file.read()

        # Update the query on Dune
        dune.update_query(query_id=id, query_sql=query_sql)
        print(f'Updated query {id} on Dune.')
    else:
        print(f'Query file for ID {id} not found.')
