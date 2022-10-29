import pygame

class Menu():
    def __init__(self,game) : #use object from game.py
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.run_display = True #tell menu to keep runnning
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = -100
        self.bg = pygame.image.load('Olvan_Assets/Select Music/Select_music_page.png')
    def blit_screen(self):
        self.game.window.blit(self.game.display,(0,0))
        pygame.display.update()
        self.game.reset_keys() #reset ทุกครั้งที่โชว์บนสกรีน
        
class SelectMusic(Menu):

    def __init__(self, game):
        Menu.__init__(self,game)
        self.list_song = ["Jingle Bell","Shutdown","Too Cute","Last Christmas","Please never fall in love again"]
        self.num_song = len(self.list_song)
       # self.state = "Start"
        self.state = 1
        self.show_song_0x, self.show_song_0y = self.mid_w,self.mid_h + 30
        self.show_song_1x, self.show_song_1y = self.mid_w, self.mid_h + 50
        self.show_song_2x,self.show_song_2y = self.mid_w,self.mid_h + 70
        self.cursor_rect.midtop = (self.show_song_0x+ self.offset , self.show_song_0y)

    def display_song(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.WHITE)
            self.game.draw_text('Main Menu',20,self.game.DISPLAY_W/2
            ,self.game.DISPLAY_H/2 - 20)
            if self.state == 0:
                #show only middle and lower game
                self.game.check_events()
                self.game.display.fill(self.game.WHITE)
                self.game.draw_text('Select Song',20,self.game.DISPLAY_W/2
                ,self.game.DISPLAY_H/2 - 20)

                self.game.draw_text(self.list_song[0],20,self.show_song_1x,
                self.show_song_1y)
                self.game.draw_text(self.list_song[1],20,self.show_song_2x,
                self.show_song_2y)
                self.blit_screen()

    
            elif self.state > 0 and self.state < self.num_song - 1 :
                 #show upper middle and lower game
                self.game.check_events()
                self.game.display.fill(self.game.WHITE)
                self.game.draw_text('Select Song',20,self.game.DISPLAY_W/2
                ,self.game.DISPLAY_H/2 - 20)

                self.game.draw_text(self.list_song[self.state-1],20,self.show_song_0x,
                self.show_song_0y)
                self.game.draw_text(self.list_song[self.state],20,self.show_song_1x,
                self.show_song_1y)
                self.game.draw_text(self.list_song[self.state+1],20,self.show_song_2x,
                self.show_song_2y)
                self.blit_screen()
                
            elif self.state == self.num_song-1:
                
                self.game.check_events()
                self.game.display.fill(self.game.WHITE)
                self.game.draw_text('Select Song',20,self.game.DISPLAY_W/2
                ,self.game.DISPLAY_H/2 - 20)
                self.game.draw_text(self.list_song[self.state-1],20,self.show_song_0x,
                self.show_song_0y)
                self.game.draw_text(self.list_song[self.state],20,self.show_song_1x,
                self.show_song_1y)

                self.blit_screen()
                
    def move_song(self):
        if self.game.DOWN_KEY:
            if self.state == 0:
                self.state +=1 
            elif self.state > 0 and self.state < self.num_song - 1 :
                self.state += 1
            elif self.state == self.num_song-1:
                pass
            print(self.state)
        if self.game.UP_KEY:
            if self.state == 0:
                pass
            elif self.state > 0 and self.state < self.num_song - 1 :
                self.state -= 1
            elif self.state == self.num_song-1:
                self.state -= 1
            print(self.state)
    
    def check_input(self):
        self.move_song()
        if self.game.START_KEY:
            self.current_song = self.list_song[self.state]
            #print(self.list_song[self.state]) 
            self.game.playing = True
            self.run_display = False
            #{แสดงค่าข้างในเกม}

