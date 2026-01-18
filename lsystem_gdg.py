import tkinter as tk # for GUI
import turtle # for Drawing

'''
F: Move turtle forward.
+: Rotate turtle right by the specified Angle.
-: Rotate turtle left by the specified Angle.
'''

'''
def main():
    root = tk.Tk()
    root.title("Lindenmayer System")
    root.geometry("900x600")
    root.mainloop()
'''   
    # buttons
def foo():
    print("Lindenmayer")
    
root = tk.Tk()
root.title("Lindenmayer System")
root.geometry("900x600")
CA = tk.Button(root, text="Shree", command = foo )
CA.pack()
root.mainloop()
    
    
foo()