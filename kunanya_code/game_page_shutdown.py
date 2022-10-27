import pygame
import time
import array
import os


os.chdir("../")
mainPath = os.getcwd()
#parentPath = os.path.dirname(os.getcwd())
#os.chdir(parentPath)
#parentPath = os.getcwd()

gamePagePath = mainPath + "/olavan_asset/game_page"
fontPath = mainPath + "/font"
musicPath = mainPath + "/music"
highestScorePath = mainPath + "/highest_score"

pygame.init()
pygame.display.set_caption("gameV.0.1")

screen = pygame.display.set_mode((1280, 800))
bg=pygame.image.load(gamePagePath+"/game_page.png")
dog = pygame.image.load(gamePagePath+"/dog.png")
cat = pygame.image.load(gamePagePath+"/cat.png")
sushi = pygame.image.load(gamePagePath+"/sushi.png")
food = pygame.image.load(gamePagePath+"/food.png")
cloud = pygame.image.load(gamePagePath+"/cloud.png")

hitSound = pygame.mixer.Sound(musicPath+"/hit_sound.mp3")
missSound = pygame.mixer.Sound(musicPath+"/miss_sound.mp3")
dogSound = pygame.mixer.Sound(musicPath+"/dog_sound.mp3")
catSound = pygame.mixer.Sound(musicPath+"/cat_sound.mp3")

hitSound.set_volume(0.4)
missSound.set_volume(0.4)
font=pygame.font.Font(fontPath+"/trebuc.ttf",32)
pygame.display.set_icon(dog)


def _getHighestScore():
    with open(highestScorePath+"/highest_score_shutdown.txt","r") as f:
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



def _play2():
    #array for counting the beat
    array.array("i")                
    a = array.array("i",(0 for i in range(0,36)))
    a[0] = 1
    #any variables
    pygame.mixer.music.load(musicPath+"/shutdown_music.mp3")
    pauseTime = 0
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(1,0.0)
    startTicks=pygame.time.get_ticks()
    countPlaySFX = 0
    scoreValue = 0
    cloudX = 0
    cloudBack = 0

    try:
        highestScore = int(_getHighestScore())
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
                        from pause_temp import _pauseTime
                        pauseTemp = _pauseTime()
                        if pauseTemp == -1:
                            _play2()
                        pauseTime += pauseTemp
                        pygame.mixer.music.unpause()
                        
                        
        presentTicks=(pygame.time.get_ticks()-startTicks-pauseTime)/1000 
        
        if a[1] == 0:       
            countPlaySFX += _callDog(1,3.2,countPlaySFX,presentTicks)
            scoreValue += _checkDog(1,3.2,key,presentTicks,a)
        elif a[2] == 0:
            countPlaySFX += _callCat(2,6.5,countPlaySFX,presentTicks)
            scoreValue += _checkCat(2,6.5,key,presentTicks,a)
        elif a[3] == 0:
            countPlaySFX += _callDog(3,9.8,countPlaySFX,presentTicks)
            scoreValue += _checkDog(3,9.8,key,presentTicks,a) 
        elif a[4] == 0:
            countPlaySFX += _callCat(4,13.1,countPlaySFX,presentTicks)
            scoreValue += _checkCat(4,13.1,key,presentTicks,a)
        elif a[5] == 0:
            countPlaySFX += _callDog(5,16.32,countPlaySFX,presentTicks)
            scoreValue += _checkDog(5,16.32,key,presentTicks,a)
        elif a[6] == 0:
            countPlaySFX += _callDog(6,17.9,countPlaySFX,presentTicks)
            scoreValue += _checkDog(6,17.9,key,presentTicks,a)
        elif a[7] == 0:
            countPlaySFX += _callCat(7,19.6,countPlaySFX,presentTicks)
            scoreValue += _checkCat(7,19.6,key,presentTicks,a)
        elif a[8] == 0:
            countPlaySFX += _callCat(8,21.2,countPlaySFX,presentTicks)
            scoreValue += _checkCat(8,21.2,key,presentTicks,a)
        elif a[9] == 0:
            countPlaySFX += _callDog(9,24.5,countPlaySFX,presentTicks)
            scoreValue += _checkDog(9,24.5,key,presentTicks,a)
        elif a[10] == 0:
            countPlaySFX += _callCat(10,26.14,countPlaySFX,presentTicks)
            scoreValue += _checkCat(10,26.14,key,presentTicks,a)
        elif a[11] == 0:
            countPlaySFX += _callDog(11,29.4,countPlaySFX,presentTicks)
            scoreValue += _checkDog(11,29.4,key,presentTicks,a)
        elif a[12] == 0:
            countPlaySFX += _callCat(12,31,countPlaySFX,presentTicks)
            scoreValue += _checkCat(12,31,key,presentTicks,a)
        elif a[13] == 0:
            countPlaySFX += _callDog(13,32.6,countPlaySFX,presentTicks)
            scoreValue += _checkDog(13,32.6,key,presentTicks,a)
        elif a[14] == 0:
            countPlaySFX += _callCat(14,34.3,countPlaySFX,presentTicks)
            scoreValue += _checkCat(14,34.3,key,presentTicks,a)
        elif a[15] == 0:
            countPlaySFX += _callDog(15,37.65,countPlaySFX,presentTicks)
            scoreValue += _checkDog(15,37.65,key,presentTicks,a)
        elif a[16] == 0:
            countPlaySFX += _callDog(16,39.25,countPlaySFX,presentTicks)
            scoreValue += _checkDog(16,39.25,key,presentTicks,a)
        elif a[17] == 0:
            countPlaySFX += _callCat(17,42.55,countPlaySFX,presentTicks)
            scoreValue += _checkCat(17,42.55,key,presentTicks,a)
        elif a[18] == 0:
            countPlaySFX += _callCat(18,44.2,countPlaySFX,presentTicks)
            scoreValue += _checkCat(18,44.2,key,presentTicks,a)
        elif a[19] == 0:
            countPlaySFX += _callCat(19,47.45,countPlaySFX,presentTicks)
            scoreValue += _checkCat(19,47.45,key,presentTicks,a)
        elif a[20] == 0:
            countPlaySFX += _callDog(20,50.74,countPlaySFX,presentTicks)
            scoreValue += _checkDog(20,50.74,key,presentTicks,a)
        elif a[21] == 0:
            countPlaySFX += _callCat(21,52.3,countPlaySFX,presentTicks)
            scoreValue += _checkCat(21,52.3,key,presentTicks,a)
        elif a[22] == 0:
            countPlaySFX += _callDog(22,54.7,countPlaySFX,presentTicks)
            scoreValue += _checkDog(22,54.7,key,presentTicks,a)
        elif a[23] == 0:
            countPlaySFX += _callCat(23,57.23,countPlaySFX,presentTicks)
            scoreValue += _checkCat(23,57.23,key,presentTicks,a)
        elif a[24] == 0:
            countPlaySFX += _callDog(24,58.9,countPlaySFX,presentTicks)
            scoreValue += _checkDog(24,58.9,key,presentTicks,a)
        elif a[25] == 0:
            countPlaySFX += _callDog(25,60.5,countPlaySFX,presentTicks)
            scoreValue += _checkDog(25,60.5,key,presentTicks,a)
        elif a[26] == 0:
            countPlaySFX += _callDog(26,62.2,countPlaySFX,presentTicks)
            scoreValue += _checkDog(26,62.2,key,presentTicks,a)
        elif a[27] == 0:
            countPlaySFX += _callCat(27,63.7,countPlaySFX,presentTicks)
            scoreValue += _checkCat(27,63.7,key,presentTicks,a)
        elif a[28] == 0:
            countPlaySFX += _callCat(28,67,countPlaySFX,presentTicks)
            scoreValue += _checkCat(28,67,key,presentTicks,a)
        elif a[29] == 0:
            countPlaySFX += _callDog(29,68.6,countPlaySFX,presentTicks)
            scoreValue += _checkDog(29,68.6,key,presentTicks,a)
        elif a[30] == 0:
            countPlaySFX += _callCat(30,70.26,countPlaySFX,presentTicks)
            scoreValue += _checkCat(30,70.26,key,presentTicks,a)
        elif a[31] == 0:
            countPlaySFX += _callCat(31,71.98,countPlaySFX,presentTicks)
            scoreValue += _checkCat(31,71.98,key,presentTicks,a)
        elif a[32] == 0:
            countPlaySFX += _callDog(32,73.56,countPlaySFX,presentTicks)
            scoreValue += _checkDog(32,73.56,key,presentTicks,a)
        elif a[33] == 0:
            countPlaySFX += _callDog(33,75.2,countPlaySFX,presentTicks)
            scoreValue += _checkDog(33,75.2,key,presentTicks,a)
        elif a[34] == 0:
            countPlaySFX += _callCat(34,76.7,countPlaySFX,presentTicks)
            scoreValue += _checkCat(34,76.7,key,presentTicks,a)
        elif a[35] == 0:
            countPlaySFX += _callCat(35,80.2,countPlaySFX,presentTicks)
            scoreValue += _checkCat(35,80.2,key,presentTicks,a)
        
        #preferences
        screen.blit(bg,(0,0))
        _showCat(catX,400)
        _showDog(dogX,400)
        _showText("Shutdown",562,50)
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

        if presentTicks >= 15:
            print("eiei")
            if scoreValue > highestScore:
                highestScore = scoreValue
                print(highestScore)
            with open(highestScorePath+"/highest_score_shutdown.txt","w") as f:
                f.write(str(highestScore))
            
_play2()
