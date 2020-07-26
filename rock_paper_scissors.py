import random

wins = 0
losses = 0
draws = 0
message = 'Your choice - Rock(r),Paper(p),Scissors(s), Quit(q): '
choice_list = ['r','p','s','q']

while True:
    user_choice = input(message)
    while user_choice not in choice_list:
        user_choice = input(message)
    if user_choice == 'q':
        break
    else:
        computer_choice = random.choice(choice_list)
        if computer_choice == 'r':
            move = 'Rock'
        elif computer_choice == 'p':
            move = 'Paper'
        else:
            move = 'Scissors'
        print('Computer move is {0}'.format(move))

        if computer_choice == user_choice:
            draws += 1
            print('It is a draw.')
        elif (computer_choice=='r' and user_choice=='p') or (computer_choice=='p' and user_choice=='s') or (computer_choice=='s' and user_choice=='r'):
            wins += 1
            print('You win!!!')
        else:
            losses += 1
            print('You lose!!!')

print('Your wins = {0}, losses = {1}, draws = {2}'.format(wins,losses,draws))