import pandas as pd 
from .datasourceItem import DatasourceItem

class TableauServer:
  def upload_datasource(_item: DatasourceItem | pd.DataFrame):
    item = _item
    if isinstance(_item, pd.DataFrame):
      item = DatasourceItem(_item)
      
    parquet = item.get_parquet()
    return 