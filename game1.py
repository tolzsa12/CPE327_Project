from tabnanny import check
import pygame
from pygame import mixer
import os

pygame.init()
mainPath = os.getcwd()
homePagePath = mainPath + "/olavan_asset/home_page"
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


list_song = ["Jingle Bell","Shutdown",
                "Too Cute"] #เวลาจะเพิ่มหรือลด มาแก้ตรงนี้พอ
num_song = len(list_song)
BLACK = (0,0,0)

#ทุกสิ่งที่กดได้
Blueblock = pygame.image.load('olavan_asset/select_music_page/Box.png').convert_alpha()
homeButton = pygame.image.load('olavan_asset/select_music_page/Home_button.png').convert_alpha()
playButton = pygame.image.load('olavan_asset/select_music_page/'+'Play_button.png').convert_alpha()

# Blueblock properties
posBlueblock1_x,posBlueblock1_y =  -74,227
posBlueblock2_x,posBlueblock2_y =  402,227
posBlueblock3_x,posBlueblock3_y =  878,227
Blueblock_weight , Blueblock_height = 465,445

# ฟ้อนที่ใช้แสดง
detailfont = pygame.font.SysFont("arialblack",40)


#create game window

BG_SELECTMUSIC = pygame.transform.scale(pygame.image.load(
    'olavan_asset/select_music_page/Select_music_page.png'),(SCREEN_WIDTH,SCREEN_HEIGHT))
def _checkClickRect(left,top,width,height):
    pos = pygame.mouse.get_pos()
    if (pos[0]>=left and pos[0]<=left+width) and (pos[1]>=top and pos[1]<=top+height):
        return 1
    else:
        return 0

#home
def home_Page():
    pygame.display.set_caption("OLAVAN")
    bg = pygame.image.load(homePagePath+"/HomePageBG.png") 
    startButton = pygame.image.load(homePagePath+"/Start_button.png")
    tutorialButton = pygame.image.load(homePagePath+"/Tutorial_button.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    quit()

            if _checkClickRect(210,248,430,180) == 1: #select tutorial
                if pygame.mouse.get_pressed()[0]:
                    return 1

            elif _checkClickRect(640,248,430,180) == 1: #select start
                if pygame.mouse.get_pressed()[0]:
                    return 2

            #if pygame.mouse.get_pressed()[0]:
                #if _checkClickRect(210,248,430,180) == 1: #select tutorial
                    #return 1
                #elif _checkClickRect(640,248,430,180) == 1: #select start
                    #return 2

        screen.blit(bg,(0,0))
        screen.blit(startButton,(640,248))
        screen.blit(tutorialButton,(210,248))
        pygame.display.update()
#mixer.music.load(homePagePath+"/MusicHomePage.mp3")
#mixer.music.play()


#tutorialPage 1
def tutorialPage_1():
    pygame.display.set_caption("OLAVAN")
    tutorialPage1 = pygame.image.load(homePagePath+"/Tutorial1.png")
    homepageButton = pygame.image.load(homePagePath+"/Home_button.png")
    nextButton = pygame.image.load(homePagePath+"/next.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    quit()
           
           
            if _checkClickRect(1028,685,230,100) == 1: #select next
                if pygame.mouse.get_pressed()[0]:
                    return 0
            if _checkClickRect(16,20,230,100) == 1: #select homepage
                if pygame.mouse.get_pressed()[0]:
                    mixer.music.load(homePagePath+"/Click sound effect.mp3")
                    mixer.music.play()
                    main()
    
        screen.blit(tutorialPage1,(0,0))
        screen.blit(homepageButton,(16,20))
        screen.blit(nextButton,(1028,685))
        pygame.display.update()


#tutorialPage 2
def tutorialPage_2():
    pygame.display.set_caption("OLAVAN")
    tutorialPage2 = pygame.image.load(homePagePath+"/Tutorial2.png")
    homepageButton = pygame.image.load(homePagePath+"/Home_button.png")
    prevButton = pygame.image.load(homePagePath+"/Previous_button.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    quit()
            if pygame.mouse.get_pressed()[0]:
                if _checkClickRect(16,686,230,100) == 1: #select back
                    if pygame.mouse.get_pressed()[0]:
                        tutorialPage_1()
                if _checkClickRect(16,20,230,100) == 1: #select homepage
                    if pygame.mouse.get_pressed()[0]:
                        main()
        
        screen.blit(tutorialPage2,(0,0))
        screen.blit(homepageButton,(16,20))
        screen.blit(prevButton,(16,686))
        pygame.display.update()


def draw_window():
    screen.blit(BG_SELECTMUSIC,(0,0))


# เลือกเพลง
def howSelectMusic(state):
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("sound/select_music/Select_Music_Page.mp3")
        pygame.mixer.music.play()
        sampleMusic = list_song[state]
        pygame.mixer.music.queue("music/"+sampleMusic+"_hook.mp3")



def draw_button(x,y,image): #วาดกล่องสี่เหลี่ยม ที่กดแล้วจะเกิด action
    display_blueblock = image.get_rect()
    display_blueblock.topleft = (x,y)
    clicked = False
    action = False
    pos = pygame.mouse.get_pos()
    if display_blueblock.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
            clicked = True
            action = True
    if pygame.mouse.get_pressed()[0] == 0:
        clicked = False
    
    screen.blit(image,(display_blueblock.x,display_blueblock.y))

    return action 


def clickEffect():
    pygame.mixer.music.load("sound/click.mp3")
    pygame.mixer.music.play()


#game loop 

def displayDetail(state):
    
    if state == 0:

        Music1name = list_song[num_song-1]
        Music2name = list_song[state]
        Music3name = list_song[state+1]
  
    elif state > 0 and state < num_song-1:

        Music1name = list_song[state-1]
        Music2name = list_song[state]
        Music3name = list_song[state+1]
   
    elif state == num_song - 1:
       
        Music1name = list_song[state-1]
        Music2name = list_song[state]
        Music3name = list_song[0]

    Music1 = detailfont.render(Music1name,True,BLACK)
    Music2 = detailfont.render(Music2name,True,BLACK)
    Music3 = detailfont.render(Music3name,True,BLACK)
   
   
    screen.blit(Music1 ,(posBlueblock1_x+Blueblock_weight/2 - Music1.get_width()/2
    ,posBlueblock1_y + Blueblock_height/2 - Music1.get_height()/2 + 50))
    screen.blit(Music2 ,(posBlueblock2_x+Blueblock_weight/2 - Music2.get_width()/2
    ,posBlueblock2_y + Blueblock_height/2 - Music2.get_height()/2 + 50))
    screen.blit(Music3 ,(posBlueblock3_x+Blueblock_weight/2 - Music3.get_width()/2
    ,posBlueblock3_y + Blueblock_height/2 - Music3.get_height()/2 + 50))

    displayIcon(Music1name,69,272)
    displayIcon(Music2name,545,272)
    displayIcon(Music3name,1021,272)
    #แสดง icon

def displayIcon(music,x,y):
    icon = pygame.image.load('olavan_asset/select_music_page/'+ music +'_icon.png').convert_alpha()
    screen.blit(icon,(x,y))

def showSampleMusic(state,selectMenu): #เล่นเพลงตัวอย่าง
   
   if not pygame.mixer.music.get_busy() and selectMenu:
    sampleMusic = list_song[state]
    pygame.mixer.music.load("music/"+sampleMusic+"_hook.mp3")
    pygame.mixer.music.play(-1)



def main():
    mixer.music.load(homePagePath+"/MusicHomePage.mp3")
    mixer.music.play()
    check1 = home_Page()
    print(check1)
    if check1 ==  1:
        mixer.music.stop()
        mixer.music.load(homePagePath+"/Click sound effect.mp3")
        mixer.music.play()
        mixer.music.queue(homePagePath+"/Tutorial1.mp3")
        check2 = tutorialPage_1()
        if check2 == 0:
            mixer.music.stop()
            mixer.music.load(homePagePath+"/Click sound effect.mp3")
            mixer.music.play()
            mixer.music.queue(homePagePath+"/Tutorial 2.mp3")
            check3 = tutorialPage_2()
    elif check1 == 2:
        # ตัวบอกสเตตัส programRunning คือ โปรแกรมทั้งหมด selectMenu = หน้าเลือกเพลง
        programRunning,selectMenu = True,True 
        # playingGame หน้าเล่นเกม homePage หน้าแรก
        playingGame,homePage = False,False
        FirsttimehomePage = True
        stateMusic = 1 # เพลงที่เล่น 
        while programRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    programRunning = False 
                #print(Bluesquare_img)


                if selectMenu:
                    draw_window()
                    if FirsttimehomePage:
                        howSelectMusic(stateMusic)
                        FirsttimehomePage = False

                    #Part แสดงกล่องฟ้า ปุ่ม และคลิกกล่องฟ้า
                    if draw_button(-74,227,Blueblock) :
                        if stateMusic == 0:
                            stateMusic = num_song-1
                        else: 
                            stateMusic -= 1
                        pygame.mixer.music.stop()

                    if draw_button(402,227,Blueblock) :
                        pass

                    if draw_button(878,227,Blueblock) :
                        if stateMusic == num_song-1:
                            stateMusic = 0
                        else: 
                            stateMusic += 1
                        pygame.mixer.music.stop()

                    #แสดงปุ่ม เล่นและย้อนกลับ
                    if draw_button(16,20,homeButton):
                        homePage = True
                        selectMenu = False
                        pygame.mixer.music.fadeout(200)
                        clickEffect()
                    
                    if draw_button(525,532,playButton):
                        playingGame = True
                        selectMenu = False
                        pygame.mixer.music.fadeout(200)
                        clickEffect()

                    #Part กดคีย์บอร์ด
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_f:
                            if stateMusic == 0:
                                stateMusic = num_song-1
                            else:
                                stateMusic -= 1
                            pygame.mixer.music.stop() # ทำการหยุดเพลงที่เล่นอยู่

                        if event.key == pygame.K_j:
                            if stateMusic == num_song-1:
                                stateMusic = 0
                            else: 
                                stateMusic += 1
                            pygame.mixer.music.stop() #ทำการหยุดเพลงที่เล่นอยู่

                        if event.key == pygame.K_RETURN:
                            playingGame = True
                            selectMenu = False
                            pygame.mixer.music.fadeout(200)
                            clickEffect()
                        if not event.key == pygame.K_f and not event.key == pygame.K_j and not event.key == pygame.K_RETURN:
                            FirsttimehomePage = True
                            pygame.mixer.music.stop() 
                            howSelectMusic(stateMusic)

                    displayDetail(stateMusic)
                    showSampleMusic(stateMusic,selectMenu)
                #กรณีที่อยู่หน้าเล่นเกม
                elif not selectMenu and playingGame:
                    draw_window()
                    Music = detailfont.render(list_song[stateMusic],True,BLACK)
                    screen.blit(Music ,(posBlueblock2_x+Blueblock_weight/2 - Music.get_width()/2
                    ,posBlueblock2_y + Blueblock_height/2 - Music.get_height()/2 + 50))
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            playingGame = False
                            selectMenu = True
                            pygame.mixer.music.stop()
                #กรณีอยู่หน้า homepage
                
                
                elif not selectMenu and homePage:
                    print("ok")
                    selectMenu = True
                    homePage = False
                    pygame.mixer.music.stop()

            pygame.display.update()
        pygame.quit()
        quit()
            







        
main()
