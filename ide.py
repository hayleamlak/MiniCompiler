# ide.py
import tkinter as tk
from tkinter import filedialog, messagebox
from lexer.lexer import Lexer
from parser.parser import Parser
from interpreter.interpreter import Interpreter

def run_code():
    code = text_editor.get("1.0", tk.END)
    if not code.strip():
        messagebox.showwarning("Warning", "Code editor is empty!")
        return
    
    try:
        lexer = Lexer(code)
        parser = Parser(lexer)
        interpreter = Interpreter()
        result = interpreter.visit(parser.parse())
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, str(result))
    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Error: {e}")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as f:
            code = f.read()
        text_editor.delete("1.0", tk.END)
        text_editor.insert(tk.END, code)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as f:
            f.write(text_editor.get("1.0", tk.END))

# GUI setup
root = tk.Tk()
root.title("MiniCompiler IDE")
root.geometry("900x600")
root.configure(bg="#20232a")

# Buttons
frame = tk.Frame(root, bg="#20232a")
frame.pack(fill="x", pady=5)

tk.Button(frame, text="Open", command=open_file, bg="#61dafb").pack(side="left", padx=5)
tk.Button(frame, text="Save", command=save_file, bg="#61dafb").pack(side="left", padx=5)
tk.Button(frame, text="Run", command=run_code, bg="#61dafb").pack(side="left", padx=5)

# Editor area
text_editor = tk.Text(root, height=20, bg="#282c34", fg="white", insertbackground="white", font=("Consolas", 12))
text_editor.pack(fill="both", expand=True, padx=10, pady=5)

# Output area
output_box = tk.Text(root, height=10, bg="#1e1e1e", fg="#00ff88", font=("Consolas", 11))
output_box.pack(fill="x", padx=10, pady=5)

root.mainloop()
