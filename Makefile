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

# Convert to wav and create a marker file
data/wav/.done: data/raw/raw_data.csv src/convert_to_wav.py | data/wav
	python src/convert_to_wav.py \
	--input-path-raw=data/raw/raw_data.csv \
	--output-dir-wav=data/wav \
	--output-path-labels=data/raw/labels.csv
	touch data/wav/.done

download-data: data/raw/raw_data.csv data/wav/.done data/raw/labels.csv

clean-data:
	rm -rf data