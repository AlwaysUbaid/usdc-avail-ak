import os
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

# Path to uploads folder
uploads_path = os.path.join(os.path.dirname(__file__), '..', 'uploads')
files = os.listdir(uploads_path)

if len(files) == 0:
    print("No files to upload.")
    exit()

# Process each CSV file
for file in files:
    if not file.endswith(".csv"):
        continue
    file_name = file.split(".")[0].lower().replace(' ', '_')
    with open(os.path.join(uploads_path, file), 'r') as file:
        table = dune.upload_csv(
            data=str(file.read()),
            table_name=file_name,
            is_private=False
        )
        print(f'Uploaded table "{file_name}".')
