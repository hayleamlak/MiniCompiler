# parser/parser.py

from lexer.lexer import *

# AST Nodes
class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num:
    def __init__(self, value):
        self.value = value

class Var:
    def __init__(self, name):
        self.name = name

class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Print:
    def __init__(self, expr):
        self.expr = expr

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
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            self.eat(token.type)
            node = BinOp(left=node, op=token, right=self.term())
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
        else:
            raise Exception(f"Invalid statement: {token}")

    def parse(self):
        if self.current_token.type == EOF:
            return None
        return self.statement()
