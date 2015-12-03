# marky.py
# Authors: {Annie Lin, Joanne Koong}
# Date: {December 7, 2015}
# Emails: {annielin@college.harvard.edu, joannekoong@college.harvard.edu}
# ----------------
# Using our Markov chain framework, this file generates the sentences requested.

import markov
import scrapy
import sys
import os
import tempfile
from subprocess import call
import re

def marky(num_sentences, tag):
    if os.path.isfile("~/Desktop/bobo.json"):
        os.remove("~/Desktop/bobo.json")

    call(["scrapy", "runspider", "stackoverflow_spider.py", "-a", "tag=%s" %tag ,"-o", "~/Desktop/bobo.json"])

    # Get raw text as string.
    with open("~/Desktop/bobo.json") as f:
        text = f.read()

    # Build the model.
    m = markov.Markov() 
    text_model = m.marking("~/Desktop/bobo.json") 

    sentence = ''

    # Print five randomly-generated sentences
    for i in range(num_sentences): 
        m = markov.Markov() 
        ans = m.marking("~/Desktop/bobo.json") 
        if ans:
            re.sub(r'\<.*?\>', '', ans)
            # Add a period for punctuation
            sentence += ans[0].upper() + ans[1:] + ". "
        else:
            sentence += 'Recompile.'

    os.remove("~/Desktop/bobo.json")

    return sentence.rstrip('\n')