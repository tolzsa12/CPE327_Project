from tabnanny import check
import pygame
from pygame import mixer
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
def homePage():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    quit()
            if pygame.mouse.get_pressed()[0]:
                if _checkClickRect(210,248,430,180) == 1: #select tutorial
                    return 2
                elif _checkClickRect(640,248,430,180) == 1: #select start
                    return 1
                
        screen.blit(bg,(0,0))
        screen.blit(startButton,(210,248))
        screen.blit(tutorialButton,(640,248))
        pygame.display.update()


#tutorialPage 1
def tutorialPage_1():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    quit()
           
            
            if pygame.mouse.get_pressed()[0]:
                if _checkClickRect(1028,685,230,100) == 1: #select next
                    return 0
                if _checkClickRect(16,20,230,100) == 1: #select homepage
                    main()
    
        screen.blit(tutorialPage1,(0,0))
        screen.blit(homepageButton,(16,20))
        screen.blit(nextButton,(1028,685))
        pygame.display.update()


#tutorialPage 2
def tutorialPage_2():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    quit()
            if pygame.mouse.get_pressed()[0]:
                if _checkClickRect(16,686,230,100) == 1: #select back
                    tutorialPage_1()
                if _checkClickRect(16,20,230,100) == 1: #select homepage
                    main()
        
        screen.blit(tutorialPage2,(0,0))
        screen.blit(homepageButton,(16,20))
        screen.blit(prevButton,(16,686))
        pygame.display.update()


#game loop 

def main():
    check1 = homePage()
    print(check1)
    if check1 ==  1:
        #mixer.music.load(homePagePath+"/Click sound effect.mp3")
        #mixer.music.play()
        #mixer.music.queue(homePagePath+"/Tutorial1.mp3")
        check2 = tutorialPage_1()
        if check2 == 0:
            mixer.music.load(homePagePath+"/Click sound effect.mp3")
            mixer.music.play()
            mixer.music.queue(homePagePath+"/Tutorial 2.mp3")
            check3 = tutorialPage_2()

main()
