How to Use

Use the File menu to create, open, or save files.

Write code in the editor. Example syntax supported:

x = 10
y = 20
print x + y
print x * 2

Click Run Code in the Run menu to execute your code. Output will appear in the terminal at the bottom.

Toggle the terminal or sidebar using the View menu if needed.

Example Code
a = 5
b = 10
print a + b
c = a * b
print c


Expected output in the terminal:

15
50

Project Structure
MiniCompiler/
│
├─ ide.py                  # Main Tkinter IDE
├─ main.py                 # Run file logic
├─ lexer/
│  └─ lexer.py             # Lexer/tokenizer
├─ parser/
│  └─ parser.py            # Parser/AST
├─ interpreter/
│  └─ interpreter.py       # Interpreter
├─ assets/
│  └─ app.ico              # Application icon
└─ dist/                   # Compiled exe (after PyInstaller)

Compiling to Executable

Ensure PyInstaller is installed:

pip install pyinstaller


Run the following command to generate a standalone executable:

pyinstaller --onefile --noconsole --icon=assets/app.ico ide.py


The ide.exe file will be located in the dist/ folder.

Notes

This IDE currently supports basic arithmetic, variable assignment, and print statements.

All output from multiple print statements is accumulated in the terminal.

Designed for educational and experimental purposes.

Dark theme inspired by VS Code.