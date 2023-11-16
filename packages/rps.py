import random


def play_rps(playerChoice):
    choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

    computerChoice = int(random.choice('123'))

    def decider_winner(playerChoice, computerChoice):
        if playerChoice == 1 and computerChoice == 3:
            return f'You Win, Player choose {choices[playerChoice]} and Computer choose {choices[computerChoice]} !'
        elif playerChoice == 2 and computerChoice == 1:
            return f'You Win, Player choose {choices[playerChoice]} and Computer choose {choices[computerChoice]} !'
        elif playerChoice == 3 and computerChoice == 2:
            return f'You Win, Player choose {choices[playerChoice]} and Computer choose {choices[computerChoice]} !'
        elif playerChoice == computerChoice:
            return f'Tie Games, Player choose {choices[playerChoice]} and Computer choose {choices[computerChoice]} !'
        else:
            return f'You Lose, Player choose {choices[playerChoice]} and Computer choose {choices[computerChoice]} !'

    game_result = decider_winner(playerChoice, computerChoice)
    return game_result
