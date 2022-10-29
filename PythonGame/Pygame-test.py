from re import S
from winreg import HKEY_LOCAL_MACHINE
import pygame
import os
pygame.init()
pygame.font.init()
WIDTH,HEIGHT = 1280,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Cotton Game")
pygame.display.update()


WHITE = (255,255,255) # set the value of white color
BLACK = (0,0,0) # set the value of white color
RED = (255,0,0)
YELLOW = (255,255,0)
# fuction for keep the game open
FPS = 60 #set fps value
VEL = 5
BULLET_VEL = 7
SPACESHIP_WIDTH , SPACESHIP_HEIGHT = 55,40
BORDER = pygame.Rect(WIDTH//2 - 5,0,10,HEIGHT)
MAX_BULLETS = 3

RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2 #custome user event # make unique event ID 


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    ),270)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    ),270)
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')),(WIDTH,HEIGHT))

HEALTH_FONT = pygame.font.SysFont('comicsans',40)




def draw_window(red,yellow, red_bullets, yellow_bullets,red_health, yellow_health): #displaying function
    #WIN.fill(WHITE) #display white screenimage.png
    WIN.blit(BACKGROUND,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER) #Show the rectangle on the screen

    red_health_text = HEALTH_FONT.render("HEALTH:" + str(red_health),1,WHITE)
    yellow_health_text = HEALTH_FONT.render("HEALTH:" + str(yellow_health),1,WHITE)
    WIN.blit(red_health_text,(10, 10 ))
    WIN.blit(yellow_health_text,(WIDTH - yellow_health_text.get_width() -10 , 10 ))

    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y)) #assign value everytime
    WIN.blit(RED_SPACESHIP,(red.x,red.y)) #assign value everytime

    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)

    pygame.display.update()


def red_handle_movement(keys_pressed,red): #control a red spaceship movement
        if keys_pressed[pygame.K_a] and red.x - VEL > 0: #LEFT 
            red.x -= VEL
        if keys_pressed[pygame.K_d] and red.x + VEL + red.width< BORDER.x: #RIGHT
            red.x += VEL
        if keys_pressed[pygame.K_w] and red.y - VEL > 0: #UP
            red.y -= VEL
        if keys_pressed[pygame.K_s] and red.y + VEL + red.height< HEIGHT-15 :#DOWN
            red.y += VEL


def yellow_handle_movement(keys_pressed,yellow): #control a red spaceship movement
        if keys_pressed[pygame.K_LEFT] and yellow.x - VEL > BORDER.x + BORDER.width: #LEFT 
            yellow.x -= VEL
        if keys_pressed[pygame.K_RIGHT]and yellow.x + VEL + yellow.width< WIDTH: #RIGHT
            yellow.x += VEL
        if keys_pressed[pygame.K_UP] and yellow.y - VEL > 0: #UP
            yellow.y -= VEL
        if keys_pressed[pygame.K_DOWN] and yellow.y + VEL + yellow.height< HEIGHT-15: #DOWN
            yellow.y += VEL

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in red_bullets:
        bullet.x += BULLET_VEL
        if yellow.colliderect(bullet): #check that the bullet collide or not?
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x > WIDTH:
             red_bullets.remove(bullet)

    for bullet in yellow_bullets:
        bullet.x -= BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x < 0:
             yellow_bullets.remove(bullet)


def main():
    yellow = pygame.Rect(800,220,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red = pygame.Rect(100,220,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red_bullets = []
    yellow_bullets = []
    red_health = 10
    yellow_health = 10
    clock = pygame.time.Clock()
    open = True
    while open:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                open = False

            if event.type ==pygame.KEYDOWN: #Press key or not
                if event.key == pygame.K_LCTRL and len(red_bullets)< MAX_BULLETS:
                    bullet = pygame.Rect(red.x + red.width,red.y + red.height//2 - 2 , 10 , 5) 
                    #use //2 instead of /2 because it must be only integers in pygame.Rect
                    red_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(yellow_bullets)< MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x ,yellow.y + yellow.height//2 - 2 , 10 , 5)
                    yellow_bullets.append(bullet)    

            if event.type == RED_HIT:
                red_health -=1


            if event.type == YELLOW_HIT:
                yellow_health -=1 
           

        winner_text = ""
        if red_health <=0:
            winner_text = "Yellow Wins!"
        if yellow_health <= 0:
            winner_text = "Red Wins!"
        if winner_text != "":
            pass # SOMEONE WIN

       # yellow.x +=1
        
        
        
    # control spaceship
       
        keys_pressed = pygame.key.get_pressed()
        red_handle_movement(keys_pressed,red), 
        yellow_handle_movement(keys_pressed,yellow)

        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
