# IMPORTS
from typing import Type
from enum import Enum
from .expr import Expression, ExpressionType


OpType = Type["Op"]

# given Op class
class Op(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4

    def __str__(self: OpType) -> str:
        op_str: str = None
        if self == Op.ADD:
            op_str = "+"
        elif self == Op.SUB:
            op_str = "-"
        elif self == Op.MUL:
            op_str = "*"
        elif self == Op.DIV:
            op_str = "/"
        else:
            raise ValueError("ERROR: unknown op [{0}]".format(self))
        return op_str
    
    def __repr__(self: OpType) -> str:
        return self.__str__()

# BinaryOp
class BinaryOp(Expression):

    def __init__(self: ExpressionType, lhs: Expression, op: Op, rhs: Expression):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs

    def __str__(self):
        l = str(self.lhs)
        r = str(self.rhs)
        op = str(self.op) 

        return f"{l} {op} {r}"

    def __repr__(self):
        return f"({repr(self)})"

    def differentiate(self) -> ExpressionType:

        from .pow import Power #(self: ExpressionType, base: Expression, exp: float)

        rhsddx = self.rhs.differentiate()
        lhsddx = self.lhs.differentiate()

        if self.op == Op.ADD:
            return BinaryOp(lhsddx, Op.ADD, rhsddx)
        
        elif self.op == Op.SUB:
            return BinaryOp(lhsddx, Op.SUB, rhsddx)
        
        elif self.op == Op.MUL:
            right_term = BinaryOp(self.lhs, Op.MUL, rhsddx)
            left_term = BinaryOp(lhsddx, Op.MUL, self.rhs)
            return BinaryOp(left_term, Op.ADD, right_term)
        
        elif self.op == Op.DIV:
            lhTOP = BinaryOp(self.rhs, Op.MUL, lhsddx)
            rhTOP = BinaryOp(self.lhs, Op.MUL, rhsddx)
            denominator = Power(self.rhs, 2.0)
            numerator = BinaryOp(lhTOP, Op.SUB, rhTOP)
            return BinaryOp(numerator, Op.DIV, denominator)

        else:
            raise ValueError("ERROR: unknown op [{0}]".format(self))     
    
    def eval(self, x):
        right = self.rhs.eval(x)
        left = self.lhs.eval(x)

        if self.op == Op.ADD:
            return left + right
        
        elif self.op == Op.SUB:
            return left - right

        elif self.op == Op.MUL:
            return left * right
            
        elif self.op == Op.DIV:
            return left / right

        else:
            raise ValueError("ERROR: unknown op [{0}]".format(self))
    
    def deepcopy(self) -> ExpressionType:
        return BinaryOp(self.lhs.deepcopy(), self.op, self.rhs.deepcopy())