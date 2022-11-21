import pygame
from pygame import mixer
import os
import array
import time


pygame.init()
mainPath = os.getcwd()
soundPath = mainPath+ "/sound"
fontPath = mainPath + "/font"
exitPagePath = mainPath + "/olavan_asset/exit_page"

totalScorePagePath = mainPath + "/olavan_asset/total_score_page"
clickSound = pygame.mixer.Sound(soundPath+"/click.mp3")


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

font=pygame.font.Font(fontPath+"/trebuc.ttf",32)

def _showText(text,x,y):
    showText=font.render(text,True,(0,0,0))
    screen.blit(showText, (x,y))

def _checkClickRect(left,top,width,height):
    pos = pygame.mouse.get_pos()
    if (pos[0]>=left and pos[0]<=left+width) and (pos[1]>=top and pos[1]<=top+height):
        return 1
    else:
        return 0


def _exit():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    clickSound.play()
                    return 1
                elif event.key == pygame.K_BACKSPACE:
                    clickSound.play()
                    return 0
            if pygame.mouse.get_pressed()[0]:
                if _checkClickRect(431,283,430,180) == 1:
                    clickSound.play()
                    return 0
                elif _checkClickRect(431,463,430,180) == 1:
                    clickSound.play()
                    return 1

        bg = pygame.image.load(exitPagePath+"/Exit_game_page.png") 
        exitButton = pygame.image.load(exitPagePath+"/Exit.png")
        noexitButton = pygame.image.load(exitPagePath+"/No_exit.png")
        screen.blit(bg,(0,0))
        screen.blit(noexitButton,(431,283))
        screen.blit(exitButton,(431,463))
        pygame.display.update()



def total_score_page(score,songName):
    bg = pygame.image.load(totalScorePagePath+"/bg.png") 
    collectButton = pygame.image.load(totalScorePagePath+"/Collect_button.png")
    titleGetpoint = pygame.image.load(totalScorePagePath+"/getPoint.png")
    star = pygame.image.load(totalScorePagePath+"/"+str(score)+".png")

    
    soundT = pygame.mixer.Sound(totalScorePagePath+"/result_score.mp3")
    soundT.play()
    #pygame.mixer.music.play()
    
    startT = pygame.time.get_ticks()/1000
    endT=0
    a=0    
        

    while True:
        if a==0 and endT-startT<4:
            endT=pygame.time.get_ticks()/1000
            print(endT)
        elif a==0:
            print('jdjis')
            pygame.mixer.music.load(totalScorePagePath+"/"+str(score)+".mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.queue(totalScorePagePath+"/Collect_TotalScore.mp3")
            a=1
  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    clickSound.play()
                    exit = _exit()
                    if exit == 1:
                        pygame.quit()
                        exit()
            if pygame.mouse.get_pressed()[0]:
                if _checkClickRect(525,576,230,100) == 1:
                    clickSound.play()
                    main()

    
        screen.blit(bg,(0,0))
        screen.blit(star,(390,434))
        screen.blit(collectButton, (512, 576))
        screen.blit(titleGetpoint, (380, 370))
        _showText(songName,562,260)
        pygame.display.update()

def main():
    pygame.init()
    total_score_page(2,"Too Cute") 
main()
