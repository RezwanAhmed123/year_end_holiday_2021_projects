board_placement = {
    1: ' ',
    2: ' ',
    3: ' ',
    4: ' ',
    5: ' ',
    6: ' ',
    7: ' ',
    8: ' ',
    9: ' '
}

board_wipe = {
    1: ' ',
    2: ' ',
    3: ' ',
    4: ' ',
    5: ' ',
    6: ' ',
    7: ' ',
    8: ' ',
    9: ' '
}



def show_game():
    print(f"""
    {board_placement[7]}|{board_placement[8]}|{board_placement[9]}
    - - -
    {board_placement[4]}|{board_placement[5]}|{board_placement[6]}
    - - -
    {board_placement[1]}|{board_placement[2]}|{board_placement[3]}
    """)
