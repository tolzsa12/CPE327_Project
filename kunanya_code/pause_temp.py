import pygame
import time
import array
import os
#import game_page_shutdown

mainPath=os.getcwd()

pygame.init()
pygame.display.set_caption("gameV.0.1")
screen = pygame.display.set_mode((1280, 800))
bgp=pygame.image.load(mainPath+"/olavan_asset/pause_page/pause_page.png")
pauseTime = 0



font=pygame.font.Font(mainPath+"/font/trebuc.ttf",32)
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
                elif event.key == pygame.K_r:
                    return -1

        
        screen.blit(bgp,(0,0))
        testText(pauseTime/1000)
        pygame.display.update()


