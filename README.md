# MiniCompiler

## Project Title
MiniCompiler — tiny educational compiler with a Tkinter IDE.

## Description
A compact playground for a minimal, localized expression language. It includes a lexer, recursive-descent parser, AST nodes, an interpreter, and a lightweight GUI for quickly tokenizing, parsing, and running programs.

## Features
- Localized keywords for print/if/else/for and booleans.
- Lexer, parser, and interpreter written in pure Python 3.8+ (standard library only).
- Tkinter IDE for quick experimentation plus a CLI helper for scripts.
- Inclusive `for` loops, conditionals, arithmetic, comparisons, strings, and booleans.

## Folder Structure
- lexer/lexer.py — tokenizer and keyword map
- parser/parser.py — AST nodes and recursive-descent parser
- interpreter/interpreter.py — evaluator for statements/expressions
- ide.py — minimal Tkinter IDE
- main.py — helper to run files (`run_file(path)`) from code/CLI
- examples/ — sample programs (input1.txt, input2.txt, ...)
- assets/ — icons/assets for the IDE
- build/, dist/ — PyInstaller artifacts (if you build the exe)

## Installation / Setup
1) Install Python 3.8+ and ensure `python` is on PATH. Use the official installer that bundles Tkinter.
2) Clone or unzip the repo, then open a terminal in the project root:
```powershell
git clone https://github.com/hayleamlak/MiniCompiler.git
cd MiniCompiler
# if you already have the folder, just cd into it instead
```
```powershell
cd "C:\Users\USER\garbage\python project\MiniCompiler"
```
3) (Optional) Create/activate a virtual environment:
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```
4) No extra deps are required for core use. For building an executable, install PyInstaller:
```powershell
pip install pyinstaller
```

## Usage
### GUI IDE
```powershell
python ide.py
```
Enter code in the editor pane and run to see tokens, AST, and output.

### Terminal / CLI
- Run an example file:
```powershell
python -c "from main import run_file; print(run_file('examples/input1.txt'))"
```
- Run your own file in the current folder:
```powershell
python -c "from main import run_file; print(run_file('temp_input.txt'))"
```
- Create and run inline code via a heredoc:
```powershell
@'
atim "hello"
x = 2
kehone x > 1 {
    atim "ok"
}
'@ | Set-Content temp_input.txt
python -c "from main import run_file; print(run_file('temp_input.txt'))"
```

## How it Works
- Lexer converts source to tokens and tags localized keywords.
- Parser builds an AST using recursive-descent rules for expressions/statements.
- Interpreter walks the AST, maintaining an environment for variables and executing statements.
- `run_file(path)` wires the pipeline (lex, parse, interpret) for CLI/automation.

## Language at a glance
- Numbers (ints), identifiers, arithmetic: `+ - * /`
- Comparisons: `== != < > <= >=`
- Assignment: `x = expr`
- Print: `atim expr` (localized)
- Conditionals: `kehone condition { ... } kalhone { ... }`
- Loops: `ke i = start eske end { ... }` (inclusive range)
- Booleans: `ewnet` (true), `haset` (false)
- Strings: double-quoted literals

### Localized keywords
| Purpose | Keyword  |
| ------- | -------- |
| print   | `atim`   |
| if      | `kehone` |
| else    | `kalhone`|
| for     | `ke`     |
| to      | `eske`   |
| true    | `ewnet`  |
| false   | `haset`  |

## Code Examples 
Example program covering all features:
```
title = "demo"
count = 3
sum = 0
flag = ewnet

atim "-- start --"

kehone flag {
    atim "flag is true"
}

ke i = 1 eske count {
    sum = sum + i
    atim i
}

avg = sum / count

kehone avg >= 2 {
    atim "avg ok"
} kalhone {
    atim "avg low"
}

kehone title == "demo" {
    atim "title matches"
}

atim sum
atim avg
atim title
atim "-- end --"
```

## Limitations
- Minimal error reporting (parsing/runtime errors are not deeply annotated).
- Integer arithmetic only; no floats or advanced types.
- No user-defined functions; only straight-line code, conditionals, and loops.
- Single-file programs; no imports.

## Future Improvements
- Better diagnostics with line/column info.
- Function definitions and calls.
- Optional float support and more operators.
- Syntax highlighting and linting inside the IDE.
- Unit tests for grammar and interpreter behaviors.

## References
- Python 3.8+ standard library (Tkinter bundled with official installer).
- PyInstaller docs: https://pyinstaller.org/en/stable/ for packaging the IDE.
- Project repo: https://github.com/hayleamlak/MiniCompiler.git

