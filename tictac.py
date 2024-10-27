field = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
active_player = "X"
run = True

def print_field():
    print(field[1] + " | " + field[2] + " | " + field[3])
    print(field[4] + " | " + field[5] + " | " + field[6])
    print(field[7] + " | " + field[8] + " | " + field[9])

def next_move_player():
    global run
    while True:
        player_move = input("choose your next move (1-9) or 'q' to quit: ")
        
        if player_move.lower() == "q":
            run = False
            return None
        
        try:
            player_move = int(player_move)
        except ValueError:
            print("you have to choose a number between 1 and 9")
            continue
        
        if player_move < 1 or player_move > 9:
            print("you have to choose a number between 1 and 9")
            continue
        
        if field[player_move] == "X" or field[player_move] == "O":
            print("this field is already taken")
            continue
        
        return player_move

def change_player():
    global active_player
    if active_player == "X":
        active_player = "O"
    else:
        active_player = "X"

def check_win():
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9), 
        (1, 4, 7), (2, 5, 8), (3, 6, 9), 
        (1, 5, 9), (3, 5, 7)
    ]
    for condition in win_conditions:
        if field[condition[0]] == field[condition[1]] == field[condition[2]] and field[condition[0]] != "":
            return field[condition[0]]
    return None

def check_draw():
    for i in range(1, 10):
        if field[i] != "X" and field[i] != "O":
            return False
    return True

def start_game():
    global run
    while run:
        print_field()
        move = next_move_player()
        if move is not None:
            field[move] = active_player
        
        winner = check_win()
        if winner:
            print_field()
            print("Player " + winner + " wins!")
            run = False
        
        if check_draw():
            print_field()
            print("Draw")
            run = False
        
        change_player()

start_game()
