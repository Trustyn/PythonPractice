#Modules are different files edited seperatly that can be things like "game logic" and "drawing the game"
#EXAMPLE
    
# game.py
# import the draw table
# import draw / Import all of draw but will have to specify at each function use i.e. draw.draw_game() etc
# from draw import draw_game / Import specific function
from draw import * # Import all functions

def play_game():
    ...

def main():
    result = play_game
    draw_game(result)

# this means that if the script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()

#If you had multiple draw modules with slight differences
#if visual_mode:
    # in visual mode, we draw using graphics
    #import draw_visual as draw
#else:
    # in textual mode, we print out text
    #import draw_textual as draw

#def main():
    #result = play_game()
    # this can either be visual or textual depending on visual_mode
    #draw.draw_game(result)

