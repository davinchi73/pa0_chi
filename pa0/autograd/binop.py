# SYSTEM IMPORTS
from typing import Type
from enum import Enum
from expr import Expression, ExpressionType


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
        pass

    def __repr__(self):
        pass

    def differentiate(self) -> ExpressionType:

        from pow import Power #(self: ExpressionType, base: Expression, exp: float)

        if self.op == Op.ADD:
            rhsddx = self.rhs.differentiate()
            lhsddx = self.lhs.differentiate()
            return BinaryOp(lhsddx, Op.ADD, rhsddx)
        
        elif self.op == Op.SUB:
            rhsddx = self.rhs.differentiate()
            lhsddx = self.lhs.differentiate()
            return BinaryOp(lhsddx, Op.SUB, rhsddx)
        
        elif self.op == Op.MUL:
            rhsddx = self.rhs.differentiate()
            lhsddx = self.lhs.differentiate()

            right_term = BinaryOp(self.lhs, Op.MUL, rhsddx)
            left_term = BinaryOp(lhsddx, Op.MUL, self.rhs)
            return BinaryOp(left_term, Op.ADD, right_term)
        
        elif self.op == Op.DIV:

        else:
            raise ValueError("ERROR: unknown op [{0}]".format(self))     
    
    def eval(self, x):
        
    
    def deepcopy(self) -> ExpressionType:
        