import ast
import operator

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
}

def compute(expr):
    def _eval(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op_type = type(node.op)
            if op_type in OPERATORS:
                return OPERATORS[op_type](left, right)
            else:
                raise ValueError(f"Operator {op_type} not allowed.")
        elif isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            op_type = type(node.op)
            if op_type in OPERATORS:
                return OPERATORS[op_type](operand)
            else:
                raise ValueError(f"Operator {op_type} not allowed.")
        else:
            raise TypeError(f"Unsupported expression: {node}")
    
    node = ast.parse(expr, mode='eval').body
    return _eval(node)

def calculate(expression):
    try:
        result = compute(expression)
        return result
    except:
        raise ValueError(f"Invalid Expression: {expression}")

def convert(number_type, number):
    number_type = number_type.lower()
    
    if number_type == "binary":
        return bin(number)[2:]
    elif number_type == "hexadecimal":
        return hex(number)[2:]
    elif number_type == "octal":
        return oct(number)[2:]
    else:
        raise ValueError(f"Invalid number type: {number_type}")
    
