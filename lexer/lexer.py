# lexer.py

# Token types
INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, ASSIGN, PRINT, IDENTIFIER, EOF, \
IF, ELSE, FOR, TO, LBRACE, RBRACE, EQ, NE, LT, GT, LTE, GTE = (
    'INTEGER','PLUS','MINUS','MUL','DIV','LPAREN','RPAREN','ASSIGN','PRINT','IDENTIFIER','EOF',
    'IF','ELSE','FOR','TO','LBRACE','RBRACE','EQ','NE','LT','GT','LTE','GTE'
)

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = text[self.pos] if text else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def identifier(self):
        result = ''
        while self.current_char and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        if result in ('print','if','else','for','to'):
            return Token(result.upper(), result)
        return Token(IDENTIFIER, result)

    def integer(self):
        result = ''
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(INTEGER, int(result))

    def get_next_token(self):
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return self.integer()
            if self.current_char.isalpha():
                return self.identifier()
            if self.current_char == '+':
                self.advance()
                return Token(PLUS,'+')
            if self.current_char == '-':
                self.advance()
                return Token(MINUS,'-')
            if self.current_char == '*':
                self.advance()
                return Token(MUL,'*')
            if self.current_char == '/':
                self.advance()
                return Token(DIV,'/')
            if self.current_char == '(':
                self.advance()
                return Token(LPAREN,'(')
            if self.current_char == ')':
                self.advance()
                return Token(RPAREN,')')
            if self.current_char == '{':
                self.advance()
                return Token(LBRACE,'{')
            if self.current_char == '}':
                self.advance()
                return Token(RBRACE,'}')
            if self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(EQ,'==')
                return Token(ASSIGN,'=')
            if self.current_char == '!':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(NE,'!=')
                raise Exception("Invalid character '!'")
            if self.current_char == '<':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(LTE,'<=')
                return Token(LT,'<')
            if self.current_char == '>':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(GTE,'>=')
                return Token(GT,'>')
            raise Exception(f"Invalid character: {self.current_char}")
        return Token(EOF, None)
