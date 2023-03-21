#implementing the linear regression
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

data_x  = np.array([[1],[2],[3]])
data_y = np.array([3,2,4])

#training a model
model = linear_model.LinearRegression()
model.fit(data_x,data_y)
data_y_predict = model.predict(data_x)
print("mean-squared error is: ",mean_squared_error(data_x,data_y))
print("weights: ",model.coef_)
print("intercept: ",model.intercept_)
plt.scatter(data_x,data_y)
plt.plot(data_x,data_y_predict)
plt.show()
