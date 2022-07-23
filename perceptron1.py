import numpy as np


class Perceptron:

    def __init__(self, learning_rate, n_iters):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_func = self._unit_signum_func
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # init parameters
        self.weights = np.zeros(n_features)
        self.bias = 0

        y_ = np.array([1 if i > 0 else -1 for i in y])

        for i in range(self.n_iters):
            
            for idx, x_i in enumerate(X):

                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)
                
                # Perceptron update rule
                update = self.lr * (y_[idx] - y_predicted)

                self.weights += update * x_i
                self.bias += update
        print(self.weights)
        print(self.bias)

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation_func(linear_output)
        return y_predicted

    def _unit_signum_func(self, x):
        return np.where(x>=0, 1, -1)
        
def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

X_train = np.array([[2.1,5], [2.1,-5],[1.5,5],[1.5,-5]])
y_train = np.array([[1],[1],[-1],[-1]])

p1 = Perceptron(0.01,1000)
p1.fit(X_train, y_train)
print(p1.predict([[1,3]]))
input('bye')
