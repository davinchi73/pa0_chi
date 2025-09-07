# SYSTEM IMPORTS
from typing import Type
from expr import Expression, ExpressionType
from binop import BinaryOp, Op
import math

class Log(Expression):
    def __init__(self: ExpressionType, arg: Expression) -> None:
        self.arg = arg

    def __str__(self):
        arg = str(self.arg)
        return f"log({arg})"
    
    def __repr__(self):
        arg = str(self.arg)
        return f"Log({repr(arg)})"

    def differentiate(self: ExpressionType) -> ExpressionType:
        ddx = self.arg.differentiate()
        return BinaryOp(ddx, Op.DIV, self.arg)

    def eval(self: ExpressionType,
             x: float) -> float:
        return math.ln(self.arg.eval(x))

    def deepcopy(self: ExpressionType) -> ExpressionType:
        return Log(self.arg.deepcopy())