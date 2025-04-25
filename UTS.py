#%%
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder

#%%
df = pd.read_csv('dataset_buys _comp.csv')  # Ganti sesuai nama file
print(df.head())

#%%
# Cek missing value
print(df.isnull().sum())

#%%
# Pisahkan fitur dan target
X = df.drop('Buys_Computer', axis=1)
y = df['Buys_Computer']

# Label Encoding untuk fitur dan target
le = LabelEncoder()

for col in X.columns:
    X[col] = le.fit_transform(X[col])

y = le.fit_transform(y)  # Target juga harus di-encode

#%%
# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#%%
# Training model Naive Bayes
model = GaussianNB()
model.fit(X_train, y_train)

#%%
# Evaluasi
y_pred = model.predict(X_test)

print("Akurasi:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))