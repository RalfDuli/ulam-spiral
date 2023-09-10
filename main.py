import tkinter as tk
from ulam_spiral import *
from constants import *

starting_dim = 5
spiral = UlamSpiral(starting_dim)

def draw_spiral(canvas):
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

button_bar = tk.Frame(root)
button_bar.pack(side='top')

five_dim_button = tk.Button(button_bar, text='5x5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                            command=lambda: change_dimension(5))
five_dim_button.pack(side='left')

ten_dim_button = tk.Button(button_bar, text='10x10', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                           command=lambda: change_dimension(10))
ten_dim_button.pack(side='left')

twelve_dim_button = tk.Button(button_bar, text='12x12', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                              command=lambda: change_dimension(12))
twelve_dim_button.pack(side='left')

fifteen_dim_button = tk.Button(button_bar, text='15x15', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                               command=lambda: change_dimension(15))
fifteen_dim_button.pack(side='left')

twenty_dim_button = tk.Button(button_bar, text='20x20', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                             command=lambda: change_dimension(20))
twenty_dim_button.pack(side='left')

fifty_dim_button = tk.Button(button_bar, text='50x50', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                             command=lambda: change_dimension(50))
fifty_dim_button.pack(side='left')

canvas = tk.Canvas(root, width=SCREEN_X, height=SCREEN_Y - MENU_HEIGHT)
canvas.pack()
draw_spiral(canvas)

root.mainloop()
