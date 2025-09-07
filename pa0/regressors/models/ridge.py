# SYSTEM IMPORTS
from typing import Type
import numpy as np


# PYTHON PROJECT IMPORTS


# TYPES DECLARED IN THIS MODULE
RidgeRegressorType = Type["RidgeRegressorType"]


# CONSTANTS



class RidgeRegressor(object):
    def __init__(self: RidgeRegressorType,
                 num_features: int,             # the number of features each example has
                 regularizer_coeff: float = 1   # the coefficient for the l-1 regularization term in the loss function
                 ) -> None:
        self.w: np.ndarray = np.random.randn(num_features, 1)   # the params of the model 
        self.regularizer_coeff: float = regularizer_coeff

    def predict(self: RidgeRegressorType,
                X: np.ndarray) -> np.ndarray:
        """
            A method to calculate predictions using ridge regression.
            @param X: the matrix of input examples. Has shape (num_examples, num_features))
            @return np.ndarray: the matrix of predictions. Has shape (num_examples, 1)
        """
        # y^ = Xw --> vector of predictions
        return X @ self.w

    def loss(self: RidgeRegressorType,
             Y_hat: np.ndarray,
             Y_gt: np.ndarray) -> float:
        """
            A method to calculate the loss function for ridge regression.
            @param Y_hat: the matrix of predictions. Has shape (num_examples, 1)
            @param Y_gt: the matrix of ground truth. Has shape (num_examples, 1)
            @return float: the ridge regression loss function evaluated at Y_hat, Y_gt
        """
        # w = (Y_hat - Y_gt) + self.regularizer_coeff(sum of squared weights, w)
        # (Y_hat - Y_gt) = sum of all y^-ygt's squared (least squares)
        ls = (np.sum((Y_hat - Y_gt) ** 2))
        lamb = self.regularizer_coeff
        sum_sq_w = np.sum(np.square(self.w))
        return float((ls) + (lamb*(sum_sq_w)))

    def grad(self: RidgeRegressorType,
             X: np.ndarray,
             Y_gt: np.ndarray) -> np.ndarray:
        """
            A method to calculate the gradient of the ridge loss function with respect to the parameters 'self.w'
            @param X: the matrix of input examples. Has shape (num_examples, num_features)
            @param Y_gt: the matrix of ground truth. Has shape (num_features, 1)
            @return np.ndarray: the gradient of the ridge loss function with respect to 'self.w'. Has shape (num_features, 1)
        """
        return None

