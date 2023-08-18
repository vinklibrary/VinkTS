from . import Dataset, DataEntry, DataBatch

import pandas as pd

class TsDataset():
    def __init__(self,
                 data: pd.DataFrame = None,
                 target_col: str = None,
                 ts_col: str = None
                 ):
        self.data = data
        self.target_col = target_col
        self.ts_col = ts_col

    def __len__(self):
        return len(self.data)
