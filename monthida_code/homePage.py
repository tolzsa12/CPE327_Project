import pygame
import os

pygame.init()
os.chdir("../")
mainPath = os.getcwd()
homePagePath = mainPath + "/olavan_asset/home_page"

#create game window

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("OLAVAN")
bg = pygame.image.load(homePagePath+"/HomePageBG.png") 
startButton = pygame.image.load(homePagePath+"/Start_button.png")
tutorialButton = pygame.image.load(homePagePath+"/Tutorial_button.png")


#game loop 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.blit(bg,(0,0))
    screen.blit(startButton,(210,248))
    screen.blit(tutorialButton,(640,248))
    pygame.display.update()
pygame.quit()