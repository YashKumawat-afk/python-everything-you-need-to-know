# ============================================================
#  Scikit-learn Basics — python-everything-you-need-to-know
# ============================================================

from sklearn.datasets import load_iris, load_digits
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    classification_report, confusion_matrix,
    accuracy_score
)
import numpy as np

print("=" * 50)
print("  Scikit-learn Basics")
print("=" * 50)

# ------ 1. Load Dataset ------
print("\n[1] Load Iris Dataset")
iris = load_iris()
X, y = iris.data, iris.target
print("Features:", iris.feature_names)
print("Classes:", iris.target_names)
print("Shape X:", X.shape, " | y:", y.shape)

# ------ 2. Train/Test Split ------
print("\n[2] Train / Test Split")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Train: {X_train.shape} | Test: {X_test.shape}")

# ------ 3. Feature Scaling ------
print("\n[3] Feature Scaling")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)
print("Mean (after scaling):", X_train_scaled.mean().round(4))
print("Std  (after scaling):", X_train_scaled.std().round(4))

# ------ 4. Random Forest ------
print("\n[4] Random Forest Classifier")
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print("\nClassification Report:\n", classification_report(
    y_test, y_pred_rf, target_names=iris.target_names
))

# ------ 5. Logistic Regression ------
print("\n[5] Logistic Regression")
lr = LogisticRegression(max_iter=200, random_state=42)
lr.fit(X_train_scaled, y_train)
y_pred_lr = lr.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred_lr))

# ------ 6. Decision Tree ------
print("\n[6] Decision Tree")
dt = DecisionTreeClassifier(max_depth=4, random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred_dt))

# ------ 7. Cross Validation ------
print("\n[7] Cross-Validation (5-fold)")
scores = cross_val_score(rf, X, y, cv=5, scoring='accuracy')
print("CV Scores:", scores.round(3))
print(f"Mean: {scores.mean():.3f}  |  Std: {scores.std():.3f}")

# ------ 8. Feature Importance ------
print("\n[8] Feature Importance (Random Forest)")
importances = rf.feature_importances_
for name, imp in zip(iris.feature_names, importances):
    bar = '█' * int(imp * 40)
    print(f"  {name:<25} {imp:.4f}  {bar}")

# ------ 9. Confusion Matrix ------
print("\n[9] Confusion Matrix (Random Forest)")
cm = confusion_matrix(y_test, y_pred_rf)
print(cm)

# ------ 10. Predict New Sample ------
print("\n[10] Predict on New Sample")
sample = np.array([[5.1, 3.5, 1.4, 0.2]])   # Looks like setosa
prediction = rf.predict(sample)
probability = rf.predict_proba(sample)
print("Predicted class:", iris.target_names[prediction[0]])
print("Probabilities:", {
    iris.target_names[i]: round(probability[0][i], 3)
    for i in range(3)
})

print("\n✅ Scikit-learn tutorial complete!")
