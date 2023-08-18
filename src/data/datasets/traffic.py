
from src.data.common import TsDataset
import os
import logging
from common.http_utils import download, url_file_name
import patoolib
import numpy as np

class TrafficTsDataset(TsDataset):
    def __init__(self, root:str=None):
        # super().__init__(None, None, None)
        self.root = root
        self.download_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00204/PEMS-SF.zip'
        self.download(self.root, self.download_url)



    def download(self, root, url):
        if os.path.isdir(root):
            logging.info(f"the {root} directory already exists.")
        download(url, os.path.join(root, url_file_name(url)))
#         下载后需要对数据进行解压
        patoolib.extract_archive( os.path.join(root, url_file_name(url)), outdir=root)

        with open(os.path.join(root, 'PEMS_train'), 'r') as f:
            train_raw_data = f.readlines()
        with open(os.path.join(root, 'PEMS_test'), 'r') as f:
            test_raw_data = f.readlines()
        with open(os.path.join(root, 'randperm'), 'r') as f:
            permutations = f.readlines()
        permutations = np.array(permutations[0].rstrip()[1:-1].split(' ')).astype(np.int)
        raw_data = train_raw_data +test_raw_data



if __name__ == '__main__':
    trafficTsDataset = TrafficTsDataset("./datasets/traffic/")
    print('test successful')