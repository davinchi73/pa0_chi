# IMPORTS
from typing import Type
import numpy as np

# TYPES DECLARED IN THIS MODULE
LassoRegressorType = Type["LassoRegressor"]


class LassoRegressor(object):
    def __init__(self: LassoRegressorType,
                 num_features: int,             # the number of features each example has
                 regularizer_coeff: float = 1   # the coefficient for the l-1 regularization term in the loss function
                 ) -> None:
        self.w: np.ndarray = np.random.randn(num_features, 1)   # the params of the model
        self.regularizer_coeff: float = regularizer_coeff

    def predict(self: LassoRegressorType,
                X: np.ndarray) -> np.ndarray:
        """
            A method to calculate predictions using lasso regression.
            @param X: the matrix of input examples. Has shape (num_examples, num_features))
            @return np.ndarray: the matrix of predictions. Has shape (num_examples, 1)
        """
        return X @ self.w

    def loss(self: LassoRegressorType,
             Y_hat: np.ndarray,
             Y_gt: np.ndarray) -> float:
        """
            A method to calculate the loss function for lasso regression.
            @param Y_hat: the matrix of predictions. Has shape (num_examples, 1)
            @param Y_gt: the matrix of ground truth. Has shape (num_examples, 1)
            @return float: the lasso regression loss function evaluated at Y_hat, Y_gt
        """
        # w = (Y_hat - Y_gt) + self.regularizer_coeff(sum of abs value weights, w)
        # (Y_hat - Y_gt) = sum of all y^-ygt's squared (least squares)
        ls = (np.sum((Y_hat - Y_gt) ** 2))
        lamb = self.regularizer_coeff
        sum_abs_w = (np.sum(np.abs(self.w)))
        return float((ls) + ((lamb) * (sum_abs_w)))

    def grad(self: LassoRegressorType,
             X: np.ndarray,
             Y_gt: np.ndarray) -> np.ndarray:
        """
            A method to calculate the gradient of the lasso loss function with respect to the parameters 'self.w'
            @param X: the matrix of input examples. Has shape (num_examples, num_features)
            @param Y_gt: the matrix of ground truth. Has shape (num_features, 1)
            @return np.ndarray: the gradient of the lasso loss function with respect to 'self.w'. Has shape (num_features, 1)
        """
        # 2*X.T * (Y_hat - Y_gt) + 2(self.regularizer_coeff)(self.w) --> w sign function
        Y_hat = self.predict(X)
        XT2 = (2) * (X.T)
        left = (XT2) @ (Y_hat - Y_gt)
        right = (self.regularizer_coeff) * (np.sign(self.w))
        return (left) + (right)