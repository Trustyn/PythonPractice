import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scisors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return f"The computer chose {computer} and you chose {user} which makes it a tie"
    if is_win(user, computer):
        return f"The computer chose {computer} and you chose {user} which means you won!"
    return f"The computer chose {computer} and you chose {user} which means you lost!"

def is_win(player, opponent):
    # Rock > Scissor, Scissor > Paper, Paper > Rock
    # Return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
        return True

print(play())