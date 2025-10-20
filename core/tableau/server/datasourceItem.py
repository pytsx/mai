import pandas as pd 
from pathlib import Path

from core.tableau.convert import Tdsx

type ParquetPath = Path

class DatasourceItem:
  def __init__(self, path: str, is_parquet: bool = False):
    self._path: Path = Path(path) 
    self._is_parquet: bool = is_parquet
    self._is_tdsx: bool = self._path.suffix.endswith("tdsx")
  
  def get_parquet(self) -> ParquetPath:
    if self._is_parquet:
      return self._path
    
    if self._is_tdsx:
      df = Tdsx.to_dataframe(self._path)
      new_item = DatasourceItem.from_dataframe(df)
      del df
      return new_item.get_parquet()
  
  @staticmethod
  def _create_temp_file() -> ParquetPath:
    base_path = './temp/upload_item_temp_file'
    file_extension = '.parquet'
    
    temp_path = Path(f'{base_path}.{file_extension}')
    if temp_path.exists():
      temp_files_len = len(list(temp_path.parent.iterdir()))
      temp_path = Path(f'{base_path} ({temp_files_len}).{file_extension}')
    
    temp_path.parent.mkdir(parents=True, exist_ok=True)
    
    return temp_path
  
  @staticmethod
  def from_dataframe(df: pd.DataFrame) -> 'DatasourceItem':
    temp_path = DatasourceItem._create_temp_file()
    df.to_parquet(temp_path)
    return DatasourceItem(temp_path, is_parquet=True)
