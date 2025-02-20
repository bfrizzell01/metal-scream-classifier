.PHONY: download_data clean-data


data/raw:
	mkdir -p data/raw

data/wav:
	mkdir -p data/wav

# download raw data
data/raw/raw_data.csv: src/download_data.py
	$(MAKE) data/raw
	python src/download_data.py \
	--output-path-raw=data/raw/raw_data.csv

# convert byte data to wav files
data/wav/* data/raw/labels.csv: data/raw/raw_data.csv src/convert_to_wav.py
	$(MAKE) data/wav
	python src/convert_to_wav.py \
	--input-path-raw=data/raw/raw_data.csv \
	--output-dir-wav=data/wav \
	--output-path-labels=data/raw/labels.csv

download-data: data/raw/raw_data.csv data/raw/labels.csv data/wav/*

clean-data:
	rm -rf data