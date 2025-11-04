# interpreter/interpreter.py

from parser.parser import BinOp, Num, Var, Assign, Print

class Interpreter:
    def __init__(self):
        self.env = {}
        self.output = ""

    def visit(self, node):
        if isinstance(node, Num):
            return node.value

        elif isinstance(node, Var):
            if node.name in self.env:
                return self.env[node.name]
            else:
                raise Exception(f"Variable '{node.name}' not defined")

        elif isinstance(node, BinOp):
            left = self.visit(node.left)
            right = self.visit(node.right)
            if node.op.type == 'PLUS':
                return left + right
            elif node.op.type == 'MINUS':
                return left - right
            elif node.op.type == 'MUL':
                return left * right
            elif node.op.type == 'DIV':
                return left / right

        elif isinstance(node, Assign):
            value = self.visit(node.value)
            self.env[node.name] = value
            return value

        elif isinstance(node, Print):
            value = self.visit(node.expr)
            self.output += str(value) + "\n"
            return value

        else:
            raise Exception(f"Unknown node: {type(node)}")

    def run(self, parser):
        while parser.current_token.type != 'EOF':
            node = parser.parse()
            if node:
                self.visit(node)
        return self.output.strip()
