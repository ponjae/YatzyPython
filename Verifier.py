class Verifier:

    def __init__(self):
        self.left_to_play_list = []
        self.set_up_game()

    def set_up_game(self):
        play_list = []
        play_list.append('Ettor')
        play_list.append('Tvåor')
        play_list.append('Treor')
        play_list.append('Fyror')
        play_list.append('Femmor')
        play_list.append('Sexor')
        play_list.append('Par')
        play_list.append('Tvåpar')
        play_list.append('Tretal')
        play_list.append('Fyrtal')
        play_list.append('Kåk')
        play_list.append('Liten stege')
        play_list.append('Stor stege')
        play_list.append('Chans')
        play_list.append('Yatzy')
        self.left_to_play_list = play_list

    def can_play(self, play):
        return play in self.left_to_play_list

    def update_plays(self, play):
        self.left_to_play_list.remove(play)
