import tkinter as tk

#-Functions-
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("error")
        expression = ""
def clear():
    global expression 
    expression = ""
    equation.set("")

#-UI Setup-
root = tk.Tk()
root.title("Calculator")
root.geometry("320x420")
root.resizable(True, True)
root.configure(bg="#1e1e2f")  # dark background

expression = ""
equation = tk.StringVar()

# Entry field
entry = tk.Entry(
    root,
    textvariable=equation,
    font=("Arial", 22),
    justify="right",
    bg="#2d2d44",
    fg="white",
    bd=0,
    insertbackground="white"
)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=10)

# Button style
btn_font = ("Arial", 14, "bold")
btn_color = "#3e3e5c"
btn_fg = "white"

def make_button(text, row,col, w=7, h=2, cmd=None, color=btn_color, span=1):
    btn = tk.Button(
        root,
        text=text,
        width=w,
        height=h,
        font=btn_font,
        bg=color,
        fg=btn_fg,
        bd=0,
        command=cmd if cmd else lambda t=text: press(t))
    btn.grid(row=row, column=col, columnspan=span, padx=5, pady=5)
    return btn

#-Buttons-
make_button("7", 1, 0)
make_button("8", 1, 1)
make_button("9", 1, 2)
make_button("+", 1, 3)

make_button("4", 2, 0)
make_button("5", 2 ,1)
make_button("6", 2, 2)
make_button("-", 2, 3)

make_button("1", 3, 0)
make_button("2", 3, 1)
make_button("3", 3, 2)
make_button("*", 3, 3)

make_button("0", 4, 0)
make_button("/", 4, 1)
make_button(".", 4, 2)
make_button("=", 4, 3, cmd=equalpress, color="#5c5cff")

make_button("C", 5, 0, w=32, h=2, cmd=clear, color="#ff4d4d", span=4)

root.mainloop()



