import pygame
import random
import os

carte_retournee = []
image_liste = {}
screen = pygame.Surface
image_dos_chemin = "assets/dos-noir1.bmp"
image_chemin = ["assets/rat.bmp", 
                "assets/poisson.bmp", 
                "assets/pieuvre.bmp", 
                "assets/pie.bmp",
                "assets/lion.bmp", 
                "assets/fourmis.bmp", 
                "assets/chien.bmp", 
                "assets/chat.bmp",
                "assets/canard.bmp", 
                "assets/aigle.bmp",
                "assets/rat.bmp", 
                "assets/poisson.bmp", 
                "assets/pieuvre.bmp", 
                "assets/pie.bmp",
                "assets/lion.bmp", 
                "assets/fourmis.bmp", 
                "assets/chien.bmp", 
                "assets/chat.bmp",
                "assets/canard.bmp", 
                "assets/aigle.bmp"]

       
image = pygame.image.load(os.path.join(image_dos_chemin))

         

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
        p_image = image_dos_chemin
        p_decale_x = decale_x
        p_decale_y = decale_y       

          
        
   #cree l etat initial
    def rejouer(self, p_screen, p_image, p_decale_x, p_decale_y):
          
        image1 = image.convert(p_screen) 
        for i in range(2):
           
            for e in range(10):
                
                random_image = random.choices(image_chemin)
              
                carte_instance = p_screen.blit(image, (p_decale_x, p_decale_y))
                carte_n0_xy = (p_decale_x, p_decale_y)
                #creeune liste de tuple coordonee xy
                image_liste[carte_n0_xy] = [carte_n0_xy, False, image_dos_chemin, random_image[0]]
                #print(random_image)
                #
                #
                print(random_image)
                image_chemin.remove(random_image[0])
                p_decale_x += 50
            p_decale_y += 73
            p_decale_x = 0
        print(len(image_liste))
    
    
    def gagner(self):
        pass    
    
    
    def perdu(self):
        pass