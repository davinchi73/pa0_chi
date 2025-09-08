# IMPORTS
from .expr import Expression, ExpressionType
from .binop import BinOp, Op
from .const import Constant


class Power(Expression):
    def __init__(self: ExpressionType, base: Expression, exp: float) -> None:
            self.base = base
            self.exp = float(exp)

    def __str__(self):
        base = str(self.base)
        exp = str(self.exp)

        return f"({base})^({exp})"
    
    def __repr__(self):
        base = str(self.base)
        exp = str(self.exp)

        return f"(Base({base}))^(Exp({exp}))"
    
    def differentiate(self: ExpressionType) -> ExpressionType:
        new_exp = self.exp - 1.0
        lhs = BinOp(Constant(self.exp), Op.MUL, Power(self.base, new_exp))
        rhs = self.base.differentiate()
        return BinOp(lhs, Op.MUL, rhs)

    def eval(self: ExpressionType,
             x: float) -> float:
        return self.base.eval(x) ** self.exp

    def deepcopy(self: ExpressionType) -> ExpressionType:
        return Power(self.base.deepcopy(), self.exp)