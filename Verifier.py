class Verifier:

    def __init__(self):
        self.left_to_play_list = []
        self.set_up_game()

    def set_up_game(self):
        play_list = []
        play_list.append('1. Ettor')
        play_list.append('2. Tvåor')
        play_list.append('3. Treor')
        play_list.append('4. Fyror')
        play_list.append('5. Femmor')
        play_list.append('6. Sexor')
        play_list.append('7. Par')
        play_list.append('8. Tvåpar')
        play_list.append('9. Tretal')
        play_list.append('10. Fyrtal')
        play_list.append('11. Kåk')
        play_list.append('12. Liten stege')
        play_list.append('13. Stor stege')
        play_list.append('14. Chans')
        play_list.append('15. Yatzy')
        self.left_to_play_list = play_list

    def can_play(self, play):
        return play in self.left_to_play_list

    def update_plays(self, play):
        self.left_to_play_list.remove(play)

    def game_finished(self):
        return len(self.left_to_play_list) == 0

    def plays_left(self):
        return self.left_to_play_list

    def print_plays_left(self):
        print('Det du fortfarande har kvar att spela är: ')
        for item in self.left_to_play_list:
            print(item)
