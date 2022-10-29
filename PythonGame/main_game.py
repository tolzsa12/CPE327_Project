import imp


import game

g = game.Game()
list_song = ["Jingle Bell","Shutdown","เกินต้าน"]
num_song = len(list_song)
while g.running:
    #g.playing = True
    g.curr_menu.display_menu()
    g.game_loop()

