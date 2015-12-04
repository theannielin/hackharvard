# test.py
# Authors: {Annie Lin, Joanne Koong}
# Date: {December 7, 2015}
# Emails: {annielin@college.harvard.edu, joannekoong@college.harvard.edu}
# ----------------
# This tests search, weighting, and sequential decision-making.

import markov
import scrapy
import sys
import os
import tempfile
from subprocess import call
import re
import sys
import random

devnull = open(os.devnull, 'w')

def search(num_sentences, tag):
    if os.path.isfile("~/Desktop/bobo.json"):
        os.remove("~/Desktop/bobo.json")

    call(["scrapy", "runspider", "stackoverflow_spider.py", "-a", "tag=%s" %tag ,"-o", "~/Desktop/bobo.json"], 
         stdout=devnull, stderr=devnull)

    with open("~/Desktop/bobo.json") as f:
        text = f.read()

    sentences = ''

    # Print sentences from random answers related to tag
    for i in range(num_sentences): 
        s = markov.Search()
        ans = str(s.searching("~/Desktop/bobo.json"))
        sent_list = ans.split('.')
        rando = random.randint(0, len(sent_list) - 1)
        sentence = sent_list[rando]
        if ans:
            # remove too many spaces
            sentence = " ".join(sentence.split())
            sentences += sentence + '. '
        else:
            sentences += 'Recompile.'

    os.remove("~/Desktop/bobo.json")
    return sentences



def markovWeighting(num_sentences, tag):
    if os.path.isfile("~/Desktop/bobo.json"):
        os.remove("~/Desktop/bobo.json")

    call(["scrapy", "runspider", "stackoverflow_spider.py", "-a", "tag=%s" %tag ,"-o", "~/Desktop/bobo.json"], 
         stdout=devnull, stderr=devnull)

    with open("~/Desktop/bobo.json") as f:
        text = f.read()

    sentences = ''

    # Print sentences from random answers related to tag
    for i in range(num_sentences): 
        s = markov.Markov()
        ans = str(s.marking("~/Desktop/bobo.json"))
        sent_list = ans.split('.')
        rando = random.randint(0, len(sent_list) - 1)
        sentence = sent_list[rando]
        if ans:
            # remove too many spaces
            sentence = " ".join(sentence.split())
            sentences += sentence + '. '
        else:
            sentences += 'Recompile.'

    os.remove("~/Desktop/bobo.json")
    return sentences


def mmarkov(num_sentences, tag):
    if os.path.isfile("~/Desktop/bobo.json"):
        os.remove("~/Desktop/bobo.json")

    call(["scrapy", "runspider", "stackoverflow_spider.py", "-a", "tag=%s" %tag ,"-o", "~/Desktop/bobo.json"], 
         stdout=devnull, stderr=devnull)

    with open("~/Desktop/bobo.json") as f:
        text = f.read()

    sentences = ''

    # Print sentences from random answers related to tag
    for i in range(num_sentences): 
        s = markov.MarkovWeighting()
        ans = str(s.marking("~/Desktop/bobo.json"))
        sent_list = ans.split('.')
        rando = random.randint(0, len(sent_list) - 1)
        sentence = sent_list[rando]
        if ans:
            # remove too many spaces
            sentence = " ".join(sentence.split())
            sentences += sentence + '. '
        else:
            sentences += 'Recompile.'

    os.remove("~/Desktop/bobo.json")
    return sentences

if __name__ == "__main__":
    sentences = int(input('Number of sentences: '))
    tag = str(input('Tag (between quotes): '))
    print "1. SEARCH: " + search(sentences, tag)
    print "2. Markov: " + mmarkov(sentences, tag)
    print "3. Markov Weighting: " + markovWeighting(sentences, tag)