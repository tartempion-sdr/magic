import pygame
import classdescartes
import os
 
# pygame setup
pygame.init()

image_chemin = "assets/dos-noir1.bmp"
decale_x = 0
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("magic")
clock = pygame.time.Clock()
running = True
ziva = classdescartes.Cartes(screen, image_chemin, decale_x)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    ziva.rejouer(screen, image_chemin, decale_x)
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
