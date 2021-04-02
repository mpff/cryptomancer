# Cryptomancer
A RNN model to predict Bitcoin spot price..

## Getting started
Create a virtual environment, install the requirements and the package in
editable mode.
```
$ python3 -m venv virtualenv
$ source virtualenv/bin/activate
$ pip install -r requirements.txt
$ pip install --editable .  
```
Download Krakens historical Bitcoin market data. Get an up-to-date URL from the [Kraken Website](https://support.kraken.com/hc/en-us/articles/360047543791-Downloadable-historical-market-data-time-and-sales-).
```
$ download_dataset
https://drive.google.com/file/d/1hbpD9_HB7fuGbXu6ZAAcvMkpbxMgOkld/view?usp=sharing
data/input
```

