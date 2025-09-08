# IMPORTS
from .expr import Expression, ExpressionType
from .const import Constant
from .binop import BinOp, Op
import math


class Cos(Expression):
    def __init__(self: ExpressionType, val: float) -> None:
            self.val = float(val)

    def __str__(self):
        arg = str(self.arg)
        return f"(cos({arg}))"
    
    def __repr__(self):
        arg = str(self.arg)
        return f"(Cos({repr(arg)}))"
    
    def differentiate(self: ExpressionType) -> ExpressionType:
        from sin import Sin

        ddx = self.arg.differentiate()
        const = Constant(-1.0)
        comb = BinOp(ddx, Op.MUL, Sin(self.arg))
        return BinOp(const, Op.MUL, comb)

    def eval(self: ExpressionType,
             x: float) -> float:
        return float(math.cos(self.arg.eval(x)))

    def deepcopy(self: ExpressionType) -> ExpressionType:
        return Cos(self.arg.deepcopy())