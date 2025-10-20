from .tdsx import Tdsx

import pandas as pd 
import polars as pl
import numpy as np 
from typing import Union, Any, Literal
from datetime import date

IgnoreRaise = Literal["ignore", "raise"]
type ArrayLike = Any
ArrayConvertible = Union[list, tuple, ArrayLike]
Scalar = Union[float, str]
DatetimeScalar = Union[Scalar, date, np.datetime64]

DateTimeErrorChoices = Union[IgnoreRaise, Literal["coerce"]]

class Series(pl.Series):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

class Dataframe(pl.DataFrame):
  # Constrói igual ao pl.DataFrame
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  # =================== readers ============================
  @staticmethod
  def read_tdsx( source: str):
    return Tdsx.to_dataframe(source)[0]
  
  @staticmethod
  def read_csv(source: str, *arg, **kwargs):
    return pl.read_csv(source, *arg, **kwargs)
  
  @staticmethod
  def read_excel(source: str, *arg, **kwargs):
    return pl.read_excel(source, *arg, **kwargs)
  
  @staticmethod
  def read_parquet(source: str, *arg, **kwargs):
    return pl.read_parquet(source, *arg, **kwargs)
 
  # =================== calc ============================
  @staticmethod
  def calc_ema(df: pd.DataFrame, groupby: str, value_column: str, window: int, min_preiods:int=1) -> pd.DataFrame:
    return df.groupby(groupby)[value_column].transform(
      lambda x: x.rolling(window=window, min_periods=min_preiods).mean()
    )
  
  @staticmethod
  def calc_ema_grid(df: pd.DataFrame, groupby: str, value_columns: list[str], windows: list[int]) -> pd.DataFrame:
    for value_column in value_columns:
      for window in windows:
        df[f'ema{window}_{value_column}_{groupby}'] = Dataframe.calc_ema(df, groupby, value_column, window)
    return df 
  
  @staticmethod
  def factorize(
    values,
    sort: bool = False,
    use_na_sentinel: bool = True,
    size_hint: int | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    return pd.factorize(
      values=values, 
      sort=sort, 
      use_na_sentinel=use_na_sentinel, 
      size_hint=size_hint
    )
    
  @staticmethod
  def to_datetime(
    arg: DatetimeScalar,
    errors: DateTimeErrorChoices = 'raise',
    dayfirst: bool = False,
    yearfirst: bool = False,
    utc: bool = None,
    format: str | None = None,
    exact: bool =True,
    unit: str | None =None,
    infer_datetime_format: bool =False,
    origin='unix',
    cache: bool = True,
) -> tuple[np.ndarray, np.ndarray]:
    return pd.to_datetime(
      arg=arg,
      errors=errors,
      dayfirst=dayfirst,
      yearfirst=yearfirst,
      utc=utc,
      format=format,
      exact=exact,
      unit=unit,
      infer_datetime_format=infer_datetime_format,
      origin=origin,
      cache=cache,
    )