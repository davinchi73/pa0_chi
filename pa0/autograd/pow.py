# SYSTEM IMPORTS
from typing import Type
from expr import Expression, ExpressionType
from binop import BinaryOp, Op
from const import Constant


class Power(Expression):
    def __init__(self: ExpressionType, base: Expression, exp: float) -> None:
            self.base = base
            self.exp = exp

    # def __str__(self):
    #     return str(self.val)
    
    # def __repr__(self):
    #     return f"Constant:({self.val})"
    
    def differentiate(self: ExpressionType) -> ExpressionType:
        new_exp = self.exp - 1.0
        lhs = BinaryOp(Constant(self.exp), Op.MUL, Power(self.base, new_exp))
        rhs = self.base.differentiate()
        return BinaryOp(lhs, Op.MUL, rhs)

    def eval(self: ExpressionType,
             x: float) -> float:
        return self.base.eval ** self.exp

    def deepcopy(self: ExpressionType) -> ExpressionType:
        return Power(self.base, self.exp)