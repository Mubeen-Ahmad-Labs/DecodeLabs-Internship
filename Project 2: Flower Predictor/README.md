# Iris Flower Classification Using KNN

## Overview

This project is part of my **Artificial Intelligence Internship at DecodeLabs**. The objective of this project is to build a basic supervised machine learning classification model using the **Iris dataset**.

The model uses the **K-Nearest Neighbors (KNN)** algorithm to classify Iris flowers into their respective species based on their measurements.

## Dataset

The project uses the `Iris.csv` dataset containing **150 samples** and the following columns:

* `Id`
* `SepalLengthCm`
* `SepalWidthCm`
* `PetalLengthCm`
* `PetalWidthCm`
* `Species`

The dataset contains three flower species:

* Iris-setosa
* Iris-versicolor
* Iris-virginica

The `Id` column is removed before training because it does not provide useful information for classification.

## Technologies & Libraries

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

## Machine Learning Workflow

The project follows these steps:

1. Load the Iris dataset using Pandas.
2. Explore the dataset and check for missing values.
3. Remove the unnecessary `Id` column.
4. Separate features and target labels.
5. Encode the target species into numerical labels.
6. Apply feature scaling using `StandardScaler`.
7. Split the dataset into training and testing sets.
8. Train a K-Nearest Neighbors (KNN) classification model.
9. Make predictions on the test data.
10. Evaluate the model using accuracy, F1 score, confusion matrix, and classification report.
11. Use the trained model to predict new flower samples.

## Model

### K-Nearest Neighbors (KNN)

The project uses the KNN classification algorithm with:

```text
n_neighbors = 5
```

KNN classifies a new sample based on the classes of its nearest neighboring data points.

## Dataset Split

The dataset is divided into:

* **80% Training Data:** 120 samples
* **20% Testing Data:** 30 samples

The split is performed using `train_test_split()` with stratification to maintain the class distribution.

## Results

The trained KNN model achieved:

| Metric            | Result |
| ----------------- | -----: |
| Accuracy          | 93.33% |
| Weighted F1 Score | 0.9327 |

### Confusion Matrix

```text
[[10  0  0]
 [ 0 10  0]
 [ 0  2  8]]
```

The model correctly classified most of the test samples, with the main misclassification occurring between **Iris-versicolor** and **Iris-virginica**.

## Prediction Example

The trained model was also tested with new flower measurements.

Example:

```text
[5.1, 3.5, 1.4, 0.2]
```

Predicted species:

```text
Iris-setosa
```

## Project Structure

```text
FlowerPredictor/
│
├── FlowerPredictor.py
├── Iris.csv
└── README.md
```

## Installation

Install the required Python libraries using:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

## How to Run

Make sure `Iris.csv` and `FlowerPredictor.py` are in the same directory.

Then run:

```bash
python FlowerPredictor.py
```

## Learning Outcomes

Through this project, I gained practical experience in:

* Data loading and exploration
* Data preprocessing
* Feature scaling
* Label encoding
* Train-test splitting
* Supervised machine learning
* KNN classification
* Model evaluation
* Confusion matrix analysis
* F1 score evaluation
* Making predictions on new data

## Internship

**Artificial Intelligence Internship – DecodeLabs**

This project helped strengthen my understanding of fundamental supervised machine learning concepts and the complete workflow of building and evaluating a classification model.

## Author

**Mubeen Ahmad**

Artificial Intelligence Student | AI Intern

