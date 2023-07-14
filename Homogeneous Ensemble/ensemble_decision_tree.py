# -*- coding: utf-8 -*-
"""ensemble_decision tree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16Jfgd8YU9vbYa8SStvyWvLdoLmspaMrU
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load the dataset
url_dataset = pd.read_csv('kaggle.csv')

# Separate the features and labels
X = url_dataset.iloc[:, 2:]  # Exclude the URL and Label columns
y = url_dataset['Label']

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create three decision tree classifiers
tree1 = DecisionTreeClassifier(max_depth=100, criterion='gini', splitter='best')
tree2 = DecisionTreeClassifier(max_depth=100, criterion='gini', splitter='best')
tree3 = DecisionTreeClassifier(max_depth=100, criterion='gini', splitter='best')

# Create the ensemble model using VotingClassifier
ensemble_model = VotingClassifier(
    estimators=[('tree1', tree1), ('tree2', tree2), ('tree3', tree3)],
    voting='hard'  # You can change this to 'soft' for probabilistic voting
)

# Fit the ensemble model on the training data
ensemble_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = ensemble_model.predict(X_test)

# Generate the classification report
classification_rep = classification_report(y_test, y_pred, digits=5)
print(classification_rep)