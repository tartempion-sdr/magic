import pygame
import classdescartes
import os
 
# pygame setup
pygame.init()

image_chemin = "assets/dos-noir1.bmp"
decale_x = 0
decale_y = 0
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("magic")
clock = pygame.time.Clock()
running = True

screen.fill("purple")

ziva = classdescartes.Cartes(screen, image_chemin, decale_x, decale_y)
ziva.rejouer(screen, image_chemin, decale_x, decale_y)
print(classdescartes.image_liste)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #action sur une carte
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(60):
                image_rect = classdescartes.image.get_rect(topleft=classdescartes.image_liste[i])
                if image_rect.collidepoint(event.pos):
                    print("clic", classdescartes.image_liste[i])

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")
    
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
