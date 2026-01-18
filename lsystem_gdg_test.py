import tkinter as tk

root = tk.Tk()
root.title("Frame Demo")

frame = tk.Frame(root, bg="lightblue", width=200, height=100, bd=3, relief=tk.RIDGE)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="This is a Frame", bg="lightblue")
label.pack(pady=20)

root.mainloop()