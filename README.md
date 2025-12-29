# MiniCompiler

A compact educational compiler/interpreter for a tiny expression language. It includes a lexer, recursive-descent parser, AST nodes, interpreter, and a minimal Tkinter IDE for quick experimentation.

## Requirements
- Python 3.8+ (standard library only)

## Language at a glance
- Numbers (ints), identifiers, arithmetic: `+ - * /`
- Comparisons: `== != < > <= >=`
- Assignment: `x = expr`
- Print: `atim expr` (localized)
- Conditionals: `kehone condition { ... } kalhone { ... }`
- Loops: `le i = start eske end { ... }` (inclusive range)
- Booleans: `negne` (true), `aydele` (false)
- Strings: double-quoted literals

### Localized keywords
| Purpose | Keyword  |
| ------- | -------- |
| print   | `atim`   |
| if      | `kehone` |
| else    | `kalhone`|
| for     | `le`     |
| to      | `eske`   |
| true    | `negne`  |
| false   | `aydele` |

### Example program (all features)
```
title = "demo"
count = 3
sum = 0
flag = negne

atim "-- start --"

kehone flag {
	atim "flag is true"
}

le i = 1 eske count {
	sum = sum + i
	atim i
}



kehone avg >= 2 {
	atim "avg ok"
```
title = "demo"
count = 3
sum = 0
flag = negne

atim "-- start --"

kehone flag {
    atim "flag is true"
}

le i = 1 eske count {
    sum = sum + i
    atim i
}

kehone x > 1 {

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
	atim "ok"
}
'@ | Set-Content temp_input.txt
python -c "from main import run_file; print(run_file('temp_input.txt'))"
```

## Project layout
- lexer/lexer.py — tokenizer and keyword map
- parser/parser.py — AST nodes and recursive-descent parser
- interpreter/interpreter.py — evaluator for statements/expressions
- ide.py — minimal Tkinter IDE
- main.py — helper to run files (run_file(path)) from code/CLI
- examples/ — sample programs (all_in_one.txt, strings.txt, etc.)

## Build a standalone IDE executable (optional)
```powershell
pip install pyinstaller
pyinstaller --onefile --noconsole --icon=assets/app.ico ide.py
```
Output lands in dist/ide.exe. Remove --icon if the icon file is unavailable.

## Troubleshooting
- python not found: ensure the Python 3.8+ install is on PATH.
- Tkinter errors: use the standard Python installer that bundles Tk/Tcl.
- Paths with spaces: always quote paths (e.g., "C:\Users\USER\garbage\python project\MiniCompiler").
- IDE errors: copy the stack trace/output; use the CLI run command to isolate issues.

