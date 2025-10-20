
from abc import ABC, abstractmethod
from typing import Literal

type ArrayLike = any
type MainMetricsType = Literal['accuracy'] | Literal['precision'] | Literal['recall'] | Literal['f1'] | Literal['roc_auc'] 

class Model(ABC):
  @abstractmethod
  def fit(self, *arg, **kwargs):
    pass

  @abstractmethod
  def predict(self, *arg, **kwargs):
    pass

  @abstractmethod
  def predict_proba(self,  *arg, **kwargs):
    pass

  @abstractmethod
  def get_params(self):
    pass