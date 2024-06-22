# Medicine-Recommendation-System
This code implements a disease prediction system based on user-reported symptoms.

## How it Works:

### Data Preprocessing:
Loads the training data from Datasets/Training.csv.
Separates features (symptoms) from target variable (disease).
Encodes the disease labels using a label encoder.
Splits data into training and testing sets.

### Model Training:
Trains various machine learning models, including:
Random Forest Classifier
Gradient Boosting Classifier
K-Nearest Neighbors Classifier
Multinomial Naive Bayes
Evaluates the performance of each model using accuracy score.

### Model Selection:
Currently, a linear SVC model is chosen and saved for prediction.

### User Input:
Asks the user to enter their symptoms separated by commas.

### Prediction:
Converts user symptoms into a numerical representation based on a predefined dictionary.
Uses the saved model to predict the disease based on the user's symptoms.

### Output:
Displays the predicted disease.
