import os
import pygame
from pygame import mixer

pygame.init()
os.chdir("../")
mainPath = os.getcwd()
homePagePath = mainPath + "/olavan_asset/sample_sound_page"


# add sound

mixer.music.load(homePagePath+"/Sample Sound.mp3")
mixer.music.play()
mixer.music.queue(homePagePath+"/countdown.mp3")


#create game window

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("OLAVAN")
bg = pygame.image.load(homePagePath+"/Sample_sound_page.png") 


#game loop 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.blit(bg,(0,0))
    pygame.display.update()
pygame.quit()