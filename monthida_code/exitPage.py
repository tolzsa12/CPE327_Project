#from socket import gaierror
import pygame
import time
from pygame import mixer
import os

pygame.init()
os.chdir("../")
mainPath = os.getcwd()
homePagePath = mainPath + "/olavan_asset/exit_page"


#create game window

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("OLAVAN")
bg = pygame.image.load(homePagePath+"/Exit_game_page.png") 
exitButton = pygame.image.load(homePagePath+"/Exit.png")
noexitButton = pygame.image.load(homePagePath+"/No_exit.png")

#add sound

mixer.music.load(homePagePath+"/Exit Game.mp3")
mixer.music.play()


def _checkClickRect(left,top,width,height):
    pos = pygame.mouse.get_pos()
    if (pos[0]>=left and pos[0]<=left+width) and (pos[1]>=top and pos[1]<=top+height):
        return 1
    else:
        return 0


def exitFunction():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if pygame.mouse.get_pressed()[0]:
                    if _checkClickRect(431,463,430,180) == 1:
                        quit()


#game loop 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.blit(bg,(0,0))
    screen.blit(exitButton,(431,463))
    screen.blit(noexitButton,(431,283))
    if pygame.mouse.get_pressed()[0] :
        if _checkClickRect(431,463,430,180) == 1:
            mixer.music.load(homePagePath+"/Click sound effect.mp3")
            mixer.music.play()
            time.sleep(1)
            exit()

    pygame.display.update()
pygame.quit()