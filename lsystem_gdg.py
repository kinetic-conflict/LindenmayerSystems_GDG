import tkinter as tk # for GUI
import turtle # for Drawing

'''
F: Move turtle forward.
+: Rotate turtle right by the specified Angle.
-: Rotate turtle left by the specified Angle.
'''

def main():
    root = tk.Tk()
    root.title("Lindenmayer System")
    root.geometry("900x600")
    root.mainloop()
    
    
if __name__ == "__main__":
    main()