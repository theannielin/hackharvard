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

def search(tag):
    if os.path.isfile("~/Desktop/bobo.json"):
        os.remove("~/Desktop/bobo.json")

    call(["scrapy", "runspider", "stackoverflow_spider.py", "-a", "tag=%s" %tag ,"-o", "~/Desktop/bobo.json"])

    with open("~/Desktop/bobo.json") as f:
        text = f.read()

    sentences = ''

    # Print random answer related to tag
    s = markov.Search()
    ans = s.searching("~/Desktop/bobo.json") 
    if ans:
        sentences += str(ans)
    else:
        sentences += 'Recompile.'

    os.remove("~/Desktop/bobo.json")
    return sentences

if __name__ == "__main__":
    sentences = int(input('Number of sentences: '))
    tag = str(input('Tag (between quotes): '))
    print "1. SEARCH: " + search(tag)