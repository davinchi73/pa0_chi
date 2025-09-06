# SYSTEM IMPORTS
from typing import Type
from expr import Expression, ExpressionType
from const import Constant

class Variable(Expression):
    def __init__(self: ExpressionType) -> None:
        pass

    def __str__(self):
        return "x"
    
    def __repr__(self):
        return f"Variable: x"
    
    def differentiate(self: ExpressionType) -> ExpressionType:
        return Constant(1.0)

    def eval(self: ExpressionType,
             x: float) -> float:
        return Constant(x)

    def deepcopy(self: ExpressionType) -> ExpressionType:
        return Variable()