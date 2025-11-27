# MiniCompiler

A small educational compiler/interpreter written in Python. It demonstrates a simple lexer, parser, AST, and interpreter for a tiny expression language with variables and `print` statements. A minimal Tkinter-based IDE (`ide.py`) is included for editing and running code.

## Features
- Lexer supporting integers, identifiers, operators, parentheses, and the `print` keyword
- Recursive-descent parser producing a small AST (binary ops, numbers, variables, assignments, print)
- Interpreter that evaluates statements and captures `print` output
- Minimal IDE (`ide.py`) with syntax highlighting, line numbers, and an output pane

## Requirements
- Python 3.8+ (no external packages required)

## Quick start

Launch the IDE:

```powershell
python ide.py
```

Run the interpreter programmatically:

```python
from main import run_file
print(run_file('examples/example1.txt'))
```

`main.run_file` returns a string with the interpreter output or an error message.

## Language examples

- Assignment:

```
x = 10
```

- Arithmetic expressions:

```
y = (x + 3) * 2
```

- Print:

```
print y
```

### Sample program

```
a = 2
b = a * 5 + 3
print b
```

Expected output:

```
13
```

## Project layout
- `lexer/lexer.py` — tokenizer
- `parser/parser.py` — parser + AST node classes
- `interpreter/interpreter.py` — evaluator
- `ide.py` — simple Tkinter IDE
- `main.py` — runner that ties lexer/parser/interpreter
- `examples/` — sample files

## Building a standalone IDE executable (optional)

Install PyInstaller if you need a standalone executable:

```powershell
pip install pyinstaller
pyinstaller --onefile --noconsole --icon=assets/app.ico ide.py
```

The `ide.exe` will be in the `dist/` folder.


## Development notes
- Run the IDE: `python ide.py`
- Run a specific example from Python: import `run_file` from `main` and call it with the file path.



.
Contributions and questions welcome
