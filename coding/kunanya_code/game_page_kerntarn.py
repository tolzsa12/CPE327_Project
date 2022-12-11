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
    with open(highestScorePath+"/highest_score_kerntarn.txt","r") as f:
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
    pygame.mixer.music.load(musicPath+"/kern_tarn_music.mp3")
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
            countPlaySFX += _callCat(1,10.77,countPlaySFX,presentTicks)
            scoreValue += _checkCat(1,10.77,key,presentTicks,a)
        elif a[2] == 0:
            countPlaySFX += _callCat(2,12.15,countPlaySFX,presentTicks)
            scoreValue += _checkCat(2,12.15,key,presentTicks,a)
        elif a[3] == 0:
            countPlaySFX += _callCat(3,13.35,countPlaySFX,presentTicks)
            scoreValue += _checkCat(3,13.35,key,presentTicks,a) 
        elif a[4] == 0:
            countPlaySFX += _callDog(4,14.86,countPlaySFX,presentTicks)
            scoreValue += _checkDog(4,14.86,key,presentTicks,a)
        elif a[5] == 0:
            countPlaySFX += _callDog(5,16.12,countPlaySFX,presentTicks)
            scoreValue += _checkDog(5,16.12,key,presentTicks,a)
        elif a[6] == 0:
            countPlaySFX += _callDog(6,17.5,countPlaySFX,presentTicks)
            scoreValue += _checkDog(6,17.5,key,presentTicks,a)
        elif a[7] == 0:
            countPlaySFX += _callCat(7,19.9,countPlaySFX,presentTicks)
            scoreValue += _checkCat(7,19.9,key,presentTicks,a)
        elif a[8] == 0:
            countPlaySFX += _callDog(8,22.84,countPlaySFX,presentTicks)
            scoreValue += _checkDog(8,22.84,key,presentTicks,a)
        elif a[9] == 0:
            countPlaySFX += _callDog(9,24.11,countPlaySFX,presentTicks)
            scoreValue += _checkDog(9,24.11,key,presentTicks,a)
        elif a[10] == 0:
            countPlaySFX += _callDog(10,25.28,countPlaySFX,presentTicks)
            scoreValue += _checkDog(10,25.28,key,presentTicks,a)
        elif a[11] == 0:
            countPlaySFX += _callDog(11,26.8,countPlaySFX,presentTicks)
            scoreValue += _checkDog(11,26.8,key,presentTicks,a)
        elif a[12] == 0:
            countPlaySFX += _callCat(12,28.02,countPlaySFX,presentTicks)
            scoreValue += _checkCat(12,28.02,key,presentTicks,a)
        elif a[13] == 0:
            countPlaySFX += _callDog(13,29.266,countPlaySFX,presentTicks)
            scoreValue += _checkDog(13,29.266,key,presentTicks,a)
        elif a[14] == 0:
            countPlaySFX += _callCat(14,30.783,countPlaySFX,presentTicks)
            scoreValue += _checkCat(14,30.783,key,presentTicks,a)
        elif a[15] == 0:
            countPlaySFX += _callDog(15,32.19,countPlaySFX,presentTicks)
            scoreValue += _checkDog(15,32.19,key,presentTicks,a)
        elif a[16] == 0:
            countPlaySFX += _callDog(16,33.498,countPlaySFX,presentTicks)
            scoreValue += _checkDog(16,33.498,key,presentTicks,a)
        elif a[17] == 0:
            countPlaySFX += _callCat(17,34.856,countPlaySFX,presentTicks)
            scoreValue += _checkCat(17,34.856,key,presentTicks,a)
        elif a[18] == 0:
            countPlaySFX += _callDog(18,36.157,countPlaySFX,presentTicks)
            scoreValue += _checkDog(18,36.157,key,presentTicks,a)
        elif a[19] == 0:
            countPlaySFX += _callDog(19,37.525,countPlaySFX,presentTicks)
            scoreValue += _checkDog(19,37.525,key,presentTicks,a)
        elif a[20] == 0:
            countPlaySFX += _callCat(20,40.746,countPlaySFX,presentTicks)
            scoreValue += _checkCat(20,40.746,key,presentTicks,a)
        elif a[21] == 0:
            countPlaySFX += _callCat(21,42.771,countPlaySFX,presentTicks)
            scoreValue += _checkCat(21,42.771,key,presentTicks,a)
        elif a[22] == 0:
            countPlaySFX += _callDog(22,44.132,countPlaySFX,presentTicks)
            scoreValue += _checkDog(22,44.132,key,presentTicks,a)
        elif a[23] == 0:
            countPlaySFX += _callDog(23,45.4,countPlaySFX,presentTicks)
            scoreValue += _checkDog(23,45.4,key,presentTicks,a)
        elif a[24] == 0:
            countPlaySFX += _callDog(24,46.6,countPlaySFX,presentTicks)
            scoreValue += _checkDog(24,46.6,key,presentTicks,a)
        elif a[25] == 0:
            countPlaySFX += _callCat(25,48.172,countPlaySFX,presentTicks)
            scoreValue += _checkCat(25,48.172,key,presentTicks,a)
        elif a[26] == 0:
            countPlaySFX += _callDog(26,49.47,countPlaySFX,presentTicks)
            scoreValue += _checkDog(26,49.47,key,presentTicks,a)
        elif a[27] == 0:
            countPlaySFX += _callDog(27,50.7,countPlaySFX,presentTicks)
            scoreValue += _checkDog(27,50.7,key,presentTicks,a)
        elif a[28] == 0:
            countPlaySFX += _callCat(28,52.03,countPlaySFX,presentTicks)
            scoreValue += _checkCat(28,52.03,key,presentTicks,a)
        elif a[29] == 0:
            countPlaySFX += _callDog(29,53.429,countPlaySFX,presentTicks)
            scoreValue += _checkDog(29,53.429,key,presentTicks,a)
        elif a[30] == 0:
            countPlaySFX += _callCat(30,54.8,countPlaySFX,presentTicks)
            scoreValue += _checkCat(30,54.8,key,presentTicks,a)
        elif a[31] == 0:
            countPlaySFX += _callDog(31,57.45,countPlaySFX,presentTicks)
            scoreValue += _checkDog(31,57.45,key,presentTicks,a)
        elif a[32] == 0:
            countPlaySFX += _callCat(32,58.8,countPlaySFX,presentTicks)
            scoreValue += _checkCat(32,58.8,key,presentTicks,a)
        elif a[33] == 0:
            countPlaySFX += _callDog(33,60.043,countPlaySFX,presentTicks)
            scoreValue += _checkDog(33,60.043,key,presentTicks,a)
        elif a[34] == 0:
            countPlaySFX += _callCat(34,61.37,countPlaySFX,presentTicks)
            scoreValue += _checkCat(34,61.37,key,presentTicks,a)
        elif a[35] == 0:
            countPlaySFX += _callDog(35,64.78,countPlaySFX,presentTicks)
            scoreValue += _checkDog(35,64.78,key,presentTicks,a)
        
        #preferences
        screen.blit(bg,(0,0))
        _showCat(catX,400)
        _showDog(dogX,400)
        _showText("Kern Tarn",562,50)
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
            if scoreValue > highestScore:
                highestScore = scoreValue
            with open(highestScorePath+"/highest_score_kerntarn.txt","w") as f:
                f.write(str(highestScore))
            
_play2()
