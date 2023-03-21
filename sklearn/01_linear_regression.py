import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error
#importing diabetes datasets
diabetes = datasets.load_diabetes()
#observing the datasets
# print(diabetes)
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])
# print(diabetes.data)
# print(diabetes.target)
# print(diabetes.DESCR)
diabetes_x = diabetes.data[:,np.newaxis,2]
# diabetes_x = diabetes.data
print(diabetes_x)
diabetes_x_train = diabetes_x[:-50]
diabetes_y_train = diabetes.target[:-50]
diabetes_x_test = diabetes_x[-50:]
diabetes_y_test = diabetes.target[-50:]

#traing the ml model
model = linear_model.LinearRegression()
model.fit(diabetes_x_train,diabetes_y_train)
diabetes_y_predict = model.predict(diabetes_x_test)
print("mean-squared error is: ",mean_squared_error(diabetes_y_test,diabetes_y_predict))
print("weights: ",model.coef_)
print("intercept: ",model.intercept_)
plt.scatter(diabetes_x_test,diabetes_y_test)
plt.plot(diabetes_x_test,diabetes_y_predict)
plt.show()


