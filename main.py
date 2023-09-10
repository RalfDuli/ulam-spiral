import tkinter as tk
from ulam_spiral import *
from constants import *

starting_dim = 5
spiral = UlamSpiral(starting_dim)

def draw_spiral(canvas):
    '''
    Draws the spiral in a grid format, with black squares
    representing prime numbers and white squares representing
    nonprime numbers.
    '''
    scaling_factor = SCREEN_X / (spiral.dim * 1.25)
    canvas.delete("all")  # Clear the canvas
    for row in range(spiral.dim):
        for col in range(spiral.dim):
            if spiral.matrix[row][col] == 1:
                color = 'black'
            else:
                color = 'white'
            x1 = col * scaling_factor
            x2 = (col + 1) * scaling_factor
            y1 = MENU_HEIGHT + row * scaling_factor
            y2 = MENU_HEIGHT + (row + 1) * scaling_factor
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

def change_dimension(new_dim):
    spiral.change_dim(new_dim)
    draw_spiral(canvas)

root = tk.Tk()
root.title("Ulam Spiral")
root.geometry(f"{SCREEN_X}x{SCREEN_Y}")

prompt = tk.Label(text="Select the dimensions of the Ulam Spiral")
prompt.pack(side = 'top')

# Creates the button bar

button_bar = tk.Frame(root)
button_bar.pack(side='top')

button_dict = {
    '5x5' : 5,
    '10x10' : 10,
    '12x12' : 12,
    '15x15' : 15,
    '20x20' : 20,
    '50x50' : 50
}

for key, dimensions in button_dict.items():
    button = tk.Button(button_bar, text=key, width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                        command=lambda d=dimensions: change_dimension(d))
    button.pack(side='left')

canvas = tk.Canvas(root, width=SCREEN_X, height=SCREEN_Y - MENU_HEIGHT)
canvas.pack()
draw_spiral(canvas)

root.mainloop()
