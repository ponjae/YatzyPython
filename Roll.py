class Roll:
    def __init__(self):
        pass

    def check_one_pair(self, dice_list):
        pass

    def check_two_pair(self, dice_list):
        pass

    def check_three_kind(self, dice_list):
        pass

    def check_four_kind(self, dice_list):
        dice_list.sort()
        if len(set(dice_list)) > 2:
            return False
        return dice_list.count(dice_list[1]) >= 4

    def check_low_straight(self, dice_list):
        dice_list.sort()
        return len(set(dice_list)) == 5 and dice_list[0] == 1

    def check_high_straight(self, dice_list):
        dice_list.sort()
        return len(set(dice_list)) == 5 and dice_list[0] == 2

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


roller = Roll()

print(roller.check_four_kind([1, 1, 1, 2, 2]))
