
name_one = input("Player one what is your name? ")
name_two = input("Player two what is your name? ")

game =  ("rock, paper, scissors\n")

player_one_wins = 0
player_two_wins = 0
ties = 0

while True:
        
        player_one = input("please select rock, paper or scissors: ")
        
        while player_one not in game:
            
            print("invalid choice: please select rock, paper or scissors:")

            player_one = input("please select rock, paper or scissors: ")

        print(f"{name_one} selected: {player_one}")


        player_two = input("please select rock, paper or scissors: ")

        while player_two not in game:
             
            print("invalid choice: please select rock, paper or scissors:")

            player_two = input("please select rock, paper or scissors: ")

        print(f"{name_two} selected: {player_two}")

        if player_one == player_two:
            print("it's a tie")
            ties += 1

        elif (
            (player_one == "rock" and player_two == "scissors") or
            (player_one == "paper" and player_two == "rock") or 
            (player_one == "scissors" and player_two == "paper")
        ):
            print("Player one wins")
            player_one_wins += 1
        else:
            print("player two wins")
            player_two_wins += 1

        play_again = input("do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing see you!")

            #final tally 
            print(f"{player_one} wins: {player_one_wins}")
            print(f"{player_two} wins: {player_two_wins}")
            print(f"ties: ", ties)
            break

