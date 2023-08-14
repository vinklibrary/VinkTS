from typing import Any, Dict, Iterator, List, Optional
from pathlib import Path

# Dictionary used for data flowing through the transformations.
DataEntry = Dict[str, Any]
DataBatch = Dict[str, Any]

class Dataset():
    def __iter__(self) -> Iterator[DataEntry]:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

class DatasetWriter:
    def write_to_file(self, dataset: Dataset, path: Path) -> None:
        raise NotImplementedError

    def write_to_folder(
        self, dataset: Dataset, folder: Path, name: Optional[str] = None
    ) -> None:
        raise NotImplementedError