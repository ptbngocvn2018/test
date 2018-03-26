#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 17:46:50 2018

@author: ptbngoc
"""

import numpy as np
import re
import string
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#load text
filename = "plain_text.txt"
file = open(filename,'rt')
text = file.read()
file.close()
#split into words by white space
words = text.split()
#print(words[:100])
#split based on words only
#words_1 = re.split(r'\W+',text)
#print(words_1)

#remove punctuation from each word
table = str.maketrans('','',string.punctuation)
stripped = [w.translate(table) for w in words]
#print(stripped[:100])

#convert to lower case
words = [word.lower() for word in words]
#print(words[:100])

#split into sentences
sentences = sent_tokenize(text)
#print(sentences[0])

#split into words
tokens = word_tokenize(text)
#print(tokens[:100])
#remove all tokens that are not alphabetic
words = [word for word in tokens if word.isalpha()]
#print(words[:100])

stop_words = stopwords.words('english')
#print(stop_words)