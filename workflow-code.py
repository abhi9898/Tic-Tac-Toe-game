print("Let's play Tic Tac Toe!")

while True:
    # board reset
    fBoard = [" "] * 10
    player1_marker, player2_marker = marker_input()
    
    turn = choose_first()
    print("\n" + turn + " GOES FIRST.")
    
    play_game = input("Are you ready? Enter Yes or No")
    
    if play_game.lower()[0] == "y":
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == "Player 1":
            display_board(fBoard)
            position = player_choice(fBoard)
            
            place_marker(fBoard, player1_marker, position)
            
            if win_check(fBoard, player1_marker):
                display_board(fBoard)
                print('Player 1 WINS!')
                game_on = False
            else:
                if full_board_check(fBoard):
                    display_board(fBoard)
                    print("The game is a TIE!")
                    break
                else:
                    turn = "Player 2"
                
        else: ## Player 2 turn
            display_board(fBoard)
            position = player_choice(fBoard)
            
            place_marker(fBoard, player2_marker, position)
            
            if win_check(fBoard, player2_marker):
                display_board(fBoard)
                print("Player 2 WINS!")
                game_on = False
            else:
                if full_board_check(fBoard):
                    display_board(fBoard)
                    print("The game is a TIE!")
                    break
                else:
                    turn = "Player 1"

            
    if not replay():
        break
