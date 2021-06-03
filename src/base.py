import pandas as pd
import numpy as np


class BaseDataAugmentation:
    def __init__(self, df, categorical, target):
        self.categorical = categorical
        self.df = df
        self.df.columns = [str(i) for i in df.columns]
        self.columns = df.columns
        self.target = target
        self.models = []
        self.continuous = []
        self.classes = df[target].unique().tolist()
        self.classes = [str(i) for i in self.classes]
        for enum, i in enumerate(self.df.columns):
            if i not in (categorical):
                self.continuous.append(i)
        self.df[self.categorical] = self.df[self.categorical].astype(str)
        self.df[self.continuous] = self.df[self.continuous].astype(float)
        self.df[self.target] = self.df[self.target].astype(str)

    def fit(self):
        pass

    def generate(self):
        generated_data = pd.DataFrame()
        majority_class = self.get_majority_class()
        majority_size = self.df[self.df[self.target] == majority_class].shape[0]
        for i, classe in enumerate(self.classes):
            initial_size = self.df[self.df[self.target] == classe].shape[0]
            n = majority_size - initial_size
            if n > 0:
                new_data = self.models[i].sample(n)
                generated_data = pd.concat([generated_data, new_data])
        return generated_data

    def augment(self):
        generated_data = self.generate()
        generated_data.columns = self.columns
        self.df.columns = self.columns
        augmented_data = pd.concat([generated_data, self.df], axis=0)
        augmented_data.columns = self.columns
        augmented_data[self.categorical] = augmented_data[self.categorical].astype(str)
        try:
            self.continuous.remove(self.target)
        except:
            pass
        augmented_data[self.continuous] = augmented_data[self.continuous].astype(float)
        augmented_data[self.target] = augmented_data[self.target].astype(str)
        augmented_data = augmented_data.replace([np.inf, -np.inf], np.nan).dropna()
        return augmented_data

    def get_majority_class(self):
        max_size = 0
        majority_class = self.classes[0]
        for classe in self.classes:
            size = self.df[self.df[self.target] == classe].shape[0]
            if size > max_size:
                max_size = size
                majority_class = classe
        return majority_class

    def get_models(self):
        return self.models