import tkinter as tk

def handle_mouse_move(event):
    print("Myš sa pohybuje na pozícii ({event.x}, {event.y})")

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=700)
canvas.pack()


canvas.bind("<Button-1>", handle_mouse_move)
root.mainloop()
