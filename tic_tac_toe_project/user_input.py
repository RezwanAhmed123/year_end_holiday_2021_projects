import board_interface
import checking_winner

players = ["X", "O"]


def player_turns(turn_counter):
    if turn_counter % 2 == 0:
        player = players[0]
    else:
        player = players[1]
    player_turn = int(input(f"It is your turn {player}, please decide which square you want to occupy: "))
    if board_interface.board_placement[player_turn] == ' ':
        board_interface.board_placement[player_turn] = player
        board_interface.show_game()
        turn_counter += 1
        if turn_counter == 9:
            print("Its a tie!")
        win = checking_winner.check_winner(board_interface.board_placement, player)
        if win:
            print(f"{player} wins!")
            turn_counter = 9
    else:
        print("Please input a square that has not been occupied!")
    return turn_counter
