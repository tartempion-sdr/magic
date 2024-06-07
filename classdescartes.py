import pygame
import random
import os


image_liste = {}
screen = pygame.Surface
image_chemin = "assets/dos-noir1.bmp"
        
image = pygame.image.load(os.path.join(image_chemin))

decale_x = 0
decale_y = 0

class Cartes:
    def __init__(self, p_screen, p_image, p_decale_x, p_decale_y):
        
        
        self.a_screen = p_screen
        self.a_image = p_image
        self.a_decale_x = p_decale_x
        self.a_decale_y = p_decale_y
        
        #p_screen = pygame.display.set_mode((1280, 720))
        p_screen = screen
        p_image = image_chemin
        p_decale_x = decale_x
        p_decale_y = decale_y       

        
        
   
    def rejouer(self, p_screen, p_image, p_decale_x, p_decale_y):
          
        image1 = image.convert(p_screen) 
            
        for i in range(2):
           
            for e in range(10):
                
              
                carte_instance = p_screen.blit(image1, (p_decale_x, p_decale_y))
                carte_n0_xy = (p_decale_x, p_decale_y)
                #creeune liste de tuple coordonee xy
                image_liste[carte_n0_xy] = [carte_n0_xy, False]
                
                p_decale_x += 50
            p_decale_y += 73
            p_decale_x = 0
        print(image_liste)
    
    
    def gagner(self):
        pass    
    
    
    def perdu(self):
        pass