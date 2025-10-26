# Sv
#Task 2: Rock Paper Scissors

def rock_pape_sciss():
    print("=== Rock Paper Scissors Game ===")
    
    #this is to track the win count and rounds 
    wins = 0
    rounds = 0
    #while loop goes on for 5 rounds and count increases
    while rounds < 5:
        rounds += 1
        print("--- Game", rounds, "---")
        
        #players input their choises
        player_a = input("Player A's choice: ").lower().strip()
        player_b = input("Player B's choice: ").lower().strip()
        
        #this printes both choises rogether 
        print("Player A chose: " + player_a)
        print("Player B chose: " + player_b)
        
        # seeing if any of these requirements are met by players responce to get the winner
        if player_a == player_b:
            print("Result: tie")
        elif player_a == "rock" and player_b == "scissors":
            print("Result: A")
            wins += 1
        elif player_a == "rock" and player_b == "paper":
            print("Result: B")
        elif player_a == "paper" and player_b == "rock":
            print("Result: A")
            wins += 1
        elif player_a == "paper" and player_b == "scissors":
            print("Result: B")
        elif player_a == "scissors" and player_b == "paper":
            print("Result: A")
            wins += 1
        elif player_a == "scissors" and player_b == "rock":
            print("Result: B")
        else:
            print("Invalid input! Please enter rock, paper, or scissors.")
            rounds -= 1
        
        print() 
    
    # this shows final results after 5 games
    print("=== Final Results ===")
    print("Player A wins:", wins)
    print("Player B wins:", 5 - wins)
    
    #result is showed at the end 
    if wins == 0 and (5 - wins) == 5:
        print("It's a tie!")
    elif wins > 2:
        print("Winner: Player A!")
    elif wins < 2:
        print("Winner: Player B!")
    else:
        print("It's a tie!")
    
    # asking user to play again 
    again = input("Would you like to play again? (y/n): ")
    
    # seeing if its a 'y' or a 'n'.
    if again.lower() == 'y':
        rock_pape_sciss()  #calling it again to replay
    else:
        print("Goodbye! Thanks for playing!")

# starting the game 
rock_pape_sciss()