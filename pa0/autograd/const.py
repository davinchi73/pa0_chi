# IMPORTS
from expr import Expression, ExpressionType


class Constant(Expression):
    def __init__(self: ExpressionType, val: float) -> None:
            self.val = float(val)

    def __str__(self):
        val = str(self.val)
        return f"({val})"
    
    def __repr__(self):
        val = str(self.val)
        return f"(Constant({val}))"
    
    def differentiate(self: ExpressionType) -> ExpressionType:
        return Constant(0.0)

    def eval(self: ExpressionType,
             x: float) -> float:
        return self.val

    def deepcopy(self: ExpressionType) -> ExpressionType:
        return Constant(self.val)