# main.py (or run_file.py)
from lexer.lexer import Lexer
from parser.parser import Parser
from interpreter.interpreter import Interpreter

def run_file(file_path):
    """
    Run code from a file and return the final result or error message.
    """
    try:
        with open(file_path, 'r') as f:
            code = f.read()

        lexer = Lexer(code)
        parser = Parser(lexer)
        interpreter = Interpreter()

        result = None
        while parser.current_token.type != 'EOF':
            ast = parser.parse()
            if ast:
                result = interpreter.visit(ast)

        return str(result)  # Always return string for GUI output

    except Exception as e:
        return f"Error: {e}"  # Return errors as strings
