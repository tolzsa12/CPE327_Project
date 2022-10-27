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

pygame.mixer.music.load(musicPath+"/jingle_bell_music.mp3")

catX = 497
dogX = 666
cloudX = 0
cloudBack = 0

scoreValue = 0

countSFX = 1
global countPlaySFX
countPlaySFX = 0
recentSoundTime = 1000000000
beatType = "c"


array.array("i")                
a = array.array("i",(0 for i in range(0,36)))
a[0] = 1
b = array.array("i",(0 for i in range(0,2)))

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
                    
    presentTicks=(pygame.time.get_ticks()-startTicks)/1000 
    
    if a[1] == 0:       
        countPlaySFX += _callCat(1,4.40,countPlaySFX)
        scoreValue += _checkCat(1,4.40,key)
    elif a[2] == 0:
        countPlaySFX += _callDog(2,9.1,countPlaySFX)
        scoreValue += _checkDog(2,9.1,key)
    elif a[3] == 0:
        countPlaySFX += _callCat(3,11.3,countPlaySFX)
        scoreValue += _checkCat(3,11.3,key)
    elif a[4] == 0:
        countPlaySFX += _callDog(4,13.70,countPlaySFX)
        scoreValue += _checkDog(4,13.70,key)
    elif a[5] == 0:
        countPlaySFX += _callDog(5,16,countPlaySFX)
        scoreValue += _checkDog(5,16,key)
    elif a[6] == 0:
        countPlaySFX += _callCat(6,18.3,countPlaySFX)
        scoreValue += _checkCat(6,18.3,key)
    elif a[7] == 0:
        countPlaySFX += _callDog(7,22.9,countPlaySFX)
        scoreValue += _checkDog(7,22.9,key)
    elif a[8] == 0:
        countPlaySFX += _callCat(8,25.1,countPlaySFX)
        scoreValue += _checkCat(8,25.1,key)
    elif a[9] == 0:
        countPlaySFX += _callDog(9,28.8,countPlaySFX)
        scoreValue += _checkDog(9,28.8,key)
    elif a[10] == 0:
        countPlaySFX += _callDog(10,31.1,countPlaySFX)
        scoreValue += _checkDog(10,31.1,key)
    elif a[11] == 0:
        countPlaySFX += _callCat(11,37.9,countPlaySFX)
        scoreValue += _checkCat(11,37.9,key)
    elif a[12] == 0:
        countPlaySFX += _callCat(12,38.9,countPlaySFX)
        scoreValue += _checkCat(12,38.9,key)
    elif a[13] == 0:
        countPlaySFX += _callDog(13,41.5,countPlaySFX)
        scoreValue += _checkDog(13,41.5,key)
    elif a[14] == 0:
        countPlaySFX += _callDog(14,46.1,countPlaySFX)
        scoreValue += _checkDog(14,46.1,key)
    elif a[15] == 0:
        countPlaySFX += _callDog(15,47.3,countPlaySFX)
        scoreValue += _checkDog(15,47.3,key)
    elif a[16] == 0:
        countPlaySFX += _callDog(16,48.5,countPlaySFX)
        scoreValue += _checkDog(16,48.5,key)
    elif a[17] == 0:
        countPlaySFX += _callCat(17,51.1,countPlaySFX)
        scoreValue += _checkCat(17,51.1,key)
    elif a[18] == 0:
        countPlaySFX += _callCat(18,52.9,countPlaySFX)
        scoreValue += _checkCat(18,52.9,key)
    elif a[19] == 0:
        countPlaySFX += _callCat(19,55.2,countPlaySFX)
        scoreValue += _checkCat(19,55.2,key)
    elif a[20] == 0:
        countPlaySFX += _callDog(20,57.6,countPlaySFX)
        scoreValue += _checkDog(20,57.6,key)
    elif a[21] == 0:
        countPlaySFX += _callCat(21,59.8,countPlaySFX)
        scoreValue += _checkCat(21,59.8,key)
    elif a[22] == 0:
        countPlaySFX += _callDog(22,64.56,countPlaySFX)
        scoreValue += _checkDog(22,64.56,key)
    elif a[23] == 0:
        countPlaySFX += _callCat(23,66.8,countPlaySFX)
        scoreValue += _checkCat(23,66.8,key)
    elif a[24] == 0:
        countPlaySFX += _callDog(24,70.35,countPlaySFX)
        scoreValue += _checkDog(24,70.35,key)
    elif a[25] == 0:
        countPlaySFX += _callDog(25,71.4,countPlaySFX)
        scoreValue += _checkDog(25,71.4,key)
    elif a[26] == 0:
        countPlaySFX += _callDog(26,72.6,countPlaySFX)
        scoreValue += _checkDog(26,72.6,key)
    elif a[27] == 0:
        countPlaySFX += _callCat(27,73.8,countPlaySFX)
        scoreValue += _checkCat(27,73.8,key)
    elif a[28] == 0:
        countPlaySFX += _callCat(28,76,countPlaySFX)
        scoreValue += _checkCat(28,76,key)
    elif a[29] == 0:
        countPlaySFX += _callDog(29,78.5,countPlaySFX)
        scoreValue += _checkDog(29,78.5,key)
    elif a[30] == 0:
        countPlaySFX += _callCat(30,82.9,countPlaySFX)
        scoreValue += _checkCat(30,82.9,key)
    elif a[31] == 0:
        countPlaySFX += _callCat(31,84.2,countPlaySFX)
        scoreValue += _checkCat(31,84.2,key)
    elif a[32] == 0:
        countPlaySFX += _callDog(32,85.5,countPlaySFX)
        scoreValue += _checkDog(32,85.5,key)
    elif a[33] == 0:
        countPlaySFX += _callDog(33,86.6,countPlaySFX)
        scoreValue += _checkDog(33,86.6,key)
    elif a[34] == 0:
        countPlaySFX += _callCat(34,90,countPlaySFX)
        scoreValue += _checkCat(34,90,key)
    elif a[35] == 0:
        countPlaySFX += _callCat(35,94,countPlaySFX)
        scoreValue += _checkCat(35,94,key)
    
    
    
    
    screen.blit(bg,(0,0))
    screen.blit(sushi,(138,495))
    screen.blit(food,(1047,495))

    testText(presentTicks)
    
    _showCat(catX,400)
    _showDog(dogX,400)
    _showText("Jingle Bell",562,50)
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
