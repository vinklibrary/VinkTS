import logging
import os
import pathlib
import sys
from urllib import request


def download(url: str, file_path: str):
    """
    Download a file to the given path

    :param url: URL to download
    :param file_path: Where to download the content.
    :return:  None
    """

    def progress(count, block_size, total_size):
        progress_pct = float(count * block_size) / float(total_size) * 100.0
        sys.stdout.write(f"\r Downloading {url} to {file_path} {round(progress_pct,2)}%")
        sys.stdout.flush()

    if not os.path.isfile(file_path):
        opener = request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        request.install_opener(opener)
        pathlib.Path(os.path.dirname(file_path)).mkdir(parents=True, exist_ok=True)
        f, _ = request.urlretrieve(url, file_path, progress)
        sys.stdout.write('\n')
        sys.stdout.flush()
        file_info = os.stat(f)
        logging.info(f"Successfully download {os.path.basename(file_path)} {file_info.st_size} bytes")
    else:
        file_info = os.stat(file_path)
        logging.info(f" File already exists: {file_path} {file_info.st_size} bytes")


def url_file_name(url: str) -> str:
    """
    Extract file name from url

    :param url: URL to extract file name from
    :return:  File Name
    """
    return url.split('/')[-1] if len(url) else ''
