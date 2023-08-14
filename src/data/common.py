from . import Dataset, DataEntry, DataBatch

import pandas

#  data:pandas.DataFrame
#  start
#


class TsDataset(Dataset):
    super().__init__()
    def __init__(self,
                 data : pandas.DataFrame,
                 target_col : str,
                 ts_col : str
                 ):
        self.data = data
        self.target_col = target_col
        self.ts_col = ts_col