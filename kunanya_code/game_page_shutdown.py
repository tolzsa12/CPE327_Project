import pygame
import time
import array
import os


codePath = os.getcwd()
parentPath = os.path.dirname(os.getcwd())
os.chdir(parentPath)
parentPath = os.getcwd()
gamePagePath = parentPath + "/olavan_asset/game_page"
fontPath = parentPath + "/font"
musicPath = parentPath + "/music"

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


screen.blit(sushi,(138,495))
screen.blit(food,(1047,495))

pygame.mixer.music.load(musicPath+"/shutdown_music.mp3")

catX = 497
dogX = 666
cloudX = 0
cloudBack = 0

scoreValue = 0
countPlaySFX = 0
pauseTime = 0


array.array("i")                
a = array.array("i",(0 for i in range(0,36)))
a[0] = 1

def _showText(text,x,y):
    showText=font.render(text,True,(0,0,0))
    screen.blit(showText, (x,y))

def _showCat(x,y):
    screen.blit(cat,(x,y))

def _showDog(x,y):
    screen.blit(dog,(x,y))

def _showCloud(x,y):
    screen.blit(cloud,(x,y))

def testText(x):
        text=font.render(str(x),True,(0,0,0))
        screen.blit(text, (400,300))
def testText1(x):
        text=font.render(str(x),True,(0,0,0))
        screen.blit(text, (800,400))
def testText2(x):
        text=font.render(str(x),True,(0,0,0))
        screen.blit(text, (800,600))

def _callCat(n,t,countPlaySFX):
    count = 0
    if presentTicks >= t and countPlaySFX<n:
        catSound.play()
        count+=1   
    return count


def _callDog(n,t,countPlaySFX):
    count = 0
    if presentTicks >= t and countPlaySFX<n:
        dogSound.play()
        count+=1   
    return count

def _checkCat(countPlaySFX,recentSoundTime,key):
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

def _checkDog(countPlaySFX,recentSoundTime,key):
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



pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(1,0.0)
startTicks=pygame.time.get_ticks()


while True:
    key = "n"
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:            
                    catX = 255
                    key = "f"
                elif event.key == pygame.K_j: 
                    dogX = 915
                    key = "j"
                elif event.key == pygame.K_SPACE:
                    pygame.mixer.music.pause()
                    from pause_temp import _pauseTime
                    pauseTime += _pauseTime()
                    pygame.mixer.music.unpause()
                    
                    
    presentTicks=(pygame.time.get_ticks()-startTicks-pauseTime)/1000 
    
    if a[1] == 0:       
        countPlaySFX += _callDog(1,3.2,countPlaySFX)
        scoreValue += _checkDog(1,3.2,key)
    elif a[2] == 0:
        countPlaySFX += _callCat(2,6.5,countPlaySFX)
        scoreValue += _checkCat(2,6.5,key)
    elif a[3] == 0:
        countPlaySFX += _callDog(3,9.8,countPlaySFX)
        scoreValue += _checkDog(3,9.8,key) 
    elif a[4] == 0:
        countPlaySFX += _callCat(4,13.1,countPlaySFX)
        scoreValue += _checkCat(4,13.1,key)
    elif a[5] == 0:
        countPlaySFX += _callDog(5,16.32,countPlaySFX)
        scoreValue += _checkDog(5,16.32,key)
    elif a[6] == 0:
        countPlaySFX += _callDog(6,17.9,countPlaySFX)
        scoreValue += _checkDog(6,17.9,key)
    elif a[7] == 0:
        countPlaySFX += _callCat(7,19.6,countPlaySFX)
        scoreValue += _checkCat(7,19.6,key)#now
    elif a[8] == 0:
        countPlaySFX += _callCat(8,21.2,countPlaySFX)
        scoreValue += _checkCat(8,21.2,key)#now
    elif a[9] == 0:
        countPlaySFX += _callDog(9,24.5,countPlaySFX)
        scoreValue += _checkDog(9,24.5,key)
    elif a[10] == 0:
        countPlaySFX += _callCat(10,26.14,countPlaySFX)
        scoreValue += _checkCat(10,26.14,key)#now
    elif a[11] == 0:
        countPlaySFX += _callDog(11,29.4,countPlaySFX)
        scoreValue += _checkDog(11,29.4,key)#now
    elif a[12] == 0:
        countPlaySFX += _callCat(12,31,countPlaySFX)
        scoreValue += _checkCat(12,31,key)
    elif a[13] == 0:
        countPlaySFX += _callDog(13,32.6,countPlaySFX)
        scoreValue += _checkDog(13,32.6,key)#now
    elif a[14] == 0:
        countPlaySFX += _callCat(14,34.3,countPlaySFX)
        scoreValue += _checkCat(14,34.3,key)#now
    elif a[15] == 0:
        countPlaySFX += _callDog(15,37.65,countPlaySFX)
        scoreValue += _checkDog(15,37.65,key)
    elif a[16] == 0:
        countPlaySFX += _callDog(16,39.25,countPlaySFX)
        scoreValue += _checkDog(16,39.25,key)
    elif a[17] == 0:
        countPlaySFX += _callCat(17,42.55,countPlaySFX)
        scoreValue += _checkCat(17,42.55,key)
    elif a[18] == 0:
        countPlaySFX += _callCat(18,44.2,countPlaySFX)
        scoreValue += _checkCat(18,44.2,key)
    elif a[19] == 0:
        countPlaySFX += _callCat(19,47.45,countPlaySFX)
        scoreValue += _checkCat(19,47.45,key)
    elif a[20] == 0:
        countPlaySFX += _callDog(20,50.74,countPlaySFX)
        scoreValue += _checkDog(20,50.74,key)
    elif a[21] == 0:
        countPlaySFX += _callCat(21,52.3,countPlaySFX)
        scoreValue += _checkCat(21,52.3,key)
        #bf hook
    elif a[22] == 0:
        countPlaySFX += _callDog(22,54.7,countPlaySFX)
        scoreValue += _checkDog(22,54.7,key)
    elif a[23] == 0:
        countPlaySFX += _callCat(23,57.23,countPlaySFX)
        scoreValue += _checkCat(23,57.23,key)
    elif a[24] == 0:
        countPlaySFX += _callDog(24,58.9,countPlaySFX)
        scoreValue += _checkDog(24,58.9,key)
    elif a[25] == 0:
        countPlaySFX += _callDog(25,60.5,countPlaySFX)
        scoreValue += _checkDog(25,60.5,key)
    elif a[26] == 0:
        countPlaySFX += _callDog(26,62.2,countPlaySFX)
        scoreValue += _checkDog(26,62.2,key)
    elif a[27] == 0:
        countPlaySFX += _callCat(27,63.7,countPlaySFX)
        scoreValue += _checkCat(27,63.7,key)
    elif a[28] == 0:
        countPlaySFX += _callCat(28,67,countPlaySFX)
        scoreValue += _checkCat(28,67,key)
    elif a[29] == 0:
        countPlaySFX += _callDog(29,68.6,countPlaySFX)
        scoreValue += _checkDog(29,68.6,key)
    elif a[30] == 0:
        countPlaySFX += _callCat(30,70.26,countPlaySFX)
        scoreValue += _checkCat(30,70.26,key)
    elif a[31] == 0:
        countPlaySFX += _callCat(31,71.98,countPlaySFX)
        scoreValue += _checkCat(31,71.98,key)
    elif a[32] == 0:
        countPlaySFX += _callDog(32,73.56,countPlaySFX)
        scoreValue += _checkDog(32,73.56,key)
    elif a[33] == 0:
        countPlaySFX += _callDog(33,75.2,countPlaySFX)
        scoreValue += _checkDog(33,75.2,key)
    elif a[34] == 0:
        countPlaySFX += _callCat(34,76.7,countPlaySFX)
        scoreValue += _checkCat(34,76.7,key)
    elif a[35] == 0:
        countPlaySFX += _callCat(35,80.2,countPlaySFX)
        scoreValue += _checkCat(35,80.2,key)
    
    
    
    
    screen.blit(bg,(0,0))
    screen.blit(sushi,(138,495))
    screen.blit(food,(1047,495))

    testText(presentTicks)
    
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
    pygame.display.update()
