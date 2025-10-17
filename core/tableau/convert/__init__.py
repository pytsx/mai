from .tdsx import Tdsx, FilePath
import pandas as pd
from pathlib import Path

class Converter:
  def __init__(self, file: str):
    self._file: FilePath = FilePath(file)
    self.suffix = self._file.suffix()

  def to_dataframe(self) -> list[pd.DataFrame]:
    match self.suffix.as_string().lower():
      case 'tdsx':
        return Tdsx.to_dataframe(self._file)
    return []
  
  def to_excel(
    self,
    out_path: str | None = None,
    engine: str | None = None,
    index: bool = False
  ) -> list[Path]:
    match self.suffix.as_string().lower():
      case 'tdsx':
        return [path._value for path in Tdsx.to_excel(self._file, out_path, engine, index)]
  
  def to_csv(
    self,
    out_path: str | None = None,
    engine: str | None = None,
    index: bool = False
  ) -> list[Path]:
    match self.suffix.as_string().lower():
      case 'tdsx':
        return [path._value for path in Tdsx.to_csv(self._file, out_path, engine, index)]
  