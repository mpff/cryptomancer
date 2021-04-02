import dotenv
dotenv.load_dotenv()

import os
import click
import logging

import requests
import re
import zipfile


def parse_google_drive_url(source_url):
    results = re.search('file/d/(.*)/', source_url)
    return results.group(1)

def download_file_from_google_drive(gdid, ofile):
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params = { 'id' : gdid }, stream = True)
    token = get_confirm_token(response)
    if token:
        params = { 'id' : gdid, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)
    save_response_content(response, ofile)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, ofile):
    CHUNK_SIZE = 32768
    with open(ofile, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)


@click.command()
@click.argument('source_url')
@click.argument('output_dir', type=click.Path(exists=True))
def download_dataset(source_url, output_dir):
    """ Downloads and unzips historical Bitcoin market data from Kraken's
        official Google Drive folder.

        source_url :  Google Drive URL to historical XTC data
        output_dir :  Directory for raw data
    """
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logger = logging.getLogger(__name__)

    logger.info('Parsing Google Drive URL.')
    gdid = parse_google_drive_url(source_url)
    logger.info(f'Google Drive ID is {gdid}.')

    logger.info('Downloading source file.')
    source_file = os.path.join(output_dir, 'source.zip')
    download_file_from_google_drive(gdid, source_file)

    logger.info('Unzipping source file.')
    with zipfile.ZipFile(source_file, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

    logger.info('Removing zip file.')
    os.remove(source_file)

    logger.info(f'Finished. Files are in {output_dir}.')
