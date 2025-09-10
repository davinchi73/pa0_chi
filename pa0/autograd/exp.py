# IMPORTS
from .expr import Expression, ExpressionType
from .binop import BinaryOp, Op
import math

class Exp(Expression):
    def __init__(self: ExpressionType, arg: Expression) -> None:
        self.arg = arg

    def __str__(self):
        arg = str(self.arg)
        return f"exp({arg})"
    
    def __repr__(self):
        arg = str(self.arg)
        return f"Exp({repr(arg)})"

    def differentiate(self: ExpressionType) -> ExpressionType:
        ddx = self.arg.differentiate()
        return BinaryOp(ddx, Op.MUL, Exp(self.arg))

    def eval(self: ExpressionType,
             x: float) -> float:
        return math.exp(self.arg.eval(x))

    def deepcopy(self: ExpressionType) -> ExpressionType:
        return Exp(self.arg.deepcopy())