# IMPORTS
from .expr import Expression, ExpressionType
from .cos import Cos
from .binop import BinaryOp, Op
import math

class Sin(Expression):
    def __init__(self: ExpressionType, arg: Expression) -> None:
            self.arg = arg

    def __str__(self):
        arg = str(self.arg)
        return f"(sin({arg}))"
    
    def __repr__(self):
        arg = str(self.arg)
        return f"(Sin({repr(arg)}))"
    
    def differentiate(self: ExpressionType) -> ExpressionType:
        ddx = self.arg.differentiate()
        return BinaryOp(ddx, Op.MUL, Cos(self.arg))

    def eval(self: ExpressionType,
             x: float) -> float:
        return float(math.sin(self.arg.eval(x)))

    def deepcopy(self: ExpressionType) -> ExpressionType:
        return Sin(self.arg.deepcopy())