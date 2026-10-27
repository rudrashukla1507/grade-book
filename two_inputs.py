from sklearn.linear_model import LinearRegression

inputs = [[1, 40], [2, 40], [3, 60], [4, 60], [5, 80], [6, 80]]
marks = [45, 50, 65, 70, 85, 90]

model = LinearRegression()
model.fit(inputs, marks)

print(model.coef_)
print(model.intercept_)
print(model.predict([[3, 80]]))