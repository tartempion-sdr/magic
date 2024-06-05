import pygame
import os

image_chemin = "assets/dos-noir1.bmp"
decale_x = 0
decale_y = 0

class Cartes:
    def __init__(self, p_screen, p_image, p_decale_x, p_decale_y):
        
        
        self.a_screen = p_screen
        self.a_image = p_image
        self.a_decale_x = p_decale_x
        self.p_decale_y = p_decale_y
        
        #p_screen = pygame.display.set_mode((1280, 720))
        p_screen = pygame.Surface
        p_image = image_chemin
        p_decale_x = decale_x
        p_decale_y = decale_y       

        
        
   
    def rejouer(self, p_screen, p_image, p_decale_x, p_decale_y):
        
        image = pygame.image.load(os.path.join(p_image)).convert(p_screen)   
        
            
        for i in range(6):
           
            for e in range(10):
                
                p_screen.blit(image, (p_decale_x, p_decale_y))
                p_decale_x += 50
            p_decale_y += 73
            p_decale_x = 0
            
    
    
    def gagner():
        pass    
    
    
    def perdu():
        pass