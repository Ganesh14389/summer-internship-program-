# summer-internship-program-
import joblib
import numpy

name = input("Enter Employee Name		: ")
exp = float(input("Enter Employee Experience 	: "))

model = joblib.load('salary.pk1')
print("\n")
print("Name			: ", name)
print("Year of Experience	: ", exp)
sal = model.predict([[exp]])
print("Salary			: ", sal)
