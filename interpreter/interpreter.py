# interpreter.py

from parser.parser import BinOp, Num, Var, Assign, Print, IfNode, ForNode

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
            raise Exception(f"Variable '{node.name}' not defined")
        elif isinstance(node, BinOp):
            left = self.visit(node.left)
            right = self.visit(node.right)
            t = node.op.type
            if t == 'PLUS': return left + right
            elif t == 'MINUS': return left - right
            elif t == 'MUL': return left * right
            elif t == 'DIV': return left / right
            elif t == 'EQ': return left == right
            elif t == 'NE': return left != right
            elif t == 'LT': return left < right
            elif t == 'GT': return left > right
            elif t == 'LTE': return left <= right
            elif t == 'GTE': return left >= right
        elif isinstance(node, Assign):
            value = self.visit(node.value)
            self.env[node.name] = value
            return value
        elif isinstance(node, Print):
            value = self.visit(node.expr)
            self.output += str(value) + "\n"
            return value
        elif isinstance(node, IfNode):
            cond = self.visit(node.condition)
            if cond:
                for stmt in node.true_block:
                    self.visit(stmt)
            elif node.false_block:
                for stmt in node.false_block:
                    self.visit(stmt)
            return None
        elif isinstance(node, ForNode):
            start = self.visit(node.start)
            end = self.visit(node.end)
            for i in range(int(start), int(end) + 1):
                self.env[node.var] = i
                for stmt in node.block:
                    self.visit(stmt)
            return None
        else:
            raise Exception(f"Unknown node type: {type(node)}")

    def run(self, parser):
        while parser.current_token.type != 'EOF':
            node = parser.parse()
            if node:
                self.visit(node)
        return self.output.strip()
