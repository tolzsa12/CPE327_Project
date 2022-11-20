#why2
from tabnanny import check
import pygame
from pygame import mixer
import os
import array


pygame.init()
mainPath = os.getcwd()

homePagePath = mainPath + "/olavan_asset/home_page"
confirmPagePath = mainPath + "/olavan_asset/selected_music_page"
highestScorePath = mainPath + "/highest_score"
fontPath = mainPath + "/font"
sampleSoundPagePath = mainPath + "/olavan_asset/sample_sound_page"
musicPath = mainPath + "/music"
gamePagePath = mainPath + "/olavan_asset/game_page"
exitPagePath = mainPath + "/olavan_asset/exit_page"
tempPagePath = mainPath + "/olavan_asset/temp"
totalScorePagePath = mainPath + "/olavan_asset/total_score_page"

soundPath = mainPath+ "/sound"

#image load
gamePageBg=pygame.image.load(gamePagePath+"/game_page.png")
dog = pygame.image.load(gamePagePath+"/dog.png")
cat = pygame.image.load(gamePagePath+"/cat.png")
sushi = pygame.image.load(gamePagePath+"/sushi.png")
food = pygame.image.load(gamePagePath+"/food.png")
cloud = pygame.image.load(gamePagePath+"/cloud.png")
oops = pygame.image.load(gamePagePath+"/oops.png")
#sound load
hitSound = pygame.mixer.Sound(musicPath+"/hit_sound.mp3")
missSound = pygame.mixer.Sound(musicPath+"/miss_sound.mp3")
dogSound = pygame.mixer.Sound(musicPath+"/dog_sound.mp3")
catSound = pygame.mixer.Sound(musicPath+"/cat_sound.mp3")
clickSound = pygame.mixer.Sound(soundPath+"/click.mp3")
#sound setting
hitSound.set_volume(0.4)
missSound.set_volume(0.4)
#icon setting
pygame.display.set_icon(dog)



#music
t0 = [0, 4.4, 9.1, 11.3, 13.7, 16, 18.3, 22.9, 25.1, 28.8, 31.1, 37.9, 38.9, 41.5, 46.1, 47.3, 48.5, 51.1, 52.9, 55.2, 57.6, 59.8, 64.56, 66.8, 70.35, 71.4, 72.6, 73.8, 76, 78.5, 82.9, 84.2, 85.5, 86.6, 90, 94, 108]
t1 = [0, 3.2, 6.5, 9.8, 13.1, 16.32, 17.9, 19.6, 21.2, 24.5, 26.14, 29.4, 31, 32.6, 34.3, 37.65, 39.25, 42.55, 44.2, 47.45, 50.74, 52.3, 54.7, 57.23, 58.9, 60.5, 62.2, 63.7, 67, 68.6, 70.26, 71.98, 73.56, 75.2, 76.7, 80.2, 89]
t2 = [0, 10.77, 12.15, 13.35, 14.86, 16.12, 17.5, 19.9, 22.84, 24.11, 25.28, 26.8, 28.02, 29.266, 30.783, 32.19, 33.498, 34.856, 36.157, 37.525, 40.746, 42.771, 44.132, 45.4, 46.4, 48.172, 49.47, 50.7, 52.03, 53.429, 54.8, 57.45, 58.8, 60.043, 61.37, 64.78, 75]
c = 'c'
d = 'd'
b0 = ["n", c, d, c, d, d, c, d, c, d, d, c, c, d, d, d, d, c, c, c, d, c, d, c, d, d, d, c, c, d, c, c, d, d, c, c]
b1 = ["n", d, c, d, c, d, d, c, c, d, c, d, c, d, c, d, d, c, c, c, d, c, d, c, d, d, d, c, c, d, c, c, d, d, c, c]
b2 = ["n", c, c, c, d, d, d, c, d, d, d, d, c, d, c, d, d, c, d, d, c, c, d, d, d, c, d, d, c, d, c, d, c, d, c, d]

tempt=[t0,t1,t2]
tempb=[b0,b1,b2]

#font load
font=pygame.font.Font(fontPath+"/trebuc.ttf",32)


print(homePagePath)
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
                    pygame.quit()
                    exit()

            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_f: #select tutorial
                    print('oo')
                    pygame.mixer.pause()
                    return 1

                if event.key == pygame.K_j: #select start
                    pygame.mixer.pause()
                    return 2

            if _checkClickRect(210,248,430,180) == 1: #select tutorial
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.pause()
                    return 1

            elif _checkClickRect(640,248,430,180) == 1: #select start
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.pause()
                    return 2

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    clickSound.play()
                    pygame.mixer.pause()
                    exit = _exit()
                    if exit == 1:
                        pygame.quit()
                        exit()
                    pygame.mixer.music.unpause()

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
    
    mixer.music.load(homePagePath+"/Click sound effect.mp3")
    mixer.music.play()
    mixer.music.queue(homePagePath+"/Tutorial1.mp3")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    clickSound.play()
                    mixer.music.pause()
                    exit = _exit()
                    if exit == 1:
                        pygame.quit()
                        exit()
                    mixer.music.unpause()
           
           
            if _checkClickRect(1028,685,230,100) == 1: #select next
                if pygame.mouse.get_pressed()[0]:
                    mixer.music.stop()
                    tutorialPage_2()
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
    mixer.music.load(homePagePath+"/Click sound effect.mp3")
    mixer.music.play()
    mixer.music.queue(homePagePath+"/Tutorial 2.mp3")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    quit()
            if pygame.mouse.get_pressed()[0]:
                if _checkClickRect(16,686,230,100) == 1: #select back
                        mixer.music.stop()
                        tutorialPage_1()
                if _checkClickRect(16,20,230,100) == 1: #select homepage
                        main()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    clickSound.play()
                    mixer.music.pause()
                    exit = _exit()
                    if exit == 1:
                        pygame.quit()
                        exit()
                    mixer.music.unpause()
        
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

def calculatePoint(endGameScore):
    if endGameScore == 0:
        return 0
    elif endGameScore <= 350:
        return 1
    elif endGameScore <= 700:
        return 2
    elif endGameScore <= 1050:
        return 3
    elif endGameScore <= 1400:
        return 4
    else:
        return 5

    
def _getHighestScore(songName):
    with open(highestScorePath+"/highest_score_"+songName+".txt","r") as f:
        return f.read()


    
def _showText(text,x,y):
    showText=font.render(text,True,(0,0,0))
    screen.blit(showText, (x,y))


    
def confirmMusicPage(stateMusic):
    print("This"+str(stateMusic))
    bg = pygame.image.load(confirmPagePath+"/Confirm_music_page.png") 
    prevButton = pygame.image.load(confirmPagePath+"/Previous_button.png")
    titleMusic = pygame.image.load(confirmPagePath+"/title_music.png")
    titleTotalScore = pygame.image.load(confirmPagePath+"/title_totalscore.png")
    startButton = pygame.image.load(confirmPagePath+"/Start_game_button.png")

    
    
    musicName = list_song[stateMusic]

    try:
        highestScore = int(_getHighestScore(musicName))
    except:
        highestScore = 0
        
    highestStar = calculatePoint(highestScore)
    print(highestStar)

    
    pygame.mixer.music.load(confirmPagePath+"/"+musicName+".mp3")
    pygame.mixer.music.queue(confirmPagePath+"/"+str(highestStar)+"Star.mp3")
    pygame.mixer.music.play()

    a=0
    
    
    
        
    

    #music & score variable
    musicIcon = pygame.image.load(confirmPagePath+"/icon_"+musicName+".png")
    

      
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:
                if _checkClickRect(410,569,230,100) == 1: #select back
                        selectMusicPage()
                        pygame.mixer.music.stop()
                        clickSound.play()
                        return -1
                        
                if _checkClickRect(640,569,230,100) == 1: #select play
                        pygame.mixer.music.stop()
                        clickSound.play()
                        sampleSoundPage()
                        return stateMusic
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.pause()
                    clickSound.play()
                    exit = _exit()
                    if exit == 1:
                        pygame.quit()
                        exit()
                    pygame.mixer.music.unpause()
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    clickSound.play()
                    sampleSoundPage()
                    return stateMusic
                if event.key == pygame.K_BACKSPACE:
                    pygame.mixer.music.stop()
                    clickSound.play()
                    return -1
            

        if not pygame.mixer.music.get_busy() and a==0:
            print("gg")
            pygame.mixer.music.load(confirmPagePath+"/ConfirmSelectMusic.mp3")
            pygame.mixer.music.play()
            a=1

            
    
        screen.blit(bg,(0,0))
        screen.blit(musicIcon, (545, 225))
        screen.blit(prevButton, (410, 569))
        screen.blit(startButton, (640, 569))
        screen.blit(titleMusic, (415, 437))
        _showText(musicName,511,425)
        screen.blit(titleTotalScore, (415, 493))

        if highestStar !=0:
            star = pygame.image.load(confirmPagePath+"/"+str(highestStar)+".png")
            screen.blit(star,(602,477))

        
        pygame.display.update()


def selectMusicPage():
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    clickSound.play()
                    pygame.mixer.music.pause()
                    exit = _exit()
                    if exit == 1:
                        pygame.quit()
                        exit()
                    pygame.mixer.music.unpause()


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
                    main()
                
                if draw_button(525,532,playButton):
                    playingGame = True
                    selectMenu = False
                    pygame.mixer.music.fadeout(200)
                    clickEffect()

                #Part กดคีย์บอร์ด
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        clickSound.play()
                        exit = _exit()
                        if exit == 1:
                            pygame.quit()
                            exit()
                    if event.key == pygame.K_f:
                        pygame.K_BACKSPACE
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
                print("eiei")
                break
            #กรณีอยู่หน้า homepage
            
            
            elif not selectMenu and homePage:
                print("ok")
                selectMenu = True
                homePage = False
                pygame.mixer.music.stop()

        pygame.display.update()
        if playingGame:
            return stateMusic
        

def sampleSoundPage():
    bg = pygame.image.load(sampleSoundPagePath+"/Sample_sound_page.png")
    mixer.music.load(sampleSoundPagePath+"/Sample Sound.mp3")
    mixer.music.play()
    mixer.music.queue(sampleSoundPagePath+"/countdown.mp3")
    a=0
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        screen.blit(bg,(0,0))
        pygame.display.update()
        if a==0:
            pygame.time.wait(16000)
            a=1
            break
        


def _showText(text,x,y):
    showText=font.render(text,True,(0,0,0))
    screen.blit(showText, (x,y))

def _showCat(x,y):
    screen.blit(cat,(x,y))

def _showDog(x,y):
    screen.blit(dog,(x,y))

def _showCloud(x,y):
    screen.blit(cloud,(x,y))

#def testText(x):
        #text=font.render(str(x),True,(0,0,0))
        #screen.blit(text, (400,300))

def _call(n,b,t,countPlaySFX,presentTicks):
    count = 0
    if presentTicks >= t and countPlaySFX<n and b == 'c':
        catSound.play()
        count+=1
    elif presentTicks >= t and countPlaySFX<n and b == 'd':
        dogSound.play()
        count+=1   
    return count

def _check(countPlaySFX,b,recentSoundTime,key,presentTicks,a):
    score = 0
    if b == "c":
        if presentTicks>=recentSoundTime and presentTicks<=recentSoundTime+1 and a[countPlaySFX]==0:
            if key == "f":
                score+=50
                hitSound.play()
                a[countPlaySFX]=1
            elif key == "j":
                missSound.play()
                screen.blit(oops,(532,400))
                pygame.display.update()
                a[countPlaySFX]=1
        elif presentTicks>recentSoundTime+1 and a[countPlaySFX]==0:
                missSound.play()
                screen.blit(oops,(532,400))
                pygame.display.update()
                a[countPlaySFX]=1
        elif a[countPlaySFX]==0 and a[countPlaySFX-1]==1 and (key=="f" or key=="j"):
                missSound.play()
                screen.blit(oops,(532,400))
                pygame.display.update()
        return score
    elif b == "d":
        if presentTicks>=recentSoundTime and presentTicks<=recentSoundTime+1 and a[countPlaySFX]==0:
            if key == "j":
                score+=50
                hitSound.play()
                a[countPlaySFX]=1
            elif key == "f":
                missSound.play()
                screen.blit(oops,(532,400))
                pygame.display.update()
                a[countPlaySFX]=1
        elif presentTicks>recentSoundTime+1 and a[countPlaySFX]==0:
                missSound.play()
                screen.blit(oops,(532,400))
                pygame.display.update()
                a[countPlaySFX]=1
        elif a[countPlaySFX]==0 and a[countPlaySFX-1]==1 and (key=="f" or key=="j"):
                missSound.play()
                screen.blit(oops,(532,400))
                pygame.display.update()
        return score

def _pauseTime():
    pausePagePath = mainPath+"/olavan_asset/pause_page"
    pauseSoundPath = soundPath+"/pause_game_page"
    pausePageBg = pygame.image.load(pausePagePath+"/pause_page.png")
    pauseTime = 0
    back = pygame.image.load(pausePagePath+"/back_select_song.png")
    continues = pygame.image.load(pausePagePath+"/continue_button.png")
    restart = pygame.image.load(pausePagePath+"/restart_button.png")
    catFoot = pygame.image.load(pausePagePath+"/cat_foot.png")

    heightCat = 250
    stateButton = 0

    pauseStart = pygame.time.get_ticks()
    temp=0
    temp2=0
    while True:
        pauseTime = pygame.time.get_ticks()
        screen.blit(pausePageBg,(0,0))
        screen.blit(back,(425,571))
        screen.blit(continues,(425,211))
        screen.blit(restart,(425,391))
        
        if stateButton == 0 and temp-temp2!=1:
            if not pygame.mixer.music.get_busy():
                heightCat = 250
                pygame.mixer.music.load(pauseSoundPath+"/pausegame.mp3")
                pygame.mixer.music.play()
                pygame.mixer.music.queue(pauseSoundPath+"/continue.mp3")
                temp = temp+1
        elif stateButton == 1 and  temp-temp2!=1:
            if not pygame.mixer.music.get_busy():
                heightCat = 250
          
                pygame.mixer.music.load(pauseSoundPath+"/continue.mp3")
                pygame.mixer.music.play()
          
                temp = temp+1
        elif stateButton == 2 and  temp-temp2!=1:
            if not pygame.mixer.music.get_busy():
                heightCat = 430
       
                pygame.mixer.music.load(pauseSoundPath+"/restart.mp3")
                pygame.mixer.music.play()
           
                temp = temp+1
        elif stateButton == 3 and  temp-temp2!=1:
            if not pygame.mixer.music.get_busy():
                heightCat = 610
   
                pygame.mixer.music.load(pauseSoundPath+"/select_new_music.mp3")
                pygame.mixer.music.play()
                temp = temp+1


        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    quit()
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f: #back select
                    pygame.mixer.music.stop()
                    clickSound.play()
                    temp2=temp2+1
                    if stateButton == 0 or stateButton == 1:
                        stateButton = 3
                    else: 
                        stateButton = stateButton - 1
                elif event.key == pygame.K_j: #to restart
                    pygame.mixer.music.stop()
                    clickSound.play()
                    temp2=temp2+1
                    if stateButton == 3:
                        stateButton = 1
                    elif stateButton == 0:
                        stateButton = 2
                    else: 
                        stateButton = stateButton + 1
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    clickSound.play()
                    if stateButton == 0 or stateButton == 1:
                        pygame.mixer.music.stop()
                        pauseTime = pygame.time.get_ticks()
                        return pauseTime-pauseStart
                    elif stateButton == 2:
                        pygame.mixer.music.stop()
                        return -1
                    elif stateButton == 3:
                        pygame.mixer.music.stop()
                        main()
                        

                if event.key == pygame.K_ESCAPE: #exit game
                    clickSound.play()
                    exit = _exit()
                    if exit == 1:
                        quit()

            #check for only changing status        
            if _checkClickRect(425,211,430,180) == 1 and heightCat != 250: #if cursor above the continue button
               
                pygame.mixer.music.stop()
                heightCat = 250
            
                stateButton = 1
                temp2=temp2+1
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.stop()
                    clickSound.play()
                    pauseTime = pygame.time.get_ticks()
                    return pauseTime-pauseStart
            elif _checkClickRect(425,391,430,180) == 1 and heightCat != 430:  #if cursor above the restart button
               
                pygame.mixer.music.stop()
                heightCat = 430
                stateButton = 2
                temp2=temp2+1
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.stop()
                    clickSound.play()
                    return -1
            elif _checkClickRect(425,571,430,180) == 1 and heightCat != 610:   #if cursor above the select new song button
                pygame.mixer.music.stop()
                heightCat = 610
                print(heightCat)
                stateButton = 3
                temp2=temp2+1
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.stop()
                    clickSound.play()
                    return 0

            #check for clicking status
            if _checkClickRect(425,211,430,180) == 1:
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.stop()
                    clickSound.play()
                    pauseTime = pygame.time.get_ticks()
                    return pauseTime-pauseStart
            elif _checkClickRect(425,391,430,180) == 1:
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.stop()
                    clickSound.play()
                    return -1
            elif _checkClickRect(425,571,430,180) == 1:
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.stop()
                    clickSound.play()
                    return 0
                
        screen.blit(catFoot,(783,heightCat))
        pygame.display.update()
            
        


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

def _exitTime():
    exitStart = pygame.time.get_ticks()
    exitTime = 0
    while True:
        exitTime = pygame.time.get_ticks()
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
                    return exitTime-exitStart
            if pygame.mouse.get_pressed()[0]:
                if _checkClickRect(431,283,430,180) == 1:
                    clickSound.play()
                    return exitTime-exitStart
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

def _play(t,b,songName):
    #array for counting the beat
    array.array("i")                
    a = array.array("i",(0 for i in range(0,36)))
    a[0] = 1
    #any variables
    pygame.mixer.music.load(musicPath+"/"+songName+"_music.mp3")
    pauseTime = 0
    exitTime = 0
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound(musicPath+"/"+songName+"_music.mp3"))
    startTicks=pygame.time.get_ticks()
    countPlaySFX = 0
    scoreValue = 0
    cloudX = 0
    cloudBack = 0

    try:
        highestScore = int(_getHighestScore(songName))
    except:
        highestScore = 0
    
    while True:
        key = "initial"
        ysushi = 495
        yfood = 495
        catX = 497
        dogX = 666
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:            
                        catX = 255
                        key = "f"
                        ysushi = 488
                    elif event.key == pygame.K_j: 
                        dogX = 915
                        key = "j"
                        yfood = 488
                    elif event.key == pygame.K_SPACE:
                        
                        pygame.mixer.music.pause()
                        
                        #pygame.mixer.Channel(0).pause()
                        pauseTemp = _pauseTime()
                        if pauseTemp == -1:
                            _play(t,b,songName)
                        elif pauseTemp == 0:
                            main()
                        pauseTime += pauseTemp
                        getPos=(pygame.time.get_ticks()-startTicks-pauseTime-exitTime)/1000
                        pygame.mixer.music.load(musicPath+"/"+songName+"_music.mp3")
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_pos(getPos)
                        
                        
                        #pygame.mixer.Channel(0).unpause()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.pause()
                        clickSound.play()
                        exitTemp = _exitTime()
                        if exitTemp == 1:
                            quit()
                        exitTime += exitTemp
                        pygame.mixer.music.unpause()
                        #pygame.mixer.Channel(0).pause()
                                    
        presentTicks=(pygame.time.get_ticks()-startTicks-pauseTime-exitTime)/1000 
        
        if a[1] == 0:       
            countPlaySFX += _call(1,b[1],t[1],countPlaySFX,presentTicks)
            scoreValue += _check(1,b[1],t[1],key,presentTicks,a)
        elif a[2] == 0:
            countPlaySFX += _call(2,b[2],t[2],countPlaySFX,presentTicks)
            scoreValue += _check(2,b[2],t[2],key,presentTicks,a)
        elif a[3] == 0:
            countPlaySFX += _call(3,b[3],t[3],countPlaySFX,presentTicks)
            scoreValue += _check(3,b[3],t[3],key,presentTicks,a) 
        elif a[4] == 0:
            countPlaySFX += _call(4,b[4],t[4],countPlaySFX,presentTicks)
            scoreValue += _check(4,b[4],t[4],key,presentTicks,a)
        elif a[5] == 0:
            countPlaySFX += _call(5,b[5],t[5],countPlaySFX,presentTicks)
            scoreValue += _check(5,b[5],t[5],key,presentTicks,a)
        elif a[6] == 0:
            countPlaySFX += _call(6,b[6],t[6],countPlaySFX,presentTicks)
            scoreValue += _check(6,b[6],t[6],key,presentTicks,a)
        elif a[7] == 0:
            countPlaySFX += _call(7,b[7],t[7],countPlaySFX,presentTicks)
            scoreValue += _check(7,b[7],t[7],key,presentTicks,a)
        elif a[8] == 0:
            countPlaySFX += _call(8,b[8],t[8],countPlaySFX,presentTicks)
            scoreValue += _check(8,b[8],t[8],key,presentTicks,a)
        elif a[9] == 0:
            countPlaySFX += _call(9,b[9],t[9],countPlaySFX,presentTicks)
            scoreValue += _check(9,b[9],t[9],key,presentTicks,a)
        elif a[10] == 0:
            countPlaySFX += _call(10,b[10],t[10],countPlaySFX,presentTicks)
            scoreValue += _check(10,b[10],t[10],key,presentTicks,a)
        elif a[11] == 0:
            countPlaySFX += _call(11,b[11],t[11],countPlaySFX,presentTicks)
            scoreValue += _check(11,b[11],t[11],key,presentTicks,a)
        elif a[12] == 0:
            countPlaySFX += _call(12,b[12],t[12],countPlaySFX,presentTicks)
            scoreValue += _check(12,b[12],t[12],key,presentTicks,a)
        elif a[13] == 0:
            countPlaySFX += _call(13,b[13],t[13],countPlaySFX,presentTicks)
            scoreValue += _check(13,b[13],t[13],key,presentTicks,a)
        elif a[14] == 0:
            countPlaySFX += _call(14,b[14],t[14],countPlaySFX,presentTicks)
            scoreValue += _check(14,b[14],t[14],key,presentTicks,a)
        elif a[15] == 0:
            countPlaySFX += _call(15,b[15],t[15],countPlaySFX,presentTicks)
            scoreValue += _check(15,b[15],t[15],key,presentTicks,a)
        elif a[16] == 0:
            countPlaySFX += _call(16,b[16],t[16],countPlaySFX,presentTicks)
            scoreValue += _check(16,b[16],t[16],key,presentTicks,a)
        elif a[17] == 0:
            countPlaySFX += _call(17,b[17],t[17],countPlaySFX,presentTicks)
            scoreValue += _check(17,b[17],t[17],key,presentTicks,a)
        elif a[18] == 0:
            countPlaySFX += _call(18,b[18],t[18],countPlaySFX,presentTicks)
            scoreValue += _check(18,b[18],t[18],key,presentTicks,a)
        elif a[19] == 0:
            countPlaySFX += _call(19,b[19],t[19],countPlaySFX,presentTicks)
            scoreValue += _check(19,b[19],t[19],key,presentTicks,a)
        elif a[20] == 0:
            countPlaySFX += _call(20,b[20],t[20],countPlaySFX,presentTicks)
            scoreValue += _check(20,b[20],t[20],key,presentTicks,a)
        elif a[21] == 0:
            countPlaySFX += _call(21,b[21],t[21],countPlaySFX,presentTicks)
            scoreValue += _check(21,b[21],t[21],key,presentTicks,a)
        elif a[22] == 0:
            countPlaySFX += _call(22,b[22],t[22],countPlaySFX,presentTicks)
            scoreValue += _check(22,b[22],t[22],key,presentTicks,a)
        elif a[23] == 0:
            countPlaySFX += _call(23,b[23],t[23],countPlaySFX,presentTicks)
            scoreValue += _check(23,b[23],t[23],key,presentTicks,a)
        elif a[24] == 0:
            countPlaySFX += _call(24,b[24],t[24],countPlaySFX,presentTicks)
            scoreValue += _check(24,b[24],t[24],key,presentTicks,a)
        elif a[25] == 0:
            countPlaySFX += _call(25,b[25],t[25],countPlaySFX,presentTicks)
            scoreValue += _check(25,b[25],t[25],key,presentTicks,a)
        elif a[26] == 0:
            countPlaySFX += _call(26,b[26],t[26],countPlaySFX,presentTicks)
            scoreValue += _check(26,b[26],t[26],key,presentTicks,a)
        elif a[27] == 0:
            countPlaySFX += _call(27,b[27],t[27],countPlaySFX,presentTicks)
            scoreValue += _check(27,b[27],t[27],key,presentTicks,a)
        elif a[28] == 0:
            countPlaySFX += _call(28,b[28],t[28],countPlaySFX,presentTicks)
            scoreValue += _check(28,b[28],t[28],key,presentTicks,a)
        elif a[29] == 0:
            countPlaySFX += _call(29,b[29],t[29],countPlaySFX,presentTicks)
            scoreValue += _check(29,b[29],t[29],key,presentTicks,a)
        elif a[30] == 0:
            countPlaySFX += _call(30,b[30],t[30],countPlaySFX,presentTicks)
            scoreValue += _check(30,b[30],t[30],key,presentTicks,a)
        elif a[31] == 0:
            countPlaySFX += _call(31,b[31],t[31],countPlaySFX,presentTicks)
            scoreValue += _check(31,b[31],t[31],key,presentTicks,a)
        elif a[32] == 0:
            countPlaySFX += _call(32,b[32],t[32],countPlaySFX,presentTicks)
            scoreValue += _check(32,b[32],t[32],key,presentTicks,a)
        elif a[33] == 0:
            countPlaySFX += _call(33,b[33],t[33],countPlaySFX,presentTicks)
            scoreValue += _check(33,b[33],t[33],key,presentTicks,a)
        elif a[34] == 0:
            countPlaySFX += _call(34,b[34],t[34],countPlaySFX,presentTicks)
            scoreValue += _check(34,b[34],t[34],key,presentTicks,a)
        elif a[35] == 0:
            countPlaySFX += _call(35,b[35],t[35],countPlaySFX,presentTicks)
            scoreValue += _check(35,b[35],t[35],key,presentTicks,a)
        
        #preferences
        screen.blit(gamePageBg,(0,0))
        _showCat(catX,400)
        _showDog(dogX,400)
        _showText(songName,562,50)
        _showCloud(cloudX,111)
        if cloudX<=100 and cloudBack==0:
            cloudX+=2
            if cloudX==100:
                cloudBack = 1
        if cloudBack==1 and cloudX>=-100:
            cloudX-=2
            if cloudX==-100:
                cloudBack = 0
            
        _showText("Score: "+str(scoreValue),554,730)
        
        pygame.time.delay(10)
        catX = 497
        dogX = 666
        
        screen.blit(sushi,(138,ysushi))
        screen.blit(food,(1047,yfood))
        pygame.display.update()

        if presentTicks >= t[36]:
            if scoreValue > highestScore:
                highestScore = scoreValue
            with open(highestScorePath+"/highest_score_"+songName+".txt","w") as f:
                f.write(str(highestScore))
            return scoreValue

def total_score_page(score,songName):
    bg = pygame.image.load(totalScorePagePath+"/bg.png") 
    collectButton = pygame.image.load(totalScorePagePath+"/Collect_button.png")
    titleGetpoint = pygame.image.load(totalScorePagePath+"/getPoint.png")
    star = pygame.image.load(totalScorePagePath+"/"+str(score)+".png")

    while True:
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
        pygame.mixer.music.load(totalScorePagePath+"/Result score sound.mp3")  
        pygame.mixer.music.queue(totalScorePagePath+"/"+str(score)+".mp3")
        pygame.mixer.music.play()
        pygame.display.update()

        

def main():
    #check1 = home_Page()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(homePagePath+"/MusicHomePage.mp3"), maxtime=500000)
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(homePagePath+"/Start_HomePage.mp3"), maxtime=9000)
    check1 = home_Page()
    print(check1)
    if check1 ==  1:
        mixer.music.stop()
        check2 = tutorialPage_1()
        #if check2 == 0:
            #check3 = tutorialPage_2()
    elif check1 == 2:
        mixer.music.stop()
        selectSongVar = selectMusicPage()
        stateMusicConfirm = confirmMusicPage(selectSongVar)
        while stateMusicConfirm == -1:
            selectSongVar = selectMusicPage()
            stateMusicConfirm = confirmMusicPage(selectSongVar)
        t=tempt[stateMusicConfirm]
        b=tempb[stateMusicConfirm]
        endGamePoint = _play(t,b,list_song[stateMusicConfirm])
        total_score_page(calculatePoint(endGamePoint),list_song[stateMusicConfirm])
        
main()
