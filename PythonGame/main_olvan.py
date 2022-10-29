
import game_olvan

g = game_olvan.Game()

while g.running:
    #g.playing = True
    g.curr_menu.display_song()
    g.game_loop()

