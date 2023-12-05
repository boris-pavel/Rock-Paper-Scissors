import random


def main():
    # parsing from file {NAME} {SCORE}
    file = open('rating.txt', 'r')
    scoreboard_list = file.read().splitlines()
    file.close()

    scoreboard_dict = dict()

    for player in scoreboard_list:
        scoreboard_dict.update({player.split()[0]: int(player.split()[1])})  # get name and score and update the dict

    name = input('Enter your name: ')
    print(f'Hello, {name}')
    options = input().split(',')  # get available options

    print('Okay, let\'s start')

    if name not in scoreboard_dict:
        scoreboard_dict.update({name: 0})

    while True:
        choice = input()
        if options == ['']:
            options = ['scissors', 'rock', 'paper']
        computer_choice = random.choice(options)

        if choice == '!exit':
            print('Bye!')
            break
        if choice == '!rating':
            print(f'Your rating: {scoreboard_dict[name]}')
            continue
        if choice not in options:
            print('Invalid input')
            continue

        # calculate losing options
        index = options.index(choice)
        losing_options = options[:]
        losing_options.remove(choice)

        for i in range(len(losing_options) // 2):
            if index < len(losing_options):
                losing_options.pop(index)
            else:
                losing_options.pop(0)

        if computer_choice == choice:
            scoreboard_dict[name] += 50  # updating points
            print(f'There is a draw ({choice})')
        elif computer_choice in losing_options:
            scoreboard_dict[name] += 100  # updating points
            print(f'Well done. The computer chose {computer_choice} and failed')
        else:
            print(f'Sorry but the computer chose {computer_choice}')


main()
