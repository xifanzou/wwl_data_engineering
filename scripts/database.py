import json
import os
from sqlalchemy import create_engine

def get_db_connection():
    with open('config/db_config.json') as f:
        config = json.load(f)
    db_string = f"postgresql://{config['user']}:{config['password']}@{config['host']}/{config['dbname']}"
    print(f"Connected to database: {config['dbname']}")
    return create_engine(db_string)

