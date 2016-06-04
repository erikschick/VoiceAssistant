import os
from os import listdir
from os.path import isfile, join
import Speech


class MusicHandler:
    MUSIC_PATH = "D:\\Music\\Music\\"

    def __init__(self, _):
        all_files = [f for f in listdir(self.MUSIC_PATH) if isfile(join(self.MUSIC_PATH, f)) and ".jpg" not in f]
        print("Which song?")
        user_input = Speech.listen()
        print("Searching songs...")
        self.find_song(all_files, user_input)

    @staticmethod
    def contains_word(query, parent_string):
        return query.lower() + " " in parent_string.lower() or " " + query.lower() in parent_string.lower()

    def find_song(self, all_files, user_input):
        potential_files = []
        for f in all_files:
            if self.contains_word(user_input, f):
                potential_files.append(f)
        number_of_potential_songs = len(potential_files)
        if number_of_potential_songs > 20:
            print("Search something more specific. Which song?")
            self.find_song(all_files, Speech.listen())
        elif number_of_potential_songs > 1:
            print("Which song did you mean?")
            index = 1
            for f in potential_files:
                print("{}: {}".format(index, potential_files[index - 1]))
                index += 1
            index_choice = Speech.listen()
            while not index_choice.isdigit() \
                    or int(index_choice) > number_of_potential_songs \
                    or int(index_choice) == 0:
                print("Please say a valid number")
                index_choice = Speech.listen()
            chosen_file = potential_files[int(index_choice) - 1]
            print("Playing {}".format(chosen_file))
            os.startfile(self.MUSIC_PATH + chosen_file)
        elif number_of_potential_songs == 1:
            chosen_file = potential_files[0]
            print("Playing {}".format(chosen_file))
            os.startfile(self.MUSIC_PATH + chosen_file)
        else:
            print('Could not find any matching music for "{}"'.format(user_input))
