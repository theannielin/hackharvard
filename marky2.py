import markovify
import scrapy
import sys
import os
import tempfile
from subprocess import call
import re

def marky2(num_sentences, tag):
    if os.path.isfile("~/Desktop/bobo.json"):
        os.remove("~/Desktop/bobo.json")

    call(["scrapy", "runspider", "stackoverflow_spider.py", "-a", "tag=%s" %tag ,"-o", "~/Desktop/bobo.json"])

    # Get raw text as string.
    with open("~/Desktop/bobo.json") as f:
        text = f.read()

    # Build the model.
    text_model = markov2.marking("~/Desktop/bobo.json") 

    sentence = ''

    # Print five randomly-generated sentences
    for i in range(num_sentences):
        ans = text_model.make_sentence()
        ans = ans.replace('\n', 'recompile')
        if ans:
            re.sub(r'\<.*?\>', '', ans)
            if ans != '\n':
                sentence += str(ans.rstrip('\n'))
            else:
                sentence = ans
        else:
            sentence += 'Recompile.'

    os.remove("~/Desktop/bobo.json")

    return sentence.rstrip('\n')

print(marky2(5,"python"))
