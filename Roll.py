class Roll:
    def __init__(self):
        pass

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
