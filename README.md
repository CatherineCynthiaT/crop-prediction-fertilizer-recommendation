# Project Overview  
This project aims to develop models for predicting suitable crops and recommending fertilizers based on various soil and environmental factors. Accurate predictions and recommendations can significantly enhance agricultural productivity and optimize resource utilization.  

## Implementation Details  

### Methods Used  
- **Machine Learning**  
- **Data Cleaning**  
- **Feature Engineering**  
- **Classification Algorithms**  

### Python Packages Used  
- `pandas`  
- `numpy`  
- `scikit-learn`  
- `matplotlib`  
- `seaborn`  
- `xgboost`  

## Steps Followed  
1. **Data Collection**: Collected datasets for crop prediction and fertilizer recommendation from Kaggle.  

2. **Data Preprocessing**:  
   - **Crop Prediction**: Handled missing values, encoded categorical columns, and performed exploratory data analysis to understand feature distributions and correlations.  
   - **Fertilizer Recommendation**: Checked for missing values, encoded categorical columns, and conducted exploratory data analysis to visualize fertilizer usage and feature relationships.  

3. **Model Development**:  
   - **Crop Prediction**: Trained various classifiers (Random Forest, K-Nearest Neighbors, Support Vector Machine, Decision Tree) and evaluated their performance. The Random Forest Classifier achieved the highest accuracy of 99%.  
   - **Fertilizer Recommendation**: Trained classifiers (Random Forest, K-Nearest Neighbors, Support Vector Machine, Decision Tree) and assessed their effectiveness. The Support Vector Classifier provided the best performance with an accuracy of 94%.  

4. **Model Evaluation**: Evaluated models using metrics such as accuracy, precision, recall, and F1-score. The Random Forest model showed the highest accuracy for crop prediction, while the Support Vector Classifier excelled in fertilizer recommendation.  

## Results and Evaluation  
- **Crop Prediction**: The Random Forest Classifier performed best with an accuracy of 99%.  
- **Fertilizer Recommendation**: The Support Vector Classifier achieved an accuracy of 94%, making it the most effective model for fertilizer recommendations.  

The project successfully demonstrates the application of machine learning for agricultural predictions and recommendations, showcasing practical benefits in optimizing crop yields and fertilizer usage.  
