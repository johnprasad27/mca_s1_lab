import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Create CSV
data = {
    'Hours': [1, 2, 2, 3, 4, 5, 6, 7],
    'Marks': [20, 25, 30, 35, 55, 65, 75, 85],
    'Result': ['Fail', 'Fail', 'Fail', 'Fail',
               'Pass', 'Pass', 'Pass', 'Pass']
}

df = pd.DataFrame(data)
df.to_csv('students.csv', index=False)

# Read CSV
df = pd.read_csv('students.csv')

X = df[['Hours', 'Marks']]
y = df['Result']

# Train model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Predict for a new student
new_student = pd.DataFrame({
    'Hours': [5],
    'Marks': [60]
})

prediction = model.predict(new_student)
print("Predicted result:", prediction[0])