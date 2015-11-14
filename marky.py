import markovify
import scrapy
import sys
import os
import tempfile
from subprocess import call
import re

num_sentences = int(sys.argv[1])
tag = str(sys.argv[2])

call(["scrapy", "runspider", "stackoverflow_spider.py", "-a", "tag=%s" %tag ,"-o", "~/Desktop/bobo.json"])


# Get raw text as string.
with open("~/Desktop/bobo.json") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(num_sentences):
	ans = text_model.make_sentence()
	if ans: 
		re.sub(r'\<.*?\>', '', ans)
		print(ans)

os.remove("~/Desktop/bobo.json")