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

pygame.init()
pygame.display.set_caption("gameV.0.1")

screen = pygame.display.set_mode((1280, 800))
bg=pygame.image.load(gamePagePath+"/game_page.png")
dog = pygame.image.load(gamePagePath+"/dog.png")
cat = pygame.image.load(gamePagePath+"/cat.png")
sushi = pygame.image.load(gamePagePath+"/sushi.png")
food = pygame.image.load(gamePagePath+"/food.png")
cloud = pygame.image.load(gamePagePath+"/cloud.png")

pygame.display.set_icon(dog)


screen.blit(sushi,(138,495))
screen.blit(food,(1047,495))

font=pygame.font.Font(fontPath+"/trebuc.ttf",32)

catX = 497
dogX = 666
totalScore = 0
cloudX = 0
cloudBack = 0




#array.array("i")                
#a = array.array("i",(0 for i in range(0,33)))

def _showText(text,x,y):
    showText=font.render(text,True,(0,0,0))
    screen.blit(showText, (x,y))

def _showCat(x,y):
    screen.blit(cat,(x,y))

def _showDog(x,y):
    screen.blit(dog,(x,y))

def _showCloud(x,y):
    screen.blit(cloud,(x,y))

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        catX = 255
                
               
    if keys[pygame.K_j]:
        dogX = 915
        
        
   
    screen.blit(bg,(0,0))
    screen.blit(sushi,(138,495))
    screen.blit(food,(1047,495))
    

    
    
    
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
        
    _showText("Score: "+str(totalScore),554,730)
    
    pygame.time.delay(10)
    catX = 497
    dogX = 666
    pygame.display.update()
