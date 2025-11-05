from lexer.lexer import Lexer
from parser.parser import Parser
from interpreter.interpreter import Interpreter

def run_file(file_path):
    try:
        with open(file_path, 'r') as f:
            code = f.read()

        lexer = Lexer(code)
        parser = Parser(lexer)
        interpreter = Interpreter()

        # Run all statements and get combined output
        return interpreter.run(parser)

    except Exception as e:
        return f"Error: {e}"
