import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import scikitplot as skplt
import matplotlib.pyplot as plt


def one_hot_encoding(df, columns):
    new_df = df.copy()
    if columns == []:
        return df
    else:
        for col in columns:
            try:
                new_df = pd.concat([new_df, pd.get_dummies(df[col], prefix=col, dtype=int)], axis=1)
                new_df.drop(columns=[col], inplace=True)
            except:
                continue
        return new_df
    

def plotROCCurves(y_test, X_test, algo_classify, algo_augment_name:str):
    plt.figure(figsize=(20, 10))
    skplt.metrics.plot_roc_curve(y_test, algo_classify.predict_proba(X_test), figsize=(20, 10))
    algo_classify_name = type(algo_classify).__name__
    title = algo_augment_name + " , " + algo_classify_name
    plt.title(title)
    plt.show()
    plt.savefig("figures/"+algo_augment_name+"_"+algo_classify_name)
    

