import random

def choose_option():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera ->')
    user_option = user_option.lower()

    if not user_option in options:
        print('esa opción no es valida')
        #continue
        return None, None

    computer_option = random.choice(options)

    print('user option =>', user_option)
    print('computer option =>', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('usario ganó!')
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('computer ganó!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('ganó user!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('computer ganó')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'tijera':
            print('tijera gana a papel')
            print('ganó computer')
            computer_wins += 1
        else: 
            print('papel le gana a piedra')
            print('el usuario ganó')
            user_wins += 1         

    return user_wins, computer_wins

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print("*" * 10)
        print('Round', rounds)
        print('*' * 10)

        print('computer wins', computer_wins) 
        print('user wins', user_wins)
        rounds += 1

        user_option, computer_option = choose_option()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)  

        if computer_wins == 2:
            print('el ganador es la computadora')
            break
        if user_wins == 2:
            print('el ganador es el usuario')
            break

run_game()