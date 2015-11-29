import random

def Markov(text_file):

    with open(text_file) as f:    # provide a text-file to parse
        data = f.read()

    data = [i for i in data.split(' ') if i != '']     # create a list of all words 
    data = [i.lower() for i in data if i.isalpha()]    # i've been removing punctuation

    markov = {i:[] for i in data}    # i create a dict with the words as keys and empty lists as values

    pos = 0
    while pos < len(data) - 1:    # add a word to the word-key's list if it immediately follows that word
        markov[data[pos]].append(data[pos+1])
        pos += 1

    new = {k:v for k,v in zip(range(len(markov)), [i for i in markov])}    # create another dict for the seed to match up with 

    length_sentence = random.randint(15, 20)    # create a random length for a sentence stopping point

    seed = random.randint(0, len(new) - 1)    # randomly pick a starting point

    sentence_data = [new[seed]]     # use that word as the first word and starting point
    current_word = new[seed]

    while len(sentence_data) < length_sentence:
        next_index = random.randint(0, len(markov[current_word]) - 1)    # randomly pick a word from the last words list.
        next_word = markov[current_word][next_index]
        sentence_data.append(next_word)
        current_word = next_word

    return ' '.join([i for i in sentence_data])