from lexer.lexer import Lexer
from parser.parser import Parser, Num, Var, Bool, Str, BinOp, Assign, Print, IfNode, ForNode
from interpreter.interpreter import Interpreter


def _tokenize(code):
    lex = Lexer(code)
    tokens = []
    tok = lex.get_next_token()
    while tok.type != 'EOF':
        tokens.append(tok)
        tok = lex.get_next_token()
    return tokens


def _parse_all(code):
    parser = Parser(Lexer(code))
    nodes = []
    while parser.current_token.type != 'EOF':
        node = parser.parse()
        if node:
            nodes.append(node)
    return nodes

def _fmt_token(tok):
    return f"{tok.type}:{tok.value}"


def _fmt_ast(node, indent=0):
    pad = '  ' * indent
    if isinstance(node, Num):
        return f"{pad}Num({node.value})"
    if isinstance(node, Bool):
        return f"{pad}Bool({node.value})"
    if isinstance(node, Str):
        return f"{pad}Str(\"{node.value}\")"
    if isinstance(node, Var):
        return f"{pad}Var({node.name})"
    if isinstance(node, BinOp):
        return "\n".join([
            f"{pad}BinOp({node.op.type})",
            _fmt_ast(node.left, indent + 1),
            _fmt_ast(node.right, indent + 1),
        ])
    if isinstance(node, Assign):
        return "\n".join([
            f"{pad}Assign({node.name})",
            _fmt_ast(node.value, indent + 1),
        ])
    if isinstance(node, Print):
        return "\n".join([
            f"{pad}Print",
            _fmt_ast(node.expr, indent + 1),
        ])
    if isinstance(node, IfNode):
        lines = [f"{pad}If"]
        lines.append(_fmt_ast(node.condition, indent + 1))
        lines.append(f"{pad}  TrueBlock")
        for stmt in node.true_block:
            lines.append(_fmt_ast(stmt, indent + 2))
        if node.false_block:
            lines.append(f"{pad}  FalseBlock")
            for stmt in node.false_block:
                lines.append(_fmt_ast(stmt, indent + 2))
        return "\n".join(lines)
    if isinstance(node, ForNode):
        lines = [f"{pad}For({node.var})"]
        lines.append(_fmt_ast(node.start, indent + 1))
        lines.append(_fmt_ast(node.end, indent + 1))
        lines.append(f"{pad}  Body")
        for stmt in node.block:
            lines.append(_fmt_ast(stmt, indent + 2))
        return "\n".join(lines)
    return f"{pad}{type(node).__name__}"


def run_file(file_path):
    """
    Run a program and return a presentation-friendly pipeline output with:
    - Lexer tokens
    - Parsed AST
    - Interpreter output
    """
    try:
        with open(file_path, 'r') as f:
            code = f.read()

        tokens = _tokenize(code)
        ast_nodes = _parse_all(code)
        interpreter = Interpreter()
        program_output = interpreter.run_nodes(ast_nodes)

        lexer_section = "\n".join(_fmt_token(t) for t in tokens) or "<no tokens>"
        ast_section = "\n".join(_fmt_ast(n) for n in ast_nodes) or "<empty program>"
        output_section = program_output if program_output else "<no output>"

        return "\n".join([
            "--- LEXER OUTPUT ---",
            lexer_section,
            "",
            "--- AST ---",
            ast_section,
            "",
            "--- PROGRAM OUTPUT ---",
            output_section,
        ])

    except Exception as e:
        return f"Error: {e}"
