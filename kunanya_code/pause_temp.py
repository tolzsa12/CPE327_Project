import pygame
import time
import array
import os

main_path=os.getcwd()

pygame.init()
pygame.display.set_caption("gameV.0.1")
screen = pygame.display.set_mode((1280, 800))
bgp=pygame.image.load(main_path+"/olavan_asset/pause_page/pause_page.png")
pauseTime = 0



font=pygame.font.Font(main_path+"/font/trebuc.ttf",32)
pauseTime = 0

def testText(x):
        text=font.render(str(x),True,(0,0,0))
        screen.blit(text, (400,300))



def _pauseTime():
    pauseStart = pygame.time.get_ticks()
    while True:
        pauseTime = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:            
                    return pauseTime-pauseStart

        
        screen.blit(bgp,(0,0))
        testText(pauseTime/1000)
        pygame.display.update()


