# summer-internship-program-
import pandas as pd
import joblib

#import dataset
db = pd.read_csv('Salary_Data.csv') 

x = db['YearsExperience'].values.reshape(-1,1)
y = db['Salary']
#import linear regression model
from sklearn.linear_model import LinearRegression  
model = LinearRegression()
#fitting the model
model.fit(x,y)
#dumping of model
joblib.dump(model,'salary.pk1')
