import pygame

from ulam_spiral import *

spiral = UlamSpiral(10)
pygame.init()

scaling_factor = 50

screen = pygame.display.set_mode([spiral.dim * scaling_factor,
                                spiral.dim * scaling_factor])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for row in (range(spiral.dim)):
        for col in (range(spiral.dim)):
            if spiral.matrix[row][col] == 1: color = (0,0,0)
            else: color = (255,255,255)
            pygame.draw.rect(screen, color, (col * scaling_factor,
                                             row * scaling_factor,
                                             scaling_factor, scaling_factor))

    pygame.display.flip()