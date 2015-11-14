import markovify
import scrapy
import sys
import os
import tempfile
from subprocess import call

num_sentences = int(sys.argv[1])

call(["scrapy", "runspider", "stackoverflow_spider.py", "-o", "~/Desktop/bobo.json"])

# Get raw text as string.
with open("~/Desktop/bobo.json") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(num_sentences):
    print(text_model.make_sentence())

os.remove("~/Desktop/bobo.json")