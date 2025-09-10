# IMPORTS
from .expr import Expression, ExpressionType
from .const import Constant
from .binop import BinaryOp, Op
import math


class Cos(Expression):
    def __init__(self: ExpressionType, arg: Expression) -> None:
            self.arg = arg

    def __str__(self):
        arg = str(self.arg)
        return f"(cos({arg}))"
    
    def __repr__(self):
        arg = str(self.arg)
        return f"(Cos({repr(arg)}))"
    
    def differentiate(self: ExpressionType) -> ExpressionType:
        from .sin import Sin

        ddx = self.arg.differentiate()
        const = Constant(-1.0)
        sin = Sin(self.arg)
        return BinaryOp(BinaryOp(const, Op.MUL, ddx), Op.MUL, sin)

    def eval(self: ExpressionType,
             x: float) -> float:
        return float(math.cos(self.arg.eval(x)))

    def deepcopy(self: ExpressionType) -> ExpressionType:
        return Cos(self.arg.deepcopy())