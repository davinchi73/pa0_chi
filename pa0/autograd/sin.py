# SYSTEM IMPORTS
from typing import Type
from expr import Expression, ExpressionType
from cos import Cos
from binop import BinaryOp, Op
import math

class Sin(Expression):
    def __init__(self: ExpressionType, arg: Expression) -> None:
            self.arg = arg

    def __str__(self):
        return str(self.val)
    
    def __repr__(self):
        return f"Constant:({self.val})"
    
    def differentiate(self: ExpressionType) -> ExpressionType:
        ddx = self.arg.differentiate()
        return BinaryOp(ddx, Op.MUL, Cos(self.arg))

    def eval(self: ExpressionType,
             x: float) -> float:
        return math.sin(self.arg.eval(x))

    def deepcopy(self: ExpressionType) -> ExpressionType:
        return Sin(self.arg.deepcopy())