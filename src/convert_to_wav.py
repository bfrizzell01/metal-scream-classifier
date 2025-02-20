import pandas as pd
import os
import click
import sys
import ast
import io
import soundfile as sf


def _bytes_to_wav(raw_audio_data: str, output_dir: str):
    '''
    Given string containing audio bytes and filename (raw_audio_data), 
    store audio as a WAV file in the given output directory (output_dir).
    Returns filename of saved file.
    
    Example
    -------
    >>> raw_data = "{'bytes': b'ID3\\x04\\x00...', 'path': 'SONG.mp3'}"
    >>> bytes_to_wav(raw_data,'data/raw/wavfiles')
    '''
    # parse string as valid dictionary
    audio_data_parsed = ast.literal_eval(raw_audio_data)
    
    # get filename and bytestring from dictionary
    audio_bytes = audio_data_parsed['bytes']
    filename = audio_data_parsed['path'].replace('mp3','wav')
    
    # convert bytes to waveform
    audio_buffer = io.BytesIO(audio_bytes)
    waveform, sample_rate = sf.read(audio_buffer)
    
    # save waveform as WAV file
    output_path = os.path.join(output_dir,filename)
    sf.write(output_path, waveform, sample_rate)
    
    return filename


def convert_data_to_wav(input_path_raw_data: str, output_dir_wav: str, output_path_labels: str):
    '''
    Convert audio byte data stored in raw_data.csv to WAV files.
    Save a dataframe of labels (vocal category) and corresponding filenames
    '''
    
    # read in raw CSV file
    input_path_raw_data = os.path.join(input_path_raw_data)
    audio_data = pd.read_csv(input_path_raw_data, usecols=['audio','scream_type'])
    
    # convert byte data to WAV files, get filenames
    print('converting data to WAV format...')
    audio_data['filename'] = audio_data['audio'].apply(lambda x: _bytes_to_wav(x,output_dir_wav))
    labels = audio_data[['filename','scream_type']]
    print('done')
    print('WAV files saved to ' + output_dir_wav)
    
    print('saving labels and filenames...')
    labels.to_csv(output_path_labels)
    print('labels saved to ' + output_path_labels)
    
@click.command()
@click.option('--input-path-raw',type=str, help="path to input raw data")
@click.option('--output-dir-wav',type=str, help="Path to directory to store wav files")
@click.option('--output-path-labels',type=str, help="Path to label file")
def main(input_path_raw,output_dir_wav,output_path_labels):
    convert_data_to_wav(input_path_raw,output_dir_wav,output_path_labels)
    
if __name__ == '__main__':
    main()