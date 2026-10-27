from sklearn.linear_model import LinearRegression

hours = [[6], [5], [1], [4], [10], [2], [8], [12], [7], [5], [4], [3]]
marks = [55, 78, 40, 70, 90, 50, 50, 60, 70, 100, 35, 47]

model = LinearRegression()
model.fit(hours, marks)

print(model.predict([[7]]))
print(model.coef_)