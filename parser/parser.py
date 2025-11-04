# parser/parser.py

from lexer.lexer import Token, INTEGER, PLUS, MINUS, MUL, DIV, ASSIGN, PRINT, IDENTIFIER, EOF

# AST nodes
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

    # factor : INTEGER | IDENTIFIER
    def factor(self):
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token.value)
        elif token.type == IDENTIFIER:
            self.eat(IDENTIFIER)
            return Var(token.value)

    # term : factor ((MUL | DIV) factor)*
    def term(self):
        node = self.factor()
        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    # expr : term ((PLUS | MINUS) term)*
    def expr(self):
        node = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)
            node = BinOp(left=node, op=token, right=self.term())
        return node

    # statement : IDENTIFIER ASSIGN expr | PRINT expr
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

    # parse : statement (for now, one statement at a time)
    def parse(self):
        return self.statement()
