from socket import gaierror
import pygame
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


#game loop 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.blit(bg,(0,0))
    screen.blit(exitButton,(431,283))
    screen.blit(noexitButton,(431,463))
    pygame.display.update()
pygame.quit()