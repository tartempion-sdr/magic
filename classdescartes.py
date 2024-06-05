import pygame
import os

image_chemin = "assets/dos-noir1.bmp"

class Cartes:
    def __init__(self, p_screen, p_image):
        
        

        
        self.a_screen = p_screen
        self.a_image = p_image
       
        
        #p_screen = pygame.display.set_mode((1280, 720))
        p_screen = pygame.Surface
        p_image = image_chemin
        
               
        
   
    def rejouer(self, p_screen, p_image):
        
        image8 = os.path.join(image_chemin)
        image = pygame.image.load(image8)
        
        image1 = image.convert(p_screen)   
        p_screen.blit(image1, (0, 50))
            
        #for i in range(10):
            
        #    for i in range(6):
         #       print(i)
    
    def gagner():
        pass    
    
    
    def perdu():
        pass