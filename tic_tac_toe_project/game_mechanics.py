import user_input
import board_interface

print('''
This is a 2 player game.
Each person must choose a number 1 to 9 to input into the tic-tac-toe table.
You cannot put conquer a space that is already taken.
Enjoy!
''')
turn = 0
play = True
while play:
    while turn < 9:
        new_turn = user_input.player_turns(turn)
        turn = new_turn
    status = input("Do you want to play again? (y/n): ").lower()
    if status != "y":
        play = False
    else:
        turn = 0
        board_interface.board_placement = board_interface.board_wipe
