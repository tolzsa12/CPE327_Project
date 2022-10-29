
from tkinter import font
import pygame
import os
import button
pygame.init()

#create game window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
WIN = pygame.display.set_mode((SCREEN_WIDTH,
      SCREEN_HEIGHT))
pygame.display.set_caption("Olvan")

#game variables


BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Olvan_Assets','Select music'
,'Select_music_page.png')),
(SCREEN_WIDTH,SCREEN_HEIGHT))


#define fonts
font = pygame.font.SysFont("arialblack",40)

#define colours
TEXT_COL = (255,255,255)
WIN.blit(BACKGROUND,(0,0))

#load button image select game
select_bg_img = pygame.image.load('Olvan_Assets/Select music/Box.png').convert_alpha()

#button class which we can move to seperate fi le


#create button instances
select_music_button1 = button.Button(-30,200,select_bg_img)
select_music_button2 = button.Button(420,200,select_bg_img)
select_music_button3 = button.Button(870,200,select_bg_img)


def draw_window():
    WIN.blit(BACKGROUND,(0,0))
   # pygame.display.update()

def draw_text(text,font,text_col,x,y):
    WIN.blit(BACKGROUND,(0,0))
    img = font.render(text,True,text_col)
    WIN.blit(img,(x,y))
    pygame.display.update()

#def draw_text(text,font,text_col,x,y):

def main():
    open = True
    game_paused = False
    while open:
        draw_window()

        if select_music_button1.draw(WIN):
            print("Song A")
        if select_music_button2.draw(WIN):
            print("Song B")
        if select_music_button3.draw(WIN):
            print("Song C")
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                open = False
        pygame.display.update()
            

    pygame.quit()
    quit()



if __name__ == "__main__":
    main()