import os
import pandas as pd
from sqlalchemy import create_engine
from database import get_db_connection
from process_data import process_data

def load_data(file_path):
    df = pd.read_csv(file_path)
    engine = get_db_connection()
    df.to_sql('vehicle_data', engine, if_exists='append', index=False)

def main():
    raw_data_dir = 'data/raw/'
    processed_data_dir = 'data/processed/'
    
    for file_name in os.listdir(raw_data_dir):
        file_path = os.path.join(raw_data_dir, file_name)
        df = pd.read_csv(file_path)
        processed_df = process_data(df)
        processed_file_path = os.path.join(processed_data_dir, file_name)
        processed_df.to_csv(processed_file_path, index=False)
        load_data(processed_file_path)

if __name__ == "__main__":
    main()
