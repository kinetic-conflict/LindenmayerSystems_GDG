import tkinter as tk # for GUI
import turtle # for Drawing

'''
My notes:- 
F: Move turtle forward.
+: Rotate turtle right by the specified Angle.
-: Rotate turtle left by the specified Angle.

Axiom - base string of LS
Rules - chnages the string
Angle - determines shape
Iteration - how many times to apply rule?
'''

def main():
    root = tk.Tk()
    root.title("Lindenmayer System")
    root.geometry("900x600")
    
import tkinter as tk

def main():
    
    global axiom, rules, iteration
    
    root = tk.Tk()
    root.title("L-System Fractal Architect")
    root.geometry("900x600")

    canvas = tk.Canvas(root, width=600, height=600, bg="white")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    frame = tk.Frame(root, width=300, bg="#e9e9e9")
    frame.pack(side=tk.RIGHT, fill=tk.Y)

    tk.Label(frame, text="Axiom:").pack(pady=(20, 5))
    axiom = tk.Entry(frame)
    axiom.pack(pady=5)

    tk.Label(frame, text="Rules:").pack(pady=(20, 5))
    rules = tk.Entry(frame)
    rules.pack(pady=5)

    tk.Label(frame, text="Angle (degree):").pack(pady=(20, 5))
    angle = tk.Entry(frame)
    angle.pack(pady=5)

    tk.Label(frame, text="Iterations:").pack(pady=(20, 5))
    iteration = tk.Entry(frame)
    iteration.pack(pady=5)

    tk.Button(frame, text="Generate").pack(pady=20)

    root.mainloop()

'''
if symbol in rules:
    replace 
'''
def rule_converter(text):
    rules = {}
    parts = text.split(",")

    for part in parts:
        if ":" in part:
            key, value = part.split(":")
            rules[key.strip()] = value.strip()

    return rules

'''
set current = axiom
repeat for each iteration:
    for each symbol in current: 
    if symbol in rules replace it 
    else keep it and then update current
return current
'''
def lsystem(axiom, rules, iteration):
    current = axiom

    for _ in range(iteration):
        result = ""
        for c in current:
            if c in rules:
                result += rules[c]
            else:
                result += c
        current = result

    return current

'''
take a, r, i as input
convrt rules into dict and call lsystem
print final string
'''
def generate():
    start = axiom.get()
    rule_text = rules.get()
    count = int(iteration.get())

    rule_dict = rule_converter(rule_text)
    final_string = lsystem(start, rule_dict, count)

    print(final_string)  # for debugging purpise

if __name__ == "__main__":
    main()