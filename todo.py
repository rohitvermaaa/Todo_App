import tkinter as tk
from PIL import Image, ImageTk

def add_task():
    task = entry.get("1.0", tk.END)
    if task.strip():
        listbox.insert(tk.END, task)
        entry.delete("1.0", tk.END)

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        index = selected_task[0]
        listbox.delete(index)

root = tk.Tk()
root.title("To-Do List")

bg_color = "#CAD2C5"
fg_color = "#354F52"
button_bg_color = "#84A98C"
button_fg_color = "#2F3E46"

root.configure(bg=bg_color)

icon_image = Image.open("icon.png")
icon = ImageTk.PhotoImage(icon_image)
root.tk.call("wm", "iconphoto", root._w, icon)

root.geometry("450x450")

listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=15, width=40, font=("Arial", 12), bg=bg_color, fg=fg_color, selectbackground="white", selectforeground="black")
listbox.pack(pady=10)

entry = tk.Text(root, height=2, width=40, font=("Arial", 12), bg=bg_color, fg=fg_color)
entry.pack(pady=10)

button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack()

add_button = tk.Button(button_frame, text="Add Task", font=("Arial", 12), command=add_task, bg=button_bg_color, fg=button_fg_color, height=2, width=15, borderwidth=5, relief="ridge")
add_button.pack(side=tk.LEFT, padx=10)

remove_button = tk.Button(button_frame, text="Remove Selected Task", font=("Arial", 12), command=remove_task, bg=button_bg_color, fg=button_fg_color, height=2, width=20, borderwidth=5, relief="ridge")
remove_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
