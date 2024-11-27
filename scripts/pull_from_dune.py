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
    query = dune.get_query(id)
    print(f'Processing query {query.base.query_id}, {query.base.name}')
    
    # Save or update the query in the queries folder
    query_file = os.path.join(
        os.path.dirname(__file__), 
        '..', 
        'queries', 
        f'{query.base.name.replace(" ", "_").lower()}___{query.base.query_id}.sql'
    )
    with open(query_file, 'w', encoding='utf-8') as file:
        file.write(f'-- Query name: {query.base.name}\n')
        file.write(f'-- Query ID: {query.base.query_id}\n\n')
        file.write(query.sql)

    print(f'Saved query {query.base.query_id} to {query_file}.')
