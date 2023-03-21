from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
#loading the data
iris = datasets.load_iris()
print(iris.keys())
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
# print(iris.DESCR)
features = iris.data
labels = iris.target
# print(features)
# print(labels)
clf = KNeighborsClassifier()
clf.fit(features,labels)
predict_flower = clf.predict([[2,2,2,2]])
predict_flower = clf.predict([[3,3,3,3]])
print(predict_flower)
# - class:
#               0  - Iris-Setosa
#               1  - Iris-Versicolour
#               2  - Iris-Virginica