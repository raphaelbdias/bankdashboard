import pickle
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier

with open('hclf_churn_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


age = float(14)
is_active_member = float(0)

# Convert to numpy array and reshape for prediction
features = np.array([age, is_active_member]).reshape(1, -1)


if hasattr(model, '_classes'):  # Check if it is a classifier with classes attribute available (scikit-learn < v0.24)
    # Make prediction
    prediction = model.predict(features)
    prediction = int(model.predict(features)[0])

    prediction = int(clf.predict(features)[0])
else:
    prediction = model.predict_proba(features).argmax()

print(prediction)