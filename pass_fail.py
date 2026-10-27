from sklearn.neighbors import KNeighborsClassifier

hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
result = [0, 0, 1, 0, 1, 1, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(hours, result)

print(model.predict([[1.4], [5.2]]))