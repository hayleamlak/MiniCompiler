import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from main import run_file  # Import your compiler logic

# -----------------------
# Syntax highlighting setup
# -----------------------
KEYWORDS = ['print', 'if', 'else', 'while', 'for', 'return', 'function']

def highlight_syntax(text_widget):
    text_widget.tag_remove("keyword", "1.0", tk.END)
    text_widget.tag_remove("number", "1.0", tk.END)
    text_widget.tag_remove("string", "1.0", tk.END)
    
    content = text_widget.get("1.0", tk.END)
    for keyword in KEYWORDS:
        start = "1.0"
        while True:
            pos = text_widget.search(r'\b' + keyword + r'\b', start, stopindex=tk.END, regexp=True)
            if not pos:
                break
            end = f"{pos}+{len(keyword)}c"
            text_widget.tag_add("keyword", pos, end)
            start = end
    
    # Numbers
    start = "1.0"
    while True:
        pos = text_widget.search(r'\d+', start, stopindex=tk.END, regexp=True)
        if not pos:
            break
        end = f"{pos}+{len(text_widget.get(pos,pos+' wordend'))}c"
        text_widget.tag_add("number", pos, end)
        start = end
    
    # Strings
    start = "1.0"
    while True:
        pos = text_widget.search(r'\".*?\"', start, stopindex=tk.END, regexp=True)
        if not pos:
            break
        end = f"{pos}+{len(text_widget.get(pos,pos+' lineend'))}c"
        text_widget.tag_add("string", pos, end)
        start = end

# -----------------------
# Line numbers
# -----------------------
class LineNumbers(tk.Canvas):
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, **kwargs)
        self.text_widget = text_widget
        self.text_widget.bind("<KeyRelease>", self.redraw)
        self.text_widget.bind("<MouseWheel>", self.redraw)
        self.redraw()
    
    def redraw(self, event=None):
        self.delete("all")
        i = self.text_widget.index("@0,0")
        while True:
            dline = self.text_widget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, fill="#888888", font=("Consolas",12))
            i = self.text_widget.index(f"{i}+1line")

# -----------------------
# Main IDE
# -----------------------
class MiniCompilerIDE:
    def __init__(self, root):
        self.root = root
        root.title("MiniCompiler IDE")
        root.geometry("1000x700")
        root.configure(bg="#20232a")

        self.editors = []

        self.create_menu()
       
        self.create_editor_tabs()
        self.create_output_terminal()

    # -----------------------
    # Menu Bar
    # -----------------------
    def create_menu(self):
        self.menu_frame = tk.Frame(self.root, bg="#1e1e1e", height=30)
        self.menu_frame.pack(side="top", fill="x")

        menu_defs = {
            "File": ["New","Open","Save","Save As","Exit"],
            "View": ["Toggle Terminal","Toggle Sidebar"],
            "Go": ["Go to Line","Go to Symbol"],
            "Run": ["Run Code","Stop","Debug"]
        }

        for menu_name, items in menu_defs.items():
            b = tk.Menubutton(self.menu_frame, text=menu_name, bg="#1e1e1e", fg="white",
                              activebackground="#3c3c3c", activeforeground="white", bd=0, padx=10, pady=2)
            b.pack(side="left", padx=2)
            # Hover effect
            b.bind("<Enter>", lambda e, b=b: b.config(bg="#007acc"))
            b.bind("<Leave>", lambda e, b=b: b.config(bg="#1e1e1e"))
            menu = tk.Menu(b, tearoff=0)
            for item in items:
                menu.add_command(label=item, command=lambda i=item: self.menu_action(i))
            b.config(menu=menu)

    def menu_action(self, item):
        if item=="New":
            self.new_tab()
        elif item=="Open":
            self.open_file()
        elif item=="Save":
            self.save_file()
        elif item=="Save As":
            self.save_file_as()
        elif item=="Exit":
            self.root.quit()
        elif item=="Run Code":
            self.run_code()
        elif item=="Toggle Terminal":
            if self.output_frame.winfo_viewable():
                self.output_frame.pack_forget()
            else:
                self.output_frame.pack(fill="x", padx=5,pady=5)
        elif item=="Go to Line":
            line = simpledialog.askinteger("Go to Line","Enter line number:")
            if line:
                editor,_ = self.current_editor()
                editor.mark_set("insert", f"{line}.0")
                editor.see(f"{line}.0")
        else:
            messagebox.showinfo("Info", f"{item} clicked")

    # -----------------------
    # Toolbar
    # -----------------------
   
   
   
   
   
   
   

    # -----------------------
    # Editor Tabs
    # -----------------------
    def create_editor_tabs(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=5, pady=5)
        self.new_tab()

    def new_tab(self, file_path=None):
        frame = tk.Frame(self.notebook)
        text_editor = tk.Text(frame, height=20, bg="#282c34", fg="white",
                              insertbackground="white", font=("Consolas",12))
        text_editor.pack(side="right", fill="both", expand=True, padx=5, pady=5)
        text_editor.bind("<KeyRelease>", lambda e: highlight_syntax(text_editor))

        line_numbers = LineNumbers(frame, text_editor, width=40, bg="#2b2b2b")
        line_numbers.pack(side="left", fill="y")

        self.notebook.add(frame, text=file_path if file_path else "Untitled")
        self.notebook.select(frame)
        self.editors.append((text_editor, file_path))

        if file_path:
            with open(file_path,"r") as f:
                text_editor.insert("1.0", f.read())

    def current_editor(self):
        idx = self.notebook.index(self.notebook.select())
        return self.editors[idx]

    # -----------------------
    # File operations
    # -----------------------
    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
        if path:
            self.new_tab(path)

    def save_file(self):
        editor, path = self.current_editor()
        if path is None:
            self.save_file_as()
        else:
            with open(path,"w") as f:
                f.write(editor.get("1.0", tk.END))

    def save_file_as(self):
        editor, _ = self.current_editor()
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files","*.txt")])
        if path:
            with open(path,"w") as f:
                f.write(editor.get("1.0",tk.END))
            idx = self.notebook.index(self.notebook.select())
            self.editors[idx] = (editor,path)
            self.notebook.tab(idx,text=path.split('/')[-1])

    # -----------------------
    # Output Terminal
    # -----------------------
    def create_output_terminal(self):
        self.output_frame = tk.Frame(self.root,bg="#1e1e1e",height=150)
        self.output_frame.pack(fill="x", padx=5,pady=5)
        self.output_box = tk.Text(self.output_frame,height=8,bg="#1e1e1e",fg="#00ff88",font=("Consolas",11))
        self.output_box.pack(fill="both",expand=True)
        tk.Button(self.output_frame,text="Clear Output",command=lambda:self.output_box.delete("1.0",tk.END),bg="#61dafb").pack(side="right", padx=5)

    # -----------------------
    # Run code
    # -----------------------
    def run_code(self):
        editor,_ = self.current_editor()
        code = editor.get("1.0",tk.END)
        with open("temp_run.txt","w") as f:
            f.write(code)
        result = run_file("temp_run.txt")
        self.output_box.delete("1.0",tk.END)
        self.output_box.insert(tk.END,result)
        self.output_box.see(tk.END)

# -----------------------
# Launch IDE
# -----------------------
if __name__=="__main__":
    root = tk.Tk()
    app = MiniCompilerIDE(root)
    root.mainloop()
