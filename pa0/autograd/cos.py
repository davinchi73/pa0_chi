# SYSTEM IMPORTS
from typing import Type
from expr import Expression, ExpressionType
from const import Constant
from binop import BinaryOp, Op
import math


class Cos(Expression):
    def __init__(self: ExpressionType, val: float) -> None:
            self.val = float(val)

    def __str__(self):
        return str(self.val)
    
    def __repr__(self):
        return f"Constant:({self.val})"
    
    def differentiate(self: ExpressionType) -> ExpressionType:
        from sin import Sin

        ddx = self.arg.differentiate()
        const = Constant(-1.0)
        comb = BinaryOp(ddx, Op.MUL, Sin(self.arg))
        return BinaryOp(const, Op.MUL, comb)

    def eval(self: ExpressionType,
             x: float) -> float:
        return math.cos(self.arg.eval(x))

    def deepcopy(self: ExpressionType) -> ExpressionType:
        return Cos(self.arg.deepcopy())