from tabnanny import check
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
tutorialPage1 = pygame.image.load(homePagePath+"/Tutorial1.png")
tutorialPage2 = pygame.image.load(homePagePath+"/Tutorial2.png")
homepageButton = pygame.image.load(homePagePath+"/Home_button.png")
nextButton = pygame.image.load(homePagePath+"/next.png")
prevButton = pygame.image.load(homePagePath+"/Previous_button.png")

def _checkClickRect(left,top,width,height):
    pos = pygame.mouse.get_pos()
    if (pos[0]>=left and pos[0]<=left+width) and (pos[1]>=top and pos[1]<=top+height):
        return 1
    else:
        return 0

#home
def homePage(check):
 if check == 0:
    screen.blit(bg,(0,0))
    screen.blit(startButton,(210,248))
    screen.blit(tutorialButton,(640,248))
 elif pygame.mouse.get_pressed()[0]:
    if _checkClickRect(210,248,430,180) == 1: #select tutorial
        return check == 1
 elif pygame.mouse.get_pressed()[0]:
    if _checkClickRect(640,248,430,180) == 1: #select start
        return check == 2

#tutorial
def tutorialPage(check):
 if check == 1: #tutorialPage 1
    screen.blit(tutorialPage1,(0,0))
    screen.blit(homepageButton,(16,20))
    screen.blit(nextButton,(1028,685))

#game loop 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    homePage(0)
    tutorialPage(1)
    pygame.display.update()
pygame.quit()