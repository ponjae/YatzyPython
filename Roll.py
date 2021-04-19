from functools import reduce
import random


class Roll:
    def __init__(self):
        self.active_dices = []
        self.kept_dices = []
        self.dictionary = {}
        self.game_setup()

    def game_setup(self):
        self.dictionary['1'] = self.check_first_part_score
        self.dictionary['2'] = self.check_first_part_score
        self.dictionary['3'] = self.check_first_part_score
        self.dictionary['4'] = self.check_first_part_score
        self.dictionary['5'] = self.check_first_part_score
        self.dictionary['6'] = self.check_first_part_score
        self.dictionary['7'] = self.check_one_pair
        self.dictionary['8'] = self.check_two_pair
        self.dictionary['9'] = self.check_three_kind
        self.dictionary['10'] = self.check_four_kind
        self.dictionary['11'] = self.check_full_house
        self.dictionary['12'] = self.check_low_straight
        self.dictionary['13'] = self.check_high_straight
        self.dictionary['14'] = self.add_chance
        self.dictionary['15'] = self.check_yatzy

    def first_roll(self):
        self.kept_dices.clear()
        rolled = [random.randint(1, 6) for _ in range(5)]
        self.active_dices = rolled

    def keep_dices(self):
        print(
            f'Ditt senaste slag: [{", ".join(str(x) for x in self.active_dices)}]')
        choice = input(
            'Vilka tärningar vill du behålla (kommaseparerad: ex 1,2,5)? ')
        split = choice.split(',')
        print(split)

        if split[0] == '':
            reassurence = input('Du vill alltså inte behålla någon (ja/nej)?')
            if reassurence[0].lower() == 'n':
                self.keep_dices()

        else:
            try:
                int_list = [int(item) for item in split]
                for die in int_list:
                    if die in self.active_dices:
                        self.kept_dices.append(die)
                        self.active_dices.remove(die)
                    else:
                        print(
                            f'Kan inte behålla tärningen med värdet {die} eftersom du inte har slagit den')
            except ValueError:
                print('FEEEL. Kan inte tolka din input som ett tal')

    def second_roll(self):
        rolled = [random.randint(1, 6) for _ in range(len(self.active_dices))]
        self.active_dices = rolled

    def get_current_dice_list(self):
        return self.active_dices

    def get_kept_dice_list(self):
        return self.kept_dices

    def third_roll(self):
        rolled = [random.randint(1, 6) for _ in range(len(self.active_dices))]
        self.kept_dices.extend(rolled)
        print(f'Dina tärningar är: {self.get_kept_dice_list()}')

    def check_first_part_score(self, dice_list, value):
        score = sum(map(lambda x: x == value, dice_list))
        return score

    def check_one_pair(self, dice_list):
        for item in dice_list:
            if dice_list.count(item) > 1:
                return True
        return False

    def check_two_pair(self, dice_list):
        dice_list.sort()
        # xx0yy
        first = dice_list[0] == dice_list[1] and dice_list[-2] == dice_list[-1]
        # 0xxyy
        second = dice_list[1] == dice_list[2] and dice_list[-2] == dice_list[-1]
        # xxyy0
        third = dice_list[0] == dice_list[1] and dice_list[2] == dice_list[3]
        return first or second or third

    def check_three_kind(self, dice_list):
        dice_list.sort()
        if len(set(dice_list)) > 3:
            return False
        return dice_list.count(dice_list[2]) >= 3

    def check_four_kind(self, dice_list):
        dice_list.sort()
        if len(set(dice_list)) > 2:
            return False
        return dice_list.count(dice_list[1]) >= 4

    def check_low_straight(self, dice_list):
        dice_list.sort()
        return len(set(dice_list)) == 5 and dice_list[0] == 1 and dice_list[-1] == 5

    def check_high_straight(self, dice_list):
        dice_list.sort()
        return len(set(dice_list)) == 5 and dice_list[0] == 2 and dice_list[-1] == 6

    def check_full_house(self, dice_list):
        dice_list.sort()

        if len(set(dice_list)) != 2:
            return False

        count_a = dice_list.count(dice_list[0])
        count_b = dice_list.count(dice_list[-1])

        return (count_a == 2 and count_b == 3) or (count_a == 3 and count_b == 2)

    def add_chance(self, dice_list):
        pass

    def check_yatzy(self, dice_list):
        if len(set(dice_list)) == 1:
            return True
        return False

    def get_methods(self):
        return self.dictionary


# roller = Roll()
# roller.first_roll()
# roller.keep_dices()
# roller.second_roll()
# print(f'Nuvarande aktiva tärningar: {roller.get_current_dice_list()}')
# print(f'Nuvarande sparade tärningar: {roller.get_kept_dice_list()}')
# roller.keep_dices()
# roller.third_roll()
# print(f'Nuvarande sparade tärningar: {roller.get_kept_dice_list()}')
