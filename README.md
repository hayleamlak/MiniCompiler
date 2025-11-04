# MiniCompiler

A simple Python compiler demonstrating core compiler concepts: **lexer**, **parser**, and **interpreter**.  
Supports variable assignments, arithmetic, and print statements.

---

## **Project Structure**

MiniCompiler/
├─ lexer/ # Tokenizer
│ └─ lexer.py
├─ parser/ # AST builder
│ └─ parser.py
├─ interpreter/ # Executes AST
│ └─ interpreter.py
├─ examples/ # Sample programs
│ └─ example1.txt
├─ main.py # Entry point
└─ README.md

yaml
Copy code

---

## **Usage**

1. Edit `examples/example1.txt`:

```text
x = 10 + 5
y = x * 2
print y
z = y - 5
print z
Run the compiler:

bash
Copy code
python main.py
Output:

Copy code
30
25
Future Enhancements
Loops and conditionals

Multi-line terminal input (REPL)

Functions and advanced expressions

Better error handling