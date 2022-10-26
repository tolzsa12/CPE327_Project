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

back=pygame.image.load(mainPath+"/olavan_asset/pause_page/back_select_song.png")
continues=pygame.image.load(mainPath+"/olavan_asset/pause_page/continue_button.png")
restart=pygame.image.load(mainPath+"/olavan_asset/pause_page/restart_button.png")


font=pygame.font.Font(mainPath+"/font/trebuc.ttf",32)
pauseTime = 0

def testText(x):
    text=font.render(str(x),True,(0,0,0))
    screen.blit(text, (400,300))


def checkClickRect(left,top,width,height):
    pos = pygame.mouse.get_pos()
    if (pos[0]>=left and pos[0]<=left+width) and (pos[1]>=top and pos[1]<=top+height):
        return 1
    else:
        return 0



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
            if pygame.mouse.get_pressed()[0]:
                if checkClickRect(425,211,430,180) == 1:
                    return pauseTime-pauseStart
                if checkClickRect(425,391,430,180) == 1:
                    return -1
        
        screen.blit(bgp,(0,0))
        screen.blit(back,(425,571))
        screen.blit(continues,(425,211))
        screen.blit(restart,(425,391))
        pygame.display.update()


