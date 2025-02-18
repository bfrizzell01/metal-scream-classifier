import pandas as pd
import os
import click



def load_scream_data(output_dir):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"The directory {output_dir} was created.")
    
    file_path = "hf://datasets/jpdiazpardo/scream_detection_heavy_metal/data/train-00000-of-00001-a72775dc16841570.parquet"
    print('loading data...')
    df = pd.read_parquet(file_path)[['audio','scream_type','song_name','band_name']]
    print('done',sep=' ')
    print('saving to CSV...')
    df.to_csv(output_dir+'/scream_data.csv')
    print('done',sep=' ')
    print('Saved data to '+output_dir+'/scream_data.csv')
    
@click.command()
@click.option('--output-dir', type=str, help="Path to raw output data")  
def main(output_dir: str):
    load_scream_data(output_dir)
    
if __name__ == '__main__':
    main()