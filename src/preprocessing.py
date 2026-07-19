from sklearn.model_selection import train_test_split
import pandas as pd

def preprocess_news_data(df):

    df = df.copy()

    for col in ["headline", "short_description", "authors"]:
        df[col] = (df[col].fillna("").str.strip())

    df = df.drop_duplicates()
    df = df.drop_duplicates(subset=["headline", "short_description","category"])
    df["text"] = (df["headline"] + " " + df["short_description"]).str.strip()
    df = df[df["text"].str.len() > 0]
    df = df[["text", "category"]]

    return df

def split_data(df, test_size=0.3, random_state=42):
    
    X = df["text"]
    y = df["category"]

    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)

    X_valid, X_test, y_valid, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=random_state, stratify=y_temp)

    return X_train, X_valid, X_test, y_train, y_valid, y_test