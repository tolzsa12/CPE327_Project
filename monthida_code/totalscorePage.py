import pygame
import os

pygame.init()
os.chdir("../")
mainPath = os.getcwd()
homePagePath = mainPath + "/olavan_asset/total_score_page"


#create game window

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("OLAVAN")
bg = pygame.image.load(homePagePath+"/Total_score_page.png") 
collectButton = pygame.image.load(homePagePath+"/Collect_button.png")
titleGetpoint = pygame.image.load(homePagePath+"/getPoint.png")
star5 = pygame.image.load(homePagePath+"/1.png") # 5 point
star4 = pygame.image.load(homePagePath+"/2.png") # 4 point 
star3 = pygame.image.load(homePagePath+"/3.png") # 3 point
star2 = pygame.image.load(homePagePath+"/4.png") # 2 point
star1 = pygame.image.load(homePagePath+"/5.png") # 1 point
star0 = pygame.image.load(homePagePath+"/6.png") # 0 point

#show star

def showStar(point):
    if point == 1:
       screen.blit(star1,(390,434))
    elif point == 2:
       screen.blit(star2,(390,434))
    elif point == 3:
       screen.blit(star3,(390,434))
    elif point == 4:
       screen.blit(star4,(390,434))
    elif point == 5:
       screen.blit(star5,(390,434))
    elif point == 0:
       screen.blit(star0,(390,434))


#game loop 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(bg,(0,0))
    showStar(0)
    screen.blit(collectButton, (512, 576))
    screen.blit(titleGetpoint, (380, 370))
    pygame.display.update()
pygame.quit()
  