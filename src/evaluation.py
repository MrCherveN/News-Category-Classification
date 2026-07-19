from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(model, X, y):

    y_pred = model.predict(X)

    accuracy = accuracy_score(y, y_pred)
    macro_f1 = f1_score(y, y_pred, average="macro")
    weighted_f1 = f1_score(y, y_pred, average="weighted")

    return accuracy, macro_f1, weighted_f1, y_pred

def plot_cm( y_true, y_pred, dataset_name="Validation"):
 
    cm = confusion_matrix(y_true, y_pred, normalize="true")
    
    labels = sorted(y_true.unique())
    
    plt.figure(figsize=(12,10))
    
    sns.heatmap(cm, cmap="Blues", xticklabels=labels,yticklabels=labels, annot=False)
    
    plt.xlabel("Клас, передбачений моделлю")
    plt.ylabel("Фактичний клас")
    plt.title(f"Нормалізована матриця помилок ({dataset_name})")
    
    plt.xticks(rotation=90)
    plt.yticks(rotation=0)
    
    plt.show()