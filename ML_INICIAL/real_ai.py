# https://towardsdatascience.com/gradient-descent-in-python-a0d07285742f

import numpy as np

def cal_cost(theta,X,y):
    '''
    calculates cost for given X and Y.
    Example of single dimensional X
    theta = vector of thetas
    X = row of X's np.zeros((2,j))
    Y = actual y's np.zeros((2,j))

    where:
        j is the no of features
    '''
    m = len(y)

    predictions = X.dot(theta)
    cost = (1/(2*m))*np.sum(np.square(predictions - y))
    return cost


def gradient_descent(X, y, theta, learning_rate=0.01, iterations=100):
    '''
    X = Matrix of X wich added bias units (1s ?)
    y = vector of Y
    theta = Vector of thetas np.random.randn(j,1)
    learning_rate
    iterations

    Return the final theta vector and array of cost history over
    no iterations
    '''

    m = len(y)
    cost_history = np.zeros(iterations)
    theta_history = np.zeros((iterations,2))
    for it in range(iterations):

        prediction = np.dot(X,theta)

        theta = theta - (1/m)*learning_rate*(X.T.dot((prediction - y)))
        theta_history[it,:] = theta.T
        cost_history[it] = cal_cost(theta,X,y)

    return theta, cost_history, theta_history


# TESTER
v = np.array([1,2,3])
w = np.array([1,2,3])

print(v.dot(w.T))
j =10
X = np.zeros((2,j))
#print(X)
print(X.T)

theta = np.random.randn(j,1)

print(theta)



