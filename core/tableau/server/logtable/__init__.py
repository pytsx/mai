import pandas as pd 
from datetime import datetime 
from typing import Literal 
from dataclasses import dataclass

type LogLevel = Literal['info'] | Literal['log'] | Literal['error'] | Literal['panic']

@dataclass
class _Event:
  trace_id: list[str]
  message: list[str]
  at: list[datetime]
  level: list[LogLevel]

class LogTable:
  def __init__(self, trace_id: str):
    self.trace_id=trace_id
    self._df=pd.DataFrame()
  
  def get_table(self):
    return self._df
  
  def _append(self, df: pd.DataFrame):
    self._df=pd.concat(objs=[self.get_table(), df], ignore_index=True)
  
  def _insert_log_entry(self, obj: dict[str, list]):
    self._append(df=pd.DataFrame(obj))
    
  def _log_event(self, trace_id: str, msg: str, level: LogLevel):
    self._insert_log_entry({
      'trace_id': [trace_id],
      'message': [msg],
      'at': [datetime.now()],
      'level': [level]
    }) 
  
  def log(self, msg: str):
    self._log_event(self.trace_id, msg, 'log')
    
  def info(self, msg: str):
    self._log_event(self.trace_id, msg, 'info')
    
  def error(self, msg: str):
    self._log_event(self.trace_id, msg, 'error')
    
  def panic(self, msg: str):
    self._log_event(self.trace_id, msg, 'panic')