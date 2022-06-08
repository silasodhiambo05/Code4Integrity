#importing the dependencies
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv('data.csv')
print(data.head())

#splitting the data into features and target
X = data.drop(columns = 'Class', axis = 1)
Y = data['Class']

#splitting the data
X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size = 0.2 , random_state = 2)
print(X.shape,Y.shape,X_train.shape,X_test.shape,Y_train.shape,Y_test.shape)

#model
model = LogisticRegression()
model.fit(X_train,Y_train)

train_pred = model.predict(X_train)
score_1 = accuracy_score(Y_train,train_pred)

test_pred = model.predict(X_test)
score_2 = accuracy_score(Y_test,test_pred)

print('Accuracy on train prediction and test prediction is:',score_1, score_2)

filename = 'finalized_model.sav'
joblib.dump(model,filename)