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

        #clic action sur une carte
        # si le clic souris est detecter
        if event.type == pygame.MOUSEBUTTONDOWN:
             #iter les keys du dico image_liste qui sont des tuple surface (250, 0) soite les coordonee x, y top left des images
            for i in classdescartes.image_liste:
               
                image_rect = classdescartes.image.get_rect(topleft=i)
                #detecte la colision entre le clic souris et la surface de l image
                if image_rect.collidepoint(event.pos):
                    #print("clic", classdescartes.image_liste[i][3])
                    
                    ###affiche l image random du dictionnaire image liste
                    string =  classdescartes.image_liste[i][3]
                    image = pygame.image.load(os.path.join(string))
                    #print("load",image)
                    image1 = image.convert(screen) 
                    carte_instance = screen.blit(image1, (image_rect))
                   # print("clic", classdescartes.image_liste[i])
                    #si moin de deux cartes retourner alors ajouté a la liste
                    
                    if len(classdescartes.carte_retournee)<= 2 :
                        if classdescartes.image_liste[i][1] == False:
                            classdescartes.carte_retournee.append(classdescartes.image_liste[i])
                            print(classdescartes.carte_retournee)
                        
                    #si il y a deux carte dans la liste carte retourner
                    if len(classdescartes.carte_retournee)== 2 :
                        #si la string du non de fichier est la meme 
                        if classdescartes.carte_retournee[0][3] == classdescartes.carte_retournee[1][3]:
                            print("les meme")
                            #passer la variable a true
                            classdescartes.image_liste[classdescartes.carte_retournee[0][0]][1] = True
                            classdescartes.image_liste[classdescartes.carte_retournee[1][0]][1] = True
                            print(classdescartes.image_liste[classdescartes.carte_retournee[0][0]])
                            print(classdescartes.image_liste[classdescartes.carte_retournee[1][0]])

                        else:
                            for i in range(2):
                                print("different",classdescartes.carte_retournee)
                                string_dos = pygame.image.load(os.path.join(classdescartes.carte_retournee[0][2]))
                                
                                image_rect_dos = string_dos.get_rect(topleft=classdescartes.carte_retournee[i][0])

                                string_dos1 = string_dos.convert(screen)
                                screen.blit(string_dos1, (image_rect_dos))
                        
                    
                        classdescartes.carte_retournee.clear()
                        print("liste d elements carte_retournee videe",classdescartes.carte_retournee )
    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")
    
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
