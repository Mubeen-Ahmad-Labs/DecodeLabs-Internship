# ==========================================================
# Project 2: Data Classification Using AI
# Dataset: Iris.csv
# Algorithm: K-Nearest Neighbors (KNN)
# ==========================================================

# ==========================
# Import Libraries
# ==========================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    f1_score
)

# ==========================
# Load Dataset
# ==========================
df = pd.read_csv("Iris.csv")

print("=" * 60)
print("IRIS DATASET")
print("=" * 60)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nClass Distribution:")
print(df["Species"].value_counts())

# ==========================
# Prepare Data
# ==========================

# Remove Id column (not useful for prediction)
df = df.drop("Id", axis=1)

# Features
X = df.drop("Species", axis=1)

# Target
y = df["Species"]

# Convert text labels into numbers
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# ==========================
# Feature Scaling
# ==========================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==========================
# Split Dataset
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples :", len(X_test))

# ==========================
# Train KNN Model
# ==========================
knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# ==========================
# Prediction
# ==========================
y_pred = knn.predict(X_test)

# ==========================
# Accuracy
# ==========================
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy Score")
print("-" * 30)
print(f"{accuracy*100:.2f}%")

# ==========================
# F1 Score
# ==========================
f1 = f1_score(y_test, y_pred, average="weighted")

print("\nF1 Score")
print("-" * 30)
print(f"{f1:.4f}")

# ==========================
# Confusion Matrix
# ==========================
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")
print("-" * 30)
print(cm)

# ==========================
# Classification Report
# ==========================
print("\nClassification Report")
print("-" * 30)

print(classification_report(
    y_test,
    y_pred,
    target_names=encoder.classes_
))

# ==========================
# Plot Confusion Matrix
# ==========================
plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=encoder.classes_,
    yticklabels=encoder.classes_
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()

# ==========================
# Predict New Flower
# ==========================

print("\nPredict New Flower")
print("-" * 30)

new_flower = [[5.1, 3.5, 1.4, 0.2]]

new_flower_scaled = scaler.transform(new_flower)

prediction = knn.predict(new_flower_scaled)

print("Flower Measurements:")
print(new_flower[0])

print("\nPredicted Species:")
print(encoder.inverse_transform(prediction)[0])

# ==========================
# Predict Multiple Flowers
# ==========================

print("\nPredict Multiple Flowers")
print("-" * 30)

flowers = [
    [5.1, 3.5, 1.4, 0.2],
    [6.5, 3.0, 5.2, 2.0],
    [5.9, 2.8, 4.3, 1.3]
]

flowers_scaled = scaler.transform(flowers)

predictions = knn.predict(flowers_scaled)

for i, flower in enumerate(flowers):
    print(f"\nFlower {i+1}")
    print("Measurements:", flower)
    print("Predicted Species:", encoder.inverse_transform([predictions[i]])[0])

print("\n" + "=" * 60)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 60)