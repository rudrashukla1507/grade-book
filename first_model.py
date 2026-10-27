from sklearn.linear_model import LinearRegression

hours = [[1], [2], [3], [4], [5]]
marks = [35, 50, 60, 72, 85]

model = LinearRegression()
model.fit(hours, marks)

print(model.predict([[6]]))
print(model.predict([[2.5]]))
print(model.coef_)
print(model.intercept_)