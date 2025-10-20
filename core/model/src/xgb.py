from .model import Model, ArrayLike
from typing import Optional, Union, Tuple,Sequence, List, Dict, Callable
import xgboost as xgb
import numpy as np 

# typing.SupportsInt is not suitable here since floating point values are convertible to
# integers as well.
Integer = Union[int, np.integer]
IterationRange = Tuple[Integer, Integer]

class XGBClassifier(xgb.XGBClassifier):
  def __init__(self, 
    max_depth: Optional[int] = None,
    max_leaves: Optional[int] = None,
    max_bin: Optional[int] = None,
    grow_policy: Optional[str] = None,
    learning_rate: Optional[float] = None,
    n_estimators: Optional[int] = None,
    verbosity: Optional[int] = None,
    objective: str = None,
    booster: Optional[str] = None,
    tree_method: Optional[str] = None,
    n_jobs: Optional[int] = None,
    gamma: Optional[float] = None,
    min_child_weight: Optional[float] = None,
    max_delta_step: Optional[float] = None,
    subsample: Optional[float] = None,
    sampling_method: Optional[str] = None,
    colsample_bytree: Optional[float] = None,
    colsample_bylevel: Optional[float] = None,
    colsample_bynode: Optional[float] = None,
    reg_alpha: Optional[float] = None,
    reg_lambda: Optional[float] = None,
    scale_pos_weight: Optional[float] = None,
    base_score: Optional[float] = None,
    random_state: Optional[
        Union[np.random.RandomState, np.random.Generator, int]
    ] = None,
    missing: float = np.nan,
    num_parallel_tree: Optional[int] = None,
    monotone_constraints: Optional[Union[Dict[str, int], str]] = None,
    interaction_constraints: Optional[Union[str, Sequence[Sequence[str]]]] = None,
    importance_type: Optional[str] = None,
    device: Optional[str] = None,
    validate_parameters: Optional[bool] = None,
    enable_categorical: bool = False,
    feature_types = None,
    feature_weights: Optional[ArrayLike] = None,
    max_cat_to_onehot: Optional[int] = None,
    max_cat_threshold: Optional[int] = None,
    multi_strategy: Optional[str] = None,
    eval_metric: Optional[Union[str, List[str], Callable]] = None,
    early_stopping_rounds: Optional[int] = None,
    callbacks = None,
  ):
    self._params = {k: v for k, v in {
      'max_depth': max_depth,
      'max_leaves': max_leaves,
      'max_bin': max_bin,
      'grow_policy': grow_policy,
      'learning_rate': learning_rate,
      'n_estimators': n_estimators,
      'verbosity': verbosity,
      'objective': objective,
      'booster': booster,
      'tree_method': tree_method,
      'n_jobs': n_jobs,
      'gamma': gamma,
      'min_child_weight': min_child_weight,
      'max_delta_step': max_delta_step,
      'subsample': subsample,
      'sampling_method': sampling_method,
      'colsample_bytree': colsample_bytree,
      'colsample_bylevel': colsample_bylevel,
      'colsample_bynode': colsample_bynode,
      'reg_alpha': reg_alpha,
      'reg_lambda': reg_lambda,
      'scale_pos_weight': scale_pos_weight,
      'base_score': base_score,
      'random_state': random_state,
      'missing': missing,
      'num_parallel_tree': num_parallel_tree,
      'monotone_constraints': monotone_constraints,
      'interaction_constraints': interaction_constraints,
      'importance_type': importance_type,
      'device': device,
      'validate_parameters': validate_parameters,
      'enable_categorical': enable_categorical,
      'max_cat_to_onehot': max_cat_to_onehot,
      'max_cat_threshold': max_cat_threshold,
      'multi_strategy': multi_strategy,
      'eval_metric': eval_metric,
      'early_stopping_rounds': early_stopping_rounds,
      'feature_weights': feature_weights,
      'feature_types': feature_types,
      'callbacks': callbacks
    }.items() if v is not None}
    
    super().__init__(**self._params)