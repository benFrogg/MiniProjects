import random

def RockPaperScissors():
    choices = ['Rock', 'Paper', 'Scissors']

    checker = False

    while checker == False:
        answer = random.choice(choices)

        player = input("Please enter 'Rock', 'Paper' or 'Scissors'\n")

        if answer.upper() == player.upper():
            print(f'Computer: {answer:10}\nPlayer: {player:10}\nResult: Draw')
        else:
            if answer.upper() == 'ROCK':
                if player.upper() == 'SCISSORS':
                    print(f'Computer: {answer:10}\nPlayer: {player:10}\nResult: You lost')
                elif player.upper() == 'PAPER':
                    print(f'Computer: {answer:10}\nPlayer: {player:10}\nResult: You win')
            elif answer.upper() == 'PAPER':
                if player.upper() == 'ROCK':
                    print(f'Computer: {answer:10}\nPlayer: {player:10}\nResult: You lost')
                elif player.upper() == 'SCISSORS':
                    print(f'Computer: {answer:10}\nPlayer: {player:10}\nResult: You win')
            elif answer.upper() == 'SCISSORS':
                if player.upper() == 'PAPER':
                    print(f'Computer: {answer:10}\nPlayer: {player:10}\nResult: You lost')
                elif player.upper() == 'ROCK':
                    print(f'Computer: {answer:10}\nPlayer: {player:10}\nResult: You win')

        newRound = input("New Round? y/n\n")

        if newRound == 'n':
            checker = True
            print("Thank you for playing")

if __name__ == '__main__':
    RockPaperScissors()