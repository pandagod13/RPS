
import random


def get_choices():
    option = ["Rock", "Paper", "Scissor"]
    player_choice = input("Enter a choice(Rock, Paper ,Scissor)")
    computer_choice = random.choice(option)   
    choices = {'player' : player_choice, 'computer' : computer_choice}
    return choices

def check_win(player, computer):
    print("You chose " + player + ", computer chose " + computer)
    if player == computer:
        return "draw"
    elif player == 'Rock' :
        if computer == 'Scissor':
            return "Rock smashes Scissors, you win "
        else:
            return "Paper wraps Rock , you lose"
    elif player == 'Paper':
        if computer == 'Scissor':
            return "Scissors cuts Paper, you lose! "
        else:
            return "Paper wraps Rock, You win!"
    elif player == 'Scissor':
        if computer == 'Rock':
            return "Rock smashes Scissors, you lose! "
        else:
            return "Scissors cuts Paper, You win!"

choices = get_choices()
result = check_win(choices['player'], choices['computer'] )
print (result) 
