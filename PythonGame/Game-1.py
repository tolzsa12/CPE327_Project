
import pygame
import os

pygame.init()
pygame.font.init()

WIDTH,HEIGHT = 1280,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Olvan")

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Olvan_Assets','Home_Page','HomePageBG.png')),
(WIDTH,HEIGHT))

def draw_window():
    WIN.blit(BACKGROUND,(0,0)) #set bg picture as background

    pygame.display.update() #update the current screen

def main():
    open = True
    while open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                open = False
    
            draw_window()
    pygame.quit()
    quit()



if __name__ == "__main__":
    main()