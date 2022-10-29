from math import gamma
import pygame
import os

pygame.init()
os.chdir("../")
mainPath = os.getcwd()
homePagePath = mainPath + "/olavan_asset/tutorial_page"


#create game window

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("OLAVAN")
tutorialPage1 = pygame.image.load(homePagePath+"/Tutorial1.png")
tutorialPage2 = pygame.image.load(homePagePath+"/Tutorial2.png")
homepageButton = pygame.image.load(homePagePath+"/Home_button.png")
nextButton = pygame.image.load(homePagePath+"/next.png")
prevButton = pygame.image.load(homePagePath+"/Previous_button.png")


#chlick
def _checkClickRect(left,top,width,height):
    pos = pygame.mouse.get_pos()
    if (pos[0]>=left and pos[0]<=left+width) and (pos[1]>=top and pos[1]<=top+height):
        return 1
    else:
        return 0


#page 1
def page1(prev):
    if prev == 1:
        screen.blit(tutorialPage1,(0,0))
        screen.blit(homepageButton,(16,20))
        screen.blit(nextButton,(1028,685))


#tutorial page 2
def nextPage(next):
    if next == 1:
        screen.blit(tutorialPage2,(0,0))
        screen.blit(homepageButton,(16,20))

#loop
def showTutorial(show):
    if show == 1:
        page1(1)
    else:
        pygame.mouse.get_pressed()[0]
        if _checkClickRect(1028,685,230,100) == 1: #click ต่อไป
            nextPage(1)

#game loop 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    showTutorial(1)
    
    pygame.display.update()
pygame.quit()