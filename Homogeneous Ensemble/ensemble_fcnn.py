# -*- coding: utf-8 -*-
"""ensemble_fcnn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TqwXdGi_LzCfjPu6DsDDCJiXNQK8gaHs
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the dataset
url_dataset = pd.read_csv('kaggle.csv')

# Separate the features and labels
X = url_dataset.iloc[:, 2:]  # Exclude the URL and Label columns
y = url_dataset['Label']

# Convert labels to categorical values
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
num_classes = len(label_encoder.classes_)
y = to_categorical(y)

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define the architecture of a single fully connected neural network
def create_model():
    model = Sequential()
    model.add(Dense(20, activation='relu', input_shape=(X_train.shape[1],)))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Create three neural network models
model1 = create_model()
model2 = create_model()
model3 = create_model()

# Train each model separately
model1.fit(X_train, y_train, epochs=500, batch_size=512, verbose=1)
model2.fit(X_train, y_train, epochs=500, batch_size=512, verbose=1)
model3.fit(X_train, y_train, epochs=500, batch_size=512, verbose=1)

# Combine the models into an ensemble
ensemble_model = [model1, model2, model3]

# Make predictions using each model in the ensemble
y_pred_ensemble = []
for model in ensemble_model:
    y_pred = model.predict(X_test)
    y_pred_ensemble.append(y_pred)

# Take the majority vote for each sample in the test set
y_pred_ensemble = sum(y_pred_ensemble) / len(ensemble_model)
y_pred_ensemble = label_encoder.inverse_transform(y_pred_ensemble.argmax(axis=1))

# Evaluate the ensemble model
accuracy = (y_pred_ensemble == label_encoder.inverse_transform(y_test.argmax(axis=1))).mean()
print(f"Accuracy: {accuracy}")

from sklearn.metrics import classification_report
# Make predictions using each model in the ensemble
y_pred_ensemble = []
for model in ensemble_model:
    y_pred = model.predict(X_test)
    y_pred_ensemble.append(y_pred)

# Take the majority vote for each sample in the test set
y_pred_ensemble = sum(y_pred_ensemble) / len(ensemble_model)
y_pred_ensemble = label_encoder.inverse_transform(y_pred_ensemble.argmax(axis=1))

# Convert the ground truth labels back to their original form
y_test = label_encoder.inverse_transform(y_test.argmax(axis=1))

# Generate the classification report
classification_rep = classification_report(y_test, y_pred_ensemble, digits=5)
print(classification_rep)