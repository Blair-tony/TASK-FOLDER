from getpass import getpass

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
         (player1_choice == 'paper' and player2_choice == 'rock') or \
         (player1_choice == 'scissors' and player2_choice == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def main():
    choices = ['rock', 'paper', 'scissors']
    player1_score = 0
    player2_score = 0
    player1_choices = []
    player2_choices = []

    num_rounds = int(input("Enter the number of rounds: "))

    for round in range(1, num_rounds + 1):
        print("\nRound", round)
        print("Player 1's turn:")
        player1_choice = getpass("Enter your choice (rock, paper, scissors): ").lower()
        while player1_choice not in choices:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            player1_choice = getpass("Enter your choice (rock, paper, scissors): ").lower()
        player1_choices.append(player1_choice)

        print("Player 2's turn:")
        player2_choice = getpass("Enter your choice (rock, paper, scissors): ").lower()
        while player2_choice not in choices:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            player2_choice = getpass("Enter your choice (rock, paper, scissors): ").lower()
        player2_choices.append(player2_choice)

        result = determine_winner(player1_choice, player2_choice)
        print(result)

        if result == "Player 1 wins!":
            player1_score += 1
        elif result == "Player 2 wins!":
            player2_score += 1

    print("\nGame over!")
    print("Player 1's score:", player1_score)
    print("Player 2's score:", player2_score)

    print("\nPlayer 1's choices:", ', '.join(player1_choices))
    print("Player 2's choices:", ', '.join(player2_choices))

if __name__ == "__main__":
    main()
