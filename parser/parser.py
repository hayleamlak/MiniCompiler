# parser/parser.py

from lexer.lexer import *

# -------------------------
# AST Nodes
# -------------------------
class Num:
    def __init__(self, value): self.value = value

class Var:
    def __init__(self, name): self.name = name

class Bool:
    def __init__(self, value): self.value = value

class Str:
    def __init__(self, value): self.value = value

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Print:
    def __init__(self, expr): self.expr = expr

class IfNode:
    def __init__(self, condition, true_block, false_block=None):
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

class ForNode:
    def __init__(self, var, start, end, block):
        self.var = var
        self.start = start
        self.end = end
        self.block = block

# -------------------------
# Parser
# -------------------------
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f"Unexpected token {self.current_token}, expected {token_type}")

    def factor(self):
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token.value)
        elif token.type == TRUE:
            self.eat(TRUE)
            return Bool(True)
        elif token.type == FALSE:
            self.eat(FALSE)
            return Bool(False)
        elif token.type == STRING:
            self.eat(STRING)
            return Str(token.value)
        elif token.type == IDENTIFIER:
            self.eat(IDENTIFIER)
            return Var(token.value)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node
        else:
            raise Exception(f"Unexpected factor: {token}")

    def term(self):
        node = self.factor()
        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            self.eat(token.type)
            node = BinOp(node, token, self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.current_token.type in (PLUS, MINUS, EQ, NE, LT, GT, LTE, GTE):
            token = self.current_token
            self.eat(token.type)
            node = BinOp(node, token, self.term())
        return node

    def statement(self):
        token = self.current_token
        if token.type == IDENTIFIER:
            var_name = token.value
            self.eat(IDENTIFIER)
            self.eat(ASSIGN)
            value = self.expr()
            return Assign(var_name, value)
        elif token.type == PRINT:
            self.eat(PRINT)
            value = self.expr()
            return Print(value)
        elif token.type == IF:
            return self.parse_if()
        elif token.type == FOR:
            return self.parse_for()
        else:
            raise Exception(f"Invalid statement: {token}")

    def parse_if(self):
        self.eat(IF)
        condition = self.expr()
        self.eat(LBRACE)
        true_block = self.parse_block()
        self.eat(RBRACE)
        false_block = None
        if self.current_token.type == ELSE:
            self.eat(ELSE)
            self.eat(LBRACE)
            false_block = self.parse_block()
            self.eat(RBRACE)
        return IfNode(condition, true_block, false_block)

    def parse_for(self):
        self.eat(FOR)
        var_name = self.current_token.value
        self.eat(IDENTIFIER)
        self.eat(ASSIGN)
        start = self.expr()
        self.eat(TO)
        end = self.expr()
        self.eat(LBRACE)
        block = self.parse_block()
        self.eat(RBRACE)
        return ForNode(var_name, start, end, block)

    def parse_block(self):
        nodes = []
        while self.current_token.type not in (RBRACE, EOF):
            nodes.append(self.statement())
        return nodes

    def parse(self):
        if self.current_token.type == 'EOF':
            return None
        return self.statement()
