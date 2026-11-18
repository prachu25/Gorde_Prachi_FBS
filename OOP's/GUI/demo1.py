import tkinter as tk

root = tk.Tk()
root.title("Mera first GUI Project")
root.geometry("400x500")

l1=tk.Label(root,text="This is My First GUI", font=("Goudy Stout",18), bg="teal", fg="black")
print()
l2=tk.Label(root,text="This is My First GUI", font=("Goudy Stout",18), bg="royalblue", fg="black")
print()
l3=tk.Label(root,text="This is My First GUI", font=("Goudy Stout",18), bg="lightpink", fg="black")

l1.pack(side="left")
l2.pack(side="right")
l3.pack(side="top")

e = tk.Entry(root)
e.pack()

def show():
    print(e.get())
    
btn = tk.Button(root, text="Submit", command=show)
btn.pack()


root.mainloop()