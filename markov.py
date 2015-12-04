# markov.py
# Authors: {Annie Lin, Joanne Koong}
# Date: {December 7, 2015}
# Emails: {annielin@college.harvard.edu, joannekoong@college.harvard.edu}
# ----------------
# Our implementation of search, Markov Chains, and weighted Markov chains. 

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
        # Just return a random answer related to the tag
        rando = random.randint(0, len(self.data) - 1)
        return self.data[rando]

    def searching(self, text_file):
        self.parse_text(text_file)
        return self.response()

class MarkovWeighting():
    def __init__(self):
        self.markov = []

    def parse_text(self, text_file):
        with open(text_file) as f:
            data = f.read()
        # Create a list of all words 
        data = [i for i in data.split(' ') if i != ''] 
        data = [i.lower() for i in data if i.isalpha()]
        self.markov = {i:[] for i in data}

        pos = 0
        while pos < len(data) - 1:    
            # Add a word to the word-key's list if it succeeds that word
            self.markov[data[pos]].append(data[pos+1])
            pos += 1

    def seeding(self):
        new = {k:v for k,v in zip(range(len(self.markov)), [i for i in self.markov])}

        # Randomly pick a starting point
        length_sentence = random.randint(15, 20)
        seed = random.randint(0, len(new) - 1)
        sentence_data = [new[seed]]
        current_word = new[seed]

        while len(sentence_data) < length_sentence:
            if len(self.markov[current_word]) == 0: 
                self.seeding()
            next_index = random.randint(0, len(self.markov[current_word]) - 1)
            # Append the random next word to the sentence
            next_word = self.markov[current_word][next_index]
            sentence_data.append(next_word)
            current_word = next_word

        return ' '.join([i for i in sentence_data])

    def marking(self, text_file):
        self.parse_text(text_file)
        return self.seeding()

class Markov():
    def __init__(self):
        self.markov = []

    def parse_text(self, text_file):
        with open(text_file) as f:
            data = f.read()
        # Create a list of all words 
        data = [i for i in data.split(' ') if i != '']
        data = [i.lower() for i in data if i.isalpha()]
        self.markov = {i:[] for i in data}

        pos = 0
        while pos < len(data) - 1:
            # Add a word to the word-key's list if it succeeds that word
            if data[pos+1] not in self.markov[data[pos]]:  
                self.markov[data[pos]].append(data[pos+1])
            pos += 1

    def seeding(self):
        new = {k:v for k,v in zip(range(len(self.markov)), [i for i in self.markov])}

        # Randomly pick a starting point
        length_sentence = random.randint(15, 20)
        seed = random.randint(0, len(new) - 1)
        sentence_data = [new[seed]]
        current_word = new[seed]

        while len(sentence_data) < length_sentence:
            if len(self.markov[current_word]) == 0: 
                self.seeding()
            next_index = random.randint(0, len(self.markov[current_word]) - 1)
            # Append the random next word to the sentence
            next_word = self.markov[current_word][next_index]
            sentence_data.append(next_word)
            current_word = next_word

        return ' '.join([i for i in sentence_data])

    def marking(self, text_file):
        self.parse_text(text_file)
        return self.seeding()