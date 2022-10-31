
from lib2to3.pytree import convert
from select import select
from turtle import pos
import pygame

pygame.font.init()
pygame.mixer.init()

# Part 1 basic attribute in all function
WIDTH, HEIGHT = 1280, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Olvan!")


BLACK = (0,0,0)
BACKGROUND = pygame.transform.scale(pygame.image.load(
    'Olvan_Assets/Select music/Select_music_page.png'),(WIDTH,HEIGHT))

#ทุกสิ่งที่กดได้
Blueblock = pygame.image.load('Olvan_Assets/Select music/Box.png').convert_alpha()
homeButton = pygame.image.load('Olvan_Assets/Select music/Home_button.png').convert_alpha()
playButton = pygame.image.load('Olvan_Assets/Select music/'+'Play_button.png').convert_alpha()

# Blueblock properties
posBlueblock1_x,posBlueblock1_y =  -74,227
posBlueblock2_x,posBlueblock2_y =  402,227
posBlueblock3_x,posBlueblock3_y =  878,227
Blueblock_weight , Blueblock_height = 465,445


list_song = ["Jingle Bell","Shutdown",
"Too Cute"] #เวลาจะเพิ่มหรือลด มาแก้ตรงนี้พอ
num_song = len(list_song)

detailfont = pygame.font.SysFont("arialblack",40)
# แสดงรูปภาพที่เป็นรูปเฉย ๆ
def displayIcon(music,x,y):
    icon = pygame.image.load('Olvan_Assets/Select Music/'+ music +'_icon.png').convert_alpha()
    WIN.blit(icon,(x,y))


#แสดงข้อมความ เปลี่ยนทุกรอบเมื่อ state เปลี่ยน
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
   
   
    WIN.blit(Music1 ,(posBlueblock1_x+Blueblock_weight/2 - Music1.get_width()/2
    ,posBlueblock1_y + Blueblock_height/2 - Music1.get_height()/2 + 50))
    WIN.blit(Music2 ,(posBlueblock2_x+Blueblock_weight/2 - Music2.get_width()/2
    ,posBlueblock2_y + Blueblock_height/2 - Music2.get_height()/2 + 50))
    WIN.blit(Music3 ,(posBlueblock3_x+Blueblock_weight/2 - Music3.get_width()/2
    ,posBlueblock3_y + Blueblock_height/2 - Music3.get_height()/2 + 50))

    displayIcon(Music1name,69,272)
    displayIcon(Music2name,545,272)
    displayIcon(Music3name,1021,272)
    #แสดง icon
    

def displayBox(x,y,image):
    displayBox_image = pygame.image.load(image).convert_alpha()
    display_rect = displayBox_image.get_rect(center = (x,y))
    WIN.blit(displayBox_image,display_rect)
#def button():



#def selectMusic():
def draw_window():
    WIN.blit(BACKGROUND,(0,0))
    
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
    
    WIN.blit(image,(display_blueblock.x,display_blueblock.y))

    return action 

def game_loop(state,playingGame): #game loop 
    
    while playingGame:
        for event in pygame.event.get():
            draw_window()
            Music = detailfont.render(list_song[state],True,BLACK)
            WIN.blit(Music ,(posBlueblock2_x+Blueblock_weight/2 - Music.get_width()/2
            ,posBlueblock2_y + Blueblock_height/2 - Music.get_height()/2 + 50))
            pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    playingGame = False
        





def main():
    # ตัวบอกสเตตัส programRunning คือ โปรแกรมทั้งหมด selectMenu = หน้าเลือกเพลง
    programRunning,selectMenu = True,True 
    # playingGame หน้าเล่นเกม homePage หน้าแรก
    playingGame,homePage = False,False
    stateMusic = 1 # เพลงที่เล่น 
    while programRunning :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                programRunning = False
                
            #print(Bluesquare_img)
            if selectMenu:
                draw_window()
                #Part แสดงกล่องฟ้า ปุ่ม และคลิกกล่องฟ้า
                if draw_button(-74,227,Blueblock) :
                    if stateMusic == 0:
                        stateMusic = num_song-1
                    else: 
                        stateMusic -= 1
                if draw_button(402,227,Blueblock) :
                    playingGame = True
                    selectMenu = False
                if draw_button(878,227,Blueblock) :
                    if stateMusic == num_song-1:
                        stateMusic = 0
                    else: 
                        stateMusic += 1
                #แสดงปุ่ม เล่นและย้อนกลับ
                if draw_button(16,20,homeButton):
                    homePage = True
                    selectMenu = False
                
                if draw_button(525,532,playButton):
                    playingGame = True
                    selectMenu = False

                #Part กดคีย์บอร์ด
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        if stateMusic == 0:
                            stateMusic = num_song-1
                        else:
                             stateMusic -= 1
                    if event.key == pygame.K_j:
                        if stateMusic == num_song-1:
                            stateMusic = 0
                        else: 
                            stateMusic += 1

                    if event.key == pygame.K_RETURN:
                        playingGame = True
                        selectMenu = False

                displayDetail(stateMusic)
            #กรณีที่อยู่หน้าเล่นเกม
            elif not selectMenu and playingGame:
                draw_window()
                Music = detailfont.render(list_song[stateMusic],True,BLACK)
                WIN.blit(Music ,(posBlueblock2_x+Blueblock_weight/2 - Music.get_width()/2
                ,posBlueblock2_y + Blueblock_height/2 - Music.get_height()/2 + 50))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        playingGame = False
                        selectMenu = True
            #กรณีอยู่หน้า homepage
            elif not selectMenu and homePage:
                print("ok")
                selectMenu = True
                homePage = False

        pygame.display.update()
    pygame.quit()
    quit()
if __name__ == "__main__":
    main()
