import tkinter as tk # for GUI
import turtle # for drawing

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
    
    global axiom, rules, iteration, t, angle
    
    root = tk.Tk()
    root.title("L-System Fractal Architect")
    root.geometry("900x600")

    canvas = tk.Canvas(root, width=600, height=600, bg="white")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    t_screen = turtle.TurtleScreen(canvas)
    t = turtle.RawTurtle(t_screen)
    t.speed(0)  #maxspeed
    t_screen.setworldcoordinates(-300, -300, 300, 300)

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

    tk.Button(frame, text="Generate", command=generate).pack(pady=20)

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

    t.clear()
    t.penup()
    t.goto(0, 0)
    t.pendown()

    turtle.tracer(0, 0)

    stack = []  #branch stack
    
    total_len = final_string.count("F")
    step = 0
    


    for ch in final_string:
        if ch == "F":
            ratio = step / total_len
            t.pencolor(ratio, 0.4, 1 - ratio) #for gradeint
            t.forward(5)
            step += 1
        elif ch == "+":
            t.right(int(angle.get()))
        elif ch == "-":
            t.left(int(angle.get()))

        elif ch == "[":
            stack.append((t.position(), t.heading()))
        elif ch == "]":
            pos, head = stack.pop()
            t.penup()
            t.goto(pos)
            t.setheading(head)
            t.pendown()

    turtle.update()

if __name__ == "__main__":
    main()
