import tkinter as tk

class CanvasWithImage(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        tk.Canvas.__init__(self, master, **kwargs)
        self.image = None
        self.bind('<KeyPress>', self.on_key_press)
        self.focus_set()
        self.move_step = 10

    def load_image(self, image_path):
        self.image = tk.PhotoImage(file=image_path)
        self.create_image(0, 0, anchor=tk.NW, image=self.image)

    def move_image(self, direction):
        if self.image:
            if direction == 'up':
                self.move(self.image, 0, -self.move_step)
            elif direction == 'down':
                self.move(self.image, 0, self.move_step)
            elif direction == 'left':
                self.move(self.image, -self.move_step, 0)
            elif direction == 'right':
                self.move(self.image, self.move_step, 0)

    def on_key_press(self, event):
        key = event.keysym
        if key in ['Up', 'Down', 'Left', 'Right']:
            self.move_image(key.lower())

def main():
    root = tk.Tk()
    root.title("Move Image with Arrow Keys")
    canvas = CanvasWithImage(root, width=400, height=400)
    canvas.pack()

    # Load an image
    canvas.load_image("example_image.png")

    root.mainloop()

if __name__ == "__main__":
    main()
