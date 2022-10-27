import pygame
import time
import array
import os

mainPath = os.getcwd()
print(mainPath)
gamePagePath = mainPath + "/olavan_asset/game_page"
fontPath = mainPath + "/font"
musicPath = mainPath + "/music"
highestScorePath = mainPath + "/highest_score"

pygame.init()
pygame.display.set_caption("main_test")
screen = pygame.display.set_mode((1280, 800))
#game variable               
t1 = [0, 4.4, 9.1, 11.3, 13.7, 16, 18.3, 22.9, 25.1, 28.8, 31.1, 37.9, 38.9, 41.5, 46.1, 47.3, 48.5, 51.1, 52.9, 55.2, 57.6, 59.8, 64.56, 66.8, 70.35, 71.4, 72.6, 73.8, 76, 78.5, 82.9, 84.2, 85.5, 86.6, 90, 94, 111]
t2 = [0, 3.2, 6.5, 9.8, 13.1, 16.32, 17.9, 19.6, 21.2, 24.5, 26.14, 29.4, 31, 32.6, 34.3, 37.65, 39.25, 42.55, 44.2, 47.45, 50.74, 52.3, 54.7, 57.23, 58.9, 60.5, 62.2, 63.7, 67, 68.6, 70.26, 71.98, 73.56, 75.2, 76.7, 80.2, 92]
t3 = [0, 10.77, 12.15, 13.35, 14.86, 16.12, 17.5, 19.9, 22.84, 24.11, 25.28, 26.8, 28.02, 29.266, 30.783, 32.19, 33.498, 34.856, 36.157, 37.525, 40.746, 42.771, 44.132, 45.4, 46.4, 48.172, 49.47, 50.7, 52.03, 53.429, 54.8, 57.45, 58.8, 60.043, 61.37, 64.78, 78]
#image load
gamePageBg=pygame.image.load(gamePagePath+"/game_page.png")
dog = pygame.image.load(gamePagePath+"/dog.png")
cat = pygame.image.load(gamePagePath+"/cat.png")
sushi = pygame.image.load(gamePagePath+"/sushi.png")
food = pygame.image.load(gamePagePath+"/food.png")
cloud = pygame.image.load(gamePagePath+"/cloud.png")
#sound load
hitSound = pygame.mixer.Sound(musicPath+"/hit_sound.mp3")
missSound = pygame.mixer.Sound(musicPath+"/miss_sound.mp3")
dogSound = pygame.mixer.Sound(musicPath+"/dog_sound.mp3")
catSound = pygame.mixer.Sound(musicPath+"/cat_sound.mp3")
#font load
font=pygame.font.Font(fontPath+"/trebuc.ttf",32)
#sound setting
hitSound.set_volume(0.4)
missSound.set_volume(0.4)
#icon setting
pygame.display.set_icon(dog)



def _getHighestScore(songName):
    with open(highestScorePath+"/highest_score_"+songName+".txt","r") as f:
        return f.read()

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

def _callCat(n,t,countPlaySFX,presentTicks):
    count = 0
    if presentTicks >= t and countPlaySFX<n:
        catSound.play()
        count+=1   
    return count


def _callDog(n,t,countPlaySFX,presentTicks):
    count = 0
    if presentTicks >= t and countPlaySFX<n:
        dogSound.play()
        count+=1   
    return count

def _checkCat(countPlaySFX,recentSoundTime,key,presentTicks,a):
    score = 0
    if presentTicks>=recentSoundTime and presentTicks<=recentSoundTime+1 and a[countPlaySFX]==0:
        if key == "f":
            score+=50
            hitSound.play()
            a[countPlaySFX]=1
        elif key == "j":
            missSound.play()
            a[countPlaySFX]=1
    elif presentTicks>recentSoundTime+1 and a[countPlaySFX]==0:
            missSound.play()
            a[countPlaySFX]=1
    elif a[countPlaySFX]==0 and a[countPlaySFX-1]==1 and (key=="f" or key=="j"):
            missSound.play()
    return score

def _checkDog(countPlaySFX,recentSoundTime,key,presentTicks,a):
    score = 0
    if presentTicks>=recentSoundTime and presentTicks<=recentSoundTime+1 and a[countPlaySFX]==0:
        if key == "j":
            score+=50
            hitSound.play()
            a[countPlaySFX]=1
        elif key == "f":
            missSound.play()
            a[countPlaySFX]=1
    elif presentTicks>recentSoundTime+1 and a[countPlaySFX]==0:
            missSound.play()
            a[countPlaySFX]=1
    elif a[countPlaySFX]==0 and a[countPlaySFX-1]==1 and (key=="f" or key=="j"):
            missSound.play()
    return score

def _pauseTime():
    pausePageBg=pygame.image.load(mainPath+"/olavan_asset/pause_page/pause_page.png")
    pauseTime = 0
    back=pygame.image.load(mainPath+"/olavan_asset/pause_page/back_select_song.png")
    continues=pygame.image.load(mainPath+"/olavan_asset/pause_page/continue_button.png")
    restart=pygame.image.load(mainPath+"/olavan_asset/pause_page/restart_button.png")

    pauseStart = pygame.time.get_ticks()
    while True:
        pauseTime = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:            
                    return pauseTime-pauseStart
                elif event.key == pygame.K_r:
                    return -1
                elif event.key == pygame.K_b:
                    return 0
            if pygame.mouse.get_pressed()[0]:
                if _checkClickRect(425,211,430,180) == 1:
                    return pauseTime-pauseStart
                if _checkClickRect(425,391,430,180) == 1:
                    return -1
    
        screen.blit(pausePageBg,(0,0))
        screen.blit(back,(425,571))
        screen.blit(continues,(425,211))
        screen.blit(restart,(425,391))
        pygame.display.update()

def _play(t,songName):
    #array for counting the beat
    array.array("i")                
    a = array.array("i",(0 for i in range(0,36)))
    a[0] = 1
    #any variables
    pygame.mixer.music.load(musicPath+"/"+songName+"_music.mp3")
    pauseTime = 0
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(1,0.0)
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
                        pauseTemp = _pauseTime()
                        if pauseTemp == -1:
                            _play(t,songName)
                        elif pauseTemp == 0:
                            main()
                        pauseTime += pauseTemp
                        pygame.mixer.music.unpause()
                        
                        
        presentTicks=(pygame.time.get_ticks()-startTicks-pauseTime)/1000 
        
        if a[1] == 0:       
            countPlaySFX += _callCat(1,t[1],countPlaySFX,presentTicks)
            scoreValue += _checkCat(1,t[1],key,presentTicks,a)
        elif a[2] == 0:
            countPlaySFX += _callCat(2,t[2],countPlaySFX,presentTicks)
            scoreValue += _checkCat(2,t[2],key,presentTicks,a)
        elif a[3] == 0:
            countPlaySFX += _callCat(3,t[3],countPlaySFX,presentTicks)
            scoreValue += _checkCat(3,t[3],key,presentTicks,a) 
        elif a[4] == 0:
            countPlaySFX += _callDog(4,t[4],countPlaySFX,presentTicks)
            scoreValue += _checkDog(4,t[4],key,presentTicks,a)
        elif a[5] == 0:
            countPlaySFX += _callDog(5,t[5],countPlaySFX,presentTicks)
            scoreValue += _checkDog(5,t[5],key,presentTicks,a)
        elif a[6] == 0:
            countPlaySFX += _callDog(6,t[6],countPlaySFX,presentTicks)
            scoreValue += _checkDog(6,t[6],key,presentTicks,a)
        elif a[7] == 0:
            countPlaySFX += _callCat(7,t[7],countPlaySFX,presentTicks)
            scoreValue += _checkCat(7,t[7],key,presentTicks,a)
        elif a[8] == 0:
            countPlaySFX += _callDog(8,t[8],countPlaySFX,presentTicks)
            scoreValue += _checkDog(8,t[8],key,presentTicks,a)
        elif a[9] == 0:
            countPlaySFX += _callDog(9,t[9],countPlaySFX,presentTicks)
            scoreValue += _checkDog(9,t[9],key,presentTicks,a)
        elif a[10] == 0:
            countPlaySFX += _callDog(10,t[10],countPlaySFX,presentTicks)
            scoreValue += _checkDog(10,t[10],key,presentTicks,a)
        elif a[11] == 0:
            countPlaySFX += _callDog(11,t[11],countPlaySFX,presentTicks)
            scoreValue += _checkDog(11,t[11],key,presentTicks,a)
        elif a[12] == 0:
            countPlaySFX += _callCat(12,t[12],countPlaySFX,presentTicks)
            scoreValue += _checkCat(12,t[12],key,presentTicks,a)
        elif a[13] == 0:
            countPlaySFX += _callDog(13,t[13],countPlaySFX,presentTicks)
            scoreValue += _checkDog(13,t[13],key,presentTicks,a)
        elif a[14] == 0:
            countPlaySFX += _callCat(14,t[14],countPlaySFX,presentTicks)
            scoreValue += _checkCat(14,t[14],key,presentTicks,a)
        elif a[15] == 0:
            countPlaySFX += _callDog(15,t[15],countPlaySFX,presentTicks)
            scoreValue += _checkDog(15,t[15],key,presentTicks,a)
        elif a[16] == 0:
            countPlaySFX += _callDog(16,t[16],countPlaySFX,presentTicks)
            scoreValue += _checkDog(16,t[16],key,presentTicks,a)
        elif a[17] == 0:
            countPlaySFX += _callCat(17,t[17],countPlaySFX,presentTicks)
            scoreValue += _checkCat(17,t[17],key,presentTicks,a)
        elif a[18] == 0:
            countPlaySFX += _callDog(18,t[18],countPlaySFX,presentTicks)
            scoreValue += _checkDog(18,t[18],key,presentTicks,a)
        elif a[19] == 0:
            countPlaySFX += _callDog(19,t[19],countPlaySFX,presentTicks)
            scoreValue += _checkDog(19,t[19],key,presentTicks,a)
        elif a[20] == 0:
            countPlaySFX += _callCat(20,t[20],countPlaySFX,presentTicks)
            scoreValue += _checkCat(20,t[20],key,presentTicks,a)
        elif a[21] == 0:
            countPlaySFX += _callCat(21,t[21],countPlaySFX,presentTicks)
            scoreValue += _checkCat(21,t[21],key,presentTicks,a)
        elif a[22] == 0:
            countPlaySFX += _callDog(22,t[22],countPlaySFX,presentTicks)
            scoreValue += _checkDog(22,t[22],key,presentTicks,a)
        elif a[23] == 0:
            countPlaySFX += _callDog(23,t[23],countPlaySFX,presentTicks)
            scoreValue += _checkDog(23,t[23],key,presentTicks,a)
        elif a[24] == 0:
            countPlaySFX += _callDog(24,t[24],countPlaySFX,presentTicks)
            scoreValue += _checkDog(24,t[24],key,presentTicks,a)
        elif a[25] == 0:
            countPlaySFX += _callCat(25,t[25],countPlaySFX,presentTicks)
            scoreValue += _checkCat(25,t[25],key,presentTicks,a)
        elif a[26] == 0:
            countPlaySFX += _callDog(26,t[26],countPlaySFX,presentTicks)
            scoreValue += _checkDog(26,t[26],key,presentTicks,a)
        elif a[27] == 0:
            countPlaySFX += _callDog(27,t[27],countPlaySFX,presentTicks)
            scoreValue += _checkDog(27,t[27],key,presentTicks,a)
        elif a[28] == 0:
            countPlaySFX += _callCat(28,t[28],countPlaySFX,presentTicks)
            scoreValue += _checkCat(28,t[28],key,presentTicks,a)
        elif a[29] == 0:
            countPlaySFX += _callDog(29,t[29],countPlaySFX,presentTicks)
            scoreValue += _checkDog(29,t[29],key,presentTicks,a)
        elif a[30] == 0:
            countPlaySFX += _callCat(30,t[30],countPlaySFX,presentTicks)
            scoreValue += _checkCat(30,t[30],key,presentTicks,a)
        elif a[31] == 0:
            countPlaySFX += _callDog(31,t[31],countPlaySFX,presentTicks)
            scoreValue += _checkDog(31,t[31],key,presentTicks,a)
        elif a[32] == 0:
            countPlaySFX += _callCat(32,t[32],countPlaySFX,presentTicks)
            scoreValue += _checkCat(32,t[32],key,presentTicks,a)
        elif a[33] == 0:
            countPlaySFX += _callDog(33,t[33],countPlaySFX,presentTicks)
            scoreValue += _checkDog(33,t[33],key,presentTicks,a)
        elif a[34] == 0:
            countPlaySFX += _callCat(34,t[34],countPlaySFX,presentTicks)
            scoreValue += _checkCat(34,t[34],key,presentTicks,a)
        elif a[35] == 0:
            countPlaySFX += _callDog(35,t[35],countPlaySFX,presentTicks)
            scoreValue += _checkDog(35,t[35],key,presentTicks,a)
        
        #preferences
        screen.blit(gamePageBg,(0,0))
        _showCat(catX,400)
        _showDog(dogX,400)
        _showText(songName,562,50)
        _showCloud(cloudX,111)
        if cloudX<=100 and cloudBack==0:
            cloudX+=0.5
            if cloudX==100:
                cloudBack = 1
        if cloudBack==1 and cloudX>=-100:
            cloudX-=0.5
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


def main_page():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:            
                    return 1
                elif event.key == pygame.K_s:
                    return 2
                elif event.key == pygame.K_k:
                    return 3
        screen.blit(gamePageBg,(0,0))
        pygame.display.update()
        
def main():
    menu = main_page()
    if menu == 1:
        songName = "jinglebell"
        endGamePoint = _play(t1,songName)
    elif menu == 2:
        songName = "shutdown"
        endGamePoint = _play(t2,songName)
    elif menu == 3:
        songName = "kerntarn"
        endGamePoint = _play(t3,songName)

main()
