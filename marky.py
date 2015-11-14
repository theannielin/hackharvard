import markovify
import scrapy
import os
import tempfile
from subprocess import call


call(["scrapy", "runspider", "stackoverflow_spider.py", "-o", "~/Desktop/bobo.json"])

# Get raw text as string.
with open("~/Desktop/bobo.json") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print(text_model.make_short_sentence(140))

os.remove("~/Desktop/bobo.json")