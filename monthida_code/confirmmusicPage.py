import pygame
import os

pygame.init()
os.chdir("../")
mainPath = os.getcwd()
homePagePath = mainPath + "/olavan_asset/selected_music_page"


#create game window

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("OLAVAN")
bg = pygame.image.load(homePagePath+"/Confirm_music_page.png") 
prevBotton = pygame.image.load(homePagePath+"/Previous_button.png")
startBotton = pygame.image.load(homePagePath+"/Start_game_button.png")
titleMusic = pygame.image.load(homePagePath+"/title_music.png")
titleTotalScore = pygame.image.load(homePagePath+"/title_totalscore.png")
musicIcon = pygame.image.load(homePagePath+"/icon_jinglebell.png")
star5 = pygame.image.load(homePagePath+"/1.png") # 5 point
star4 = pygame.image.load(homePagePath+"/2.png") # 4 point 
star3 = pygame.image.load(homePagePath+"/3.png") # 3 point
star2 = pygame.image.load(homePagePath+"/4.png") # 2 point
star1 = pygame.image.load(homePagePath+"/5.png") # 1 point


#show highscore

def showStar(point):
    if point == 1:
       screen.blit(star1,(602,477))
    elif point == 2:
       screen.blit(star2,(602,475))
    elif point == 3:
       screen.blit(star3,(602,475))
    elif point == 4:
       screen.blit(star4,(602,475))
    elif point == 5:
       screen.blit(star5,(602,475))


#game loop 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.blit(bg,(0,0))
    showStar(3)
    screen.blit(musicIcon, (545, 225))
    screen.blit(prevBotton, (410, 569))
    screen.blit(startBotton, (640, 569))
    screen.blit(titleMusic, (415, 437))
    screen.blit(titleTotalScore, (415, 493))
    pygame.display.update()
pygame.quit()
  
