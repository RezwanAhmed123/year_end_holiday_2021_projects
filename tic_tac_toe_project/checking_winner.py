victories = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
)


def check_winner(board, current_turn):
    win_status = False
    for way_to_win in victories:
        space_set_values = []
        for item in way_to_win:
            space_set_values.append(board[item])
        if space_set_values.count(current_turn) == 3:
            win_status = True
            break
    return win_status
