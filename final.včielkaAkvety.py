import tkinter as tk
import random

class Bee:
    def __init__(self, canvas, img, x, y):
        self.canvas = canvas
        self.image = img
        self.id = canvas.create_image(x, y, image=img)
        self.x = x
        self.y = y

    def move(self):
        # Náhodný pohyb v rozmedzí -50 až 50 pixelov v oboch osiach
        dx = random.randint(-50, 50)
        dy = random.randint(-50, 50)

        # Zabráňme, aby včielka opustila canvas
        new_x = self.x + dx
        new_y = self.y + dy
        if new_x < 0:
            new_x = 0
        elif new_x > 800:
            new_x = 800
        if new_y < 0:
            new_y = 0
        elif new_y > 600:
            new_y = 600

        self.canvas.move(self.id, new_x - self.x, new_y - self.y)
        self.x = new_x
        self.y = new_y

class Flower:
    def __init__(self, canvas, img, x, y):
        self.canvas = canvas
        self.image = img
        self.id = canvas.create_image(x, y, image=img)

# Create the main window
root = tk.Tk()
root.title("Bee Flying Simulation")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Load images
bee_img = tk.PhotoImage(file="mikrovcela.png")
flower_img = tk.PhotoImage(file="buducikvet.png")

# Create bee and flowers
bee = Bee(canvas, bee_img, 400, 300)
flowers = [Flower(canvas, flower_img, random.randint(50, 750), random.randint(50, 550)) for _ in range(3)]

# Function to make the bee fly randomly
def fly_randomly():
    bee.move()
    root.after(100, fly_randomly)  # Opakuj každých 100 milisekúnd

# Start the bee flying
fly_randomly()

root.mainloop()
