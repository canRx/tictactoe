field = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
aktiv_player = "X"
run = True 

def print_field():
    print(field[1] + " | " + field[2] + " | " + field[3])
    print(field[4] + " | " + field[5] + " | " + field[6])
    print(field[7] + " | " + field[8] + " | " + field[9])
    return

def next_move_player():
    global run 
    while True:
        player_move = input("choose your next move (1-9): ")    
        player_move = int(player_move)
        if field[player_move] == "X" or field[player_move] == "O":
            print("this field is already taken")
            continue
        if player_move == "q" or player_move == "Q":
            run = False
            return None
        if player_move >= 1 and player_move <= 9:
            return player_move
        else:
            print("you have to choose a number between 1 and 9")

def change_player():
    global aktiv_player
    if aktiv_player == "X":
        aktiv_player = "O"
    else:
        aktiv_player = "X"
    return aktiv_player 

def start_game():
    while run:
        print_field()
        field[next_move_player()] = aktiv_player
        change_player()

start_game()