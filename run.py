from functions import *


input('\nWelcome to Tower of Py, a generic fantasy game!\nHere you will fight your way thorugh the Tower of Py and defeat the terrible rulers of your homeland: The Death Baron and The Holy Duchess.\nAre you up for the challenge?\n>')
player = create_hero()
input('{stats} \n>'.format(stats = player))

#Stage 1
stage_1(player)

#Stage 2 
stage_2(player)

#Stage 3
stage_3(player)