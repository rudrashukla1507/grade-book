from sklearn.linear_model import LinearRegression

hours = [[6], [5], [1], [4], [10], [2], [8], [12], [7], [5], [4], [3]]
marks = [55, 78, 40, 70, 90, 50, 50, 60, 70, 100, 35, 47]

hours_train = hours[:9]
marks_train = marks[:9]
hours_test = hours[9:]
marks_test = marks[9:]

model = LinearRegression()
model.fit(hours_train, marks_train)

print(model.predict(hours_test))
print(marks_test)