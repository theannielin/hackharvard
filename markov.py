# markov.py
# Authors: {Annie Lin, Joanne Koong}
# Date: {December 7, 2015}
# Emails: {annielin@college.harvard.edu, joannekoong@college.harvard.edu}
# ----------------
# This creates our Markov chains. 

import random
import json

class Search():
    def __init__(self):
        self.data = []

    def parse_text(self, text_file):
        with open(text_file) as f: 
            jsons = f.read()
            self.data = json.loads(jsons)

    def response(self):
        # just return a random answer related to the tag
        rando = random.randint(0, len(self.data) - 1)
        print self.data[rando]
        return self.data[rando]

    def searching(self, text_file):
        self.parse_text(text_file)
        return self.response()

class Weighting():
    def __init__(self):
        self.data = []

    def parse_text(self, text_file):
        data = []

class SDP():
    def __init__(self):
        self.markov = []

    def parse_text(self, text_file):
        data = []

class Markov():
    def __init__(self):
        self.markov = []

    def parse_text(self, text_file):
        with open(text_file) as f:    # provide a text-file to parse
            data = f.read()
        data = [i for i in data.split(' ') if i != '']     # create a list of all words 
        data = [i.lower() for i in data if i.isalpha()]    # i've been removing punctuation
        self.markov = {i:[] for i in data}    # i create a dict with the words as keys and empty lists as values

        pos = 0
        while pos < len(data) - 1:    # add a word to the word-key's list if it immediately follows that word
            self.markov[data[pos]].append(data[pos+1])
            pos += 1

    def seeding(self):
        new = {k:v for k,v in zip(range(len(self.markov)), [i for i in self.markov])}    # create another dict for the seed to match up with 

        length_sentence = random.randint(15, 20)    # create a random length for a sentence stopping point

        seed = random.randint(0, len(new) - 1)    # randomly pick a starting point

        sentence_data = [new[seed]]     # use that word as the first word and starting point
        current_word = new[seed]

        while len(sentence_data) < length_sentence:
            if len(self.markov[current_word]) == 0: 
                self.seeding()
            next_index = random.randint(0, len(self.markov[current_word]) - 1)    # randomly pick a word from the last words list.
            next_word = self.markov[current_word][next_index]
            sentence_data.append(next_word)
            current_word = next_word

        return ' '.join([i for i in sentence_data])

    def marking(self, text_file):
        self.parse_text(text_file)
        return self.seeding()