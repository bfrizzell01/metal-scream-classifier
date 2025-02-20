import pandas as pd
import os
import click
import sys
import ast
import io
import soundfile as sf


def download_raw_data(output_path_raw):
    '''
    Download raw data from HuggingFace to given path
    '''
    
    print('downloading data from HuggingFace...')
    file_path = "hf://datasets/jpdiazpardo/scream_detection_heavy_metal/data/train-00000-of-00001-a72775dc16841570.parquet"
    df = pd.read_parquet(file_path)[['audio','scream_type','song_name','band_name']]
    print('done')
    
    print('Saving to CSV...')
    df.to_csv(output_path_raw)
    print('done')
    print('Saved data to ' + output_path_raw)
    
@click.command()
@click.option('--output-path-raw', type=str, help="Path to store raw data")  
def main(output_path_raw: str):
    download_raw_data(output_path_raw)
    
if __name__ == '__main__':
    main()