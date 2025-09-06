# SYSTEM IMPORTS
from typing import Type
from enum import Enum
from expr import Expression, ExpressionType


OpType = Type["Op"]

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
    
    