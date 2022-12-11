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

pygame.mixer.music.load(musicPath+"/kern_tarn_music.mp3")

catX = 497
dogX = 666
cloudX = 0
cloudBack = 0

scoreValue = 0
countPlaySFX = 0


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



pygame.mixer.music.set_volume(0.29)
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
                    
    presentTicks=(pygame.time.get_ticks()-startTicks)/1000 
    
    if a[1] == 0:       
        countPlaySFX += _callCat(1,10.77,countPlaySFX)
        scoreValue += _checkCat(1,10.77,key)
    elif a[2] == 0:
        countPlaySFX += _callCat(2,12.15,countPlaySFX)
        scoreValue += _checkCat(2,12.15,key)
    elif a[3] == 0:
        countPlaySFX += _callCat(3,13.35,countPlaySFX)
        scoreValue += _checkCat(3,13.35,key) 
    elif a[4] == 0:
        countPlaySFX += _callDog(4,14.86,countPlaySFX)
        scoreValue += _checkDog(4,14.86,key)
    elif a[5] == 0:
        countPlaySFX += _callDog(5,16.12,countPlaySFX)
        scoreValue += _checkDog(5,16.12,key)
    elif a[6] == 0:
        countPlaySFX += _callDog(6,17.5,countPlaySFX)
        scoreValue += _checkDog(6,17.5,key)
    elif a[7] == 0:
        countPlaySFX += _callCat(7,19.9,countPlaySFX)
        scoreValue += _checkCat(7,19.9,key)#now
    elif a[8] == 0:
        countPlaySFX += _callDog(8,22.84,countPlaySFX)
        scoreValue += _checkDog(8,22.84,key)#now
    elif a[9] == 0:
        countPlaySFX += _callDog(9,24.11,countPlaySFX)
        scoreValue += _checkDog(9,24.11,key)
    elif a[10] == 0:
        countPlaySFX += _callDog(10,25.28,countPlaySFX)
        scoreValue += _checkDog(10,25.28,key)#now
    elif a[11] == 0:
        countPlaySFX += _callDog(11,26.8,countPlaySFX)
        scoreValue += _checkDog(11,26.8,key)#now
    elif a[12] == 0:
        countPlaySFX += _callCat(12,28.02,countPlaySFX)
        scoreValue += _checkCat(12,28.02,key)
    elif a[13] == 0:
        countPlaySFX += _callDog(13,29.266,countPlaySFX)
        scoreValue += _checkDog(13,29.266,key)
    elif a[14] == 0:
        countPlaySFX += _callCat(14,30.783,countPlaySFX)
        scoreValue += _checkCat(14,30.783,key)#now
    elif a[15] == 0:
        countPlaySFX += _callDog(15,32.19,countPlaySFX)
        scoreValue += _checkDog(15,32.19,key)
    elif a[16] == 0:
        countPlaySFX += _callDog(16,33.498,countPlaySFX)
        scoreValue += _checkDog(16,33.498,key)
    elif a[17] == 0:
        countPlaySFX += _callCat(17,34.856,countPlaySFX)
        scoreValue += _checkCat(17,34.856,key)
    elif a[18] == 0:
        countPlaySFX += _callDog(18,36.157,countPlaySFX)
        scoreValue += _checkDog(18,36.157,key)
    elif a[19] == 0:
        countPlaySFX += _callDog(19,37.525,countPlaySFX)
        scoreValue += _checkDog(19,37.525,key)
    elif a[20] == 0:
        countPlaySFX += _callCat(20,40.746,countPlaySFX)
        scoreValue += _checkCat(20,40.746,key)
    elif a[21] == 0:
        countPlaySFX += _callCat(21,42.771,countPlaySFX)
        scoreValue += _checkCat(21,42.771,key)
    elif a[22] == 0:
        countPlaySFX += _callDog(22,44.132,countPlaySFX)
        scoreValue += _checkDog(22,44.132,key)
    elif a[23] == 0:
        countPlaySFX += _callDog(23,45.4,countPlaySFX)
        scoreValue += _checkDog(23,45.4,key)
    elif a[24] == 0:
        countPlaySFX += _callDog(24,46.6,countPlaySFX)
        scoreValue += _checkDog(24,46.6,key)
    elif a[25] == 0:
        countPlaySFX += _callCat(25,48.172,countPlaySFX)
        scoreValue += _checkCat(25,48.172,key)
    elif a[26] == 0:
        countPlaySFX += _callDog(26,49.47,countPlaySFX)
        scoreValue += _checkDog(26,49.47,key)
    elif a[27] == 0:
        countPlaySFX += _callDog(27,50.7,countPlaySFX)
        scoreValue += _checkDog(27,50.7,key)
    elif a[28] == 0:
        countPlaySFX += _callCat(28,52.03,countPlaySFX)
        scoreValue += _checkCat(28,52.03,key)
    elif a[29] == 0:
        countPlaySFX += _callDog(29,53.429,countPlaySFX)
        scoreValue += _checkDog(29,53.429,key)
    elif a[30] == 0:
        countPlaySFX += _callCat(30,54.8,countPlaySFX)
        scoreValue += _checkCat(30,54.8,key)
    elif a[31] == 0:
        countPlaySFX += _callDog(31,57.45,countPlaySFX)
        scoreValue += _checkDog(31,57.45,key)
    elif a[32] == 0:
        countPlaySFX += _callCat(32,58.8,countPlaySFX)
        scoreValue += _checkCat(32,58.8,key)
    elif a[33] == 0:
        countPlaySFX += _callDog(33,60.043,countPlaySFX)
        scoreValue += _checkDog(33,60.043,key)
    elif a[34] == 0:
        countPlaySFX += _callCat(34,61.37,countPlaySFX)
        scoreValue += _checkCat(34,61.37,key)
    elif a[35] == 0:
        countPlaySFX += _callDog(35,64.78,countPlaySFX)
        scoreValue += _checkDog(35,64.78,key)
    
    
    
    
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
