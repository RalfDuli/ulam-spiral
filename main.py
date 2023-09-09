import numpy as np
import tkinter as tk

from ulam_spiral import *
from constants import *

spiral_dim = 12
spiral = UlamSpiral(spiral_dim)

scaling_factor = 50

def draw_spiral():
    canvas = tk.Canvas(root, width=SCREEN_X, height=MENU_HEIGHT+SCREEN_Y)
    canvas.pack()
    for row in (range(spiral.dim)):
        for col in (range(spiral.dim)):
            if spiral.matrix[row][col] == 1: color = 'black'
            else: color = 'white'
            x1 = col * scaling_factor
            x2 = (col+1) * scaling_factor
            y1 = MENU_HEIGHT + row * scaling_factor
            y2 = MENU_HEIGHT + (row+1) * scaling_factor
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)
            #pygame.draw.rect(screen, color, (col * scaling_factor,
            #                                 row * scaling_factor,
             #                                scaling_factor, scaling_factor))

root = tk.Tk()
root.title("Ulam Spiral")
root.geometry(f"{SCREEN_X}x{SCREEN_Y}")

draw_spiral()


root.mainloop()

""" pygame.init()

scaling_factor = 50

screen = pygame.display.set_mode([spiral.dim * scaling_factor,
                                spiral.dim * scaling_factor])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    draw_spiral()

    pygame.display.flip() """