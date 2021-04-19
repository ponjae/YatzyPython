from Player import Player
from Verifier import Verifier
from Roll import Roll


def main():
    playerList = []

    nbr_players = input(
        'Hej! Välkomna till det här enkla Yatzy-spelet. Var vänlig och ange antalet deltagare (1-4): ')
    try:
        nbr = int(nbr_players)
        if nbr < 1 or nbr > 4:
            raise ValueError()
        for i in range(nbr):
            name = input(f'Skriv in namnet för spelare {i+1}: ')

            playerList.append(Player(name, Verifier(), Roll()))
    except ValueError:
        print('Error. Var vänlig och försök igen och ange antalet deltager i siffror mellan 1-4.')

    plays_list = playerList[0].get_verifier().plays_left()

    while len(plays_list) > 0:
        for p in playerList:
            roller = p.get_roller()
            verifier = p.get_verifier()
            roller.first_roll()
            roller.keep_dices()
            roller.second_roll()
            roller.keep_dices()
            roller.third_roll()
            verifier.print_plays_left()
            current_dices = roller.get_kept_dice_list()
            choice = input(
                'Var vänlig att skriv det nummer som du vill lägga till din poäng på (om du inte kan, skriv x:"NUMMER ATT STRYKA"): ')
            todo = roller.get_methods().get(choice)
            if todo(current_dices):
                print(f'Lägger till ponäng i {todo}')


main()
