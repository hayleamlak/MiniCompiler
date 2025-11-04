from lexer.lexer import Lexer
from parser.parser import Parser
from interpreter.interpreter import Interpreter

def run_file(file_path):
    with open(file_path, 'r') as f:
        code = f.read()

    lexer = Lexer(code)
    parser = Parser(lexer)
    interpreter = Interpreter()

    while parser.current_token.type != 'EOF':
        ast = parser.parse()
        if ast:
            interpreter.visit(ast)

if __name__ == "__main__":
    run_file("examples/example1.txt")
