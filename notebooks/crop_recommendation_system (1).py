# -*- coding: utf-8 -*-
"""Crop Recommendation System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ec8cnu2Fae7yoLQQ6fwXJyVSkhsbT1yQ

###Importing Libraries
"""

# Importing the necessary libraries

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score
from tabulate import tabulate

"""###Load the dataset
The dataset used in this notebook was sourced from Kaggle and it contains information of various Crops along with the factors.
"""

crop= pd.read_csv('/content/drive/MyDrive/ML/Crop_recommendation.csv')

"""*ATTRIBUTES DESCRIPTION:*
*  **N -** ratio of Nitrogen content in the soil
*   **P -** ratio of Phosphorus content in the soil
*   **K -** ratio of Potassium content in the soil
*   **temperature -** temperature in degree Celsius
*   **humidity -** relative humidity in %
*   **ph -** ph value of the soil
*   **rainfall -** rainfall in mm
*   **label -** Crop Type

###Exploratory Data Analysis
"""

crop.head()

crop.describe()

crop.info()

crop.shape

crop.columns

crop['label'].unique()

# Histogram

crop.hist(figsize=(12, 8))
plt.tight_layout()
plt.show()

# Bar plot of 'label'

plt.figure(figsize=(8, 6))
sns.countplot(x='label', data=crop)
plt.title('Frequency Count of Crop Types')
plt.xticks(rotation=45)
plt.show()

"""The equal bar sizes of the 22 crops in the bar plot indicate a *balanced distribution of crop types* in the dataset."""

# Correlation using heatmap

plt.figure(figsize=(13,11))
sns.heatmap(crop.corr(), center = 0, annot = True)
plt.show()

"""###Data Preprocessing"""

# Checking for missing values

crop.isnull().sum()

# Encoding categorical column into numerical

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
crop['label'] = le.fit_transform(crop['label'])

crop

# Extracting independent and dependent variables

x = crop.iloc[:,:-1].values
y = crop.iloc[:,-1].values

"""Auto Data Split"""

def performance(x_train, x_test, y_train, y_test, classifier):
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    return accuracy, precision, recall, f1

def find_optimal_split_ratio(x_scaled, y, classifiers, splitting_ratios):
    optimal_ratio = None
    max_accuracy = 0.0
    header = ["Test Ratio", "Classifier", "Accuracy", "Precision", "Recall", "F1-score"]
    table_data = []
    for test_ratio in splitting_ratios:
        x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=test_ratio, random_state=42)
        for classifier_name, classifier in classifiers.items():
            accuracy, precision, recall, f1 = performance(x_train, x_test, y_train, y_test, classifier)
            row_data = [f"{test_ratio:.2f}", classifier_name,
                        f"{accuracy:.4f}", f"{precision:.4f}",
                        f"{recall:.4f}", f"{f1:.4f}"]
            table_data.append(row_data)
            if accuracy > max_accuracy:
                max_accuracy = accuracy
                optimal_ratio = test_ratio
    print("\nOptimal Splitting Ratio:", optimal_ratio)
    print(tabulate(table_data, headers=header, tablefmt="grid"))

# Define the classifiers

classifiers = {'Random Forest': RandomForestClassifier(),
              'Support Vector Machine': SVC(),
              'Decision Tree': DecisionTreeClassifier(),
              'KNN': KNeighborsClassifier()
              }

# Define Splitting ratios to evaluate

splitting_ratios = np.linspace(0.1, 0.9)

# Find the Optimal Splitting ratio
find_optimal_split_ratio(x, y, classifiers, splitting_ratios)

"""###Model Building"""

# Splitting into train and test set

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

print(x_train.shape)

print(x_test.shape)

# RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=None,random_state=42)
rfc.fit(x_train, y_train)
y_pred1 = rfc.predict(x_test)

print('Random Forest Classifier\n')
rfc_acc = accuracy_score(y_test, y_pred1)
print(f'Accuracy: {rfc_acc}')
rfc_precision = precision_score(y_test, y_pred1, average='weighted')
print(f'Precision: {rfc_precision}')
rfc_recall = recall_score(y_test, y_pred1, average='weighted')
print(f'Recall: {rfc_recall}')
rfc_f1 = f1_score(y_test, y_pred1, average='weighted')
print(f'F1-score: {rfc_f1}')

# K-Neighbors Classifier

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
y_pred2 = knn.predict(x_test)

print('K-Nearest Neighbor\n')
knn_acc = accuracy_score(y_test, y_pred2)
print(f'Accuracy: {knn_acc}')
knn_precision = precision_score(y_test, y_pred2, average='weighted')
print(f'Precision: {knn_precision}')
knn_recall = recall_score(y_test, y_pred2, average='weighted')
print(f'Recall: {knn_recall}')
knn_f1 = f1_score(y_test, y_pred2, average='weighted')
print(f'F1-score: {knn_f1}')

# Support Vector Classsifier

svm = SVC(random_state=42)
svm.fit(x_train, y_train)
y_pred3 = svm.predict(x_test)

print('Support Vector Classifier\n')
svm_acc = accuracy_score(y_test, y_pred3)
print(f'Accuracy: {svm_acc}')
svm_precision = precision_score(y_test, y_pred3, average='weighted')
print(f'Precision: {svm_precision}')
svm_recall = recall_score(y_test, y_pred3, average='weighted')
print(f'Recall: {svm_recall}')
svm_f1 = f1_score(y_test, y_pred3, average='weighted')
print(f'F1-score: {svm_f1}')

# Decision Tree Classifier

dt = DecisionTreeClassifier(random_state=42)
dt.fit(x_train, y_train)
y_pred4 = dt.predict(x_test)

print('Decision Tree Classifier\n')
dt_acc = accuracy_score(y_test, y_pred4)
print(f'Accuracy: {dt_acc}')
dt_precision = precision_score(y_test, y_pred4, average='weighted')
print(f'Precision: {dt_precision}')
dt_recall = recall_score(y_test, y_pred4, average='weighted')
print(f'Recall: {dt_recall}')
dt_f1 = f1_score(y_test, y_pred4, average='weighted')
print(f'F1-score: {dt_f1}')

"""


*   Random forest Classifier followed with an accuracy of **0.993**

*   K Neighbors Classifier has an accuracy of **0.970**
*   Support Vector Classsifier follows as accuracy of **0.961**
*   Decision Tree Model has an accuracy of **0.986**

"""

model_names = ['Random Forest', 'KNN', 'SVM', 'Decision Tree']
accuracies = [rfc_acc, knn_acc, svm_acc, dt_acc]

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(model_names, accuracies, color='skyblue')
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Accuracy of Each Model')
plt.ylim(0.95, 1)  # Set y-axis limit to ensure all accuracies are visible
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for better visualization
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

"""The *Random Forest Classifier* showed the highest accuracy of **99%** among the models tested, making it more effective model for predicting the crops based on the features given in this dataset."""



