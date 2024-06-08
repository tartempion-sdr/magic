import pygame
import classdescartes
import os
 
# pygame setup
pygame.init()

image_dos_chemin = "assets/dos-noir1.bmp"
decale_x = 0
decale_y = 0
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("magic")
clock = pygame.time.Clock()
running = True

screen.fill("purple")

ziva = classdescartes.Cartes(screen, image_dos_chemin, decale_x, decale_y)
ziva.rejouer(screen, image_dos_chemin, decale_x, decale_y)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #action sur une carte
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in classdescartes.image_liste:
                image_rect = classdescartes.image.get_rect(topleft=i)
                if image_rect.collidepoint(event.pos):
                    print("clic", classdescartes.image_liste[i][3])
                    string =  classdescartes.image_liste[i][3]
                    print(string[0])
                    image = pygame.image.load(os.path.join(string[0]))
                    image1 = image.convert(screen) 
                    carte_instance = screen.blit(image1, (image_rect))
                    print("clic", classdescartes.image_liste[i])

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")
    
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
