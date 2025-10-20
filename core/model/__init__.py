import xgboost as xgb
from sklearn.metrics import precision_recall_curve, classification_report
import matplotlib.pyplot as plt

from .src.model import ArrayLike, MainMetricsType

from sklearn.metrics import (
    accuracy_score, 
    precision_score, 
    recall_score, 
    f1_score, 
    roc_auc_score
)

class ModelMetrics:
  @staticmethod
  def main_metrics(
    y_test: ArrayLike, 
    y_pred: ArrayLike, 
    y_pred_proba: ArrayLike
  ) -> list[tuple[MainMetricsType, float]]:
    # Calcular métricas de desempenho
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    
    return [
      ('accuracy', accuracy),
      ('precision', precision),
      ('recall', recall),
      ('f1', f1),
      ('roc_auc', roc_auc),
    ]
    
  @staticmethod
  def print_main_metrics(
    y_test: ArrayLike, 
    y_pred: ArrayLike, 
    y_pred_proba: ArrayLike
  ) -> list[tuple[MainMetricsType, float]]:
    metrics = ModelMetrics.main_metrics(y_test, y_pred, y_pred_proba)
    for metric in metrics:
      key, value = metric
      print(f"{key}:\t\t\t\t{value:.4f}") # quao bem o modelo consegue separar as classes 
      
  @staticmethod
  def plot_precision_recall_curve(
    y_test: ArrayLike, 
    y_pred_proba: ArrayLike  
  ):
    precision, recall, thresholds = precision_recall_curve(y_test, y_pred_proba)

    f1 = 2 * (precision * recall) / (precision + recall + 1e-8)
    best_threshold = thresholds[f1.argmax()]

    print(f"Melhor threshold: {best_threshold:.3f}")

    # aplicar o novo limiar
    y_pred_opt = (y_pred_proba >= best_threshold).astype(int)
    print(classification_report(y_test, y_pred_opt))

    # opcional: visualizar
    plt.plot(thresholds, precision[:-1], label='Precisão')
    plt.plot(thresholds, recall[:-1], label='Recall')
    plt.plot(thresholds, f1[:-1], label='F1-score', color='black')
    plt.xlabel("Threshold")
    plt.ylabel("Métrica")
    plt.title("Precisão, Recall e F1 vs Threshold")
    plt.legend()
    plt.show()
  
  @staticmethod
  def plot_importance(model):
    fig, ax = plt.subplots(figsize=(15, 8))
    xgb.plot_importance(model, max_num_features=15, ax=ax, importance_type='weight')
    plt.title('Importância das Features (XGBoost - Weight)')
    plt.tight_layout()
    plt.show()