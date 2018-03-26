#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 10:01:38 2018

@author: ptbngoc
"""

import numpy as np
import string
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

#load data
filename = "plain_text.txt"
file = open(filename, 'rt')
text = file.read()
file.close()
#split into words
tokens = word_tokenize(text)
#convert to lower case
tokens = [w.lower() for w in tokens]
#remove punctuation from each word
table = str.maketrans('','',string.punctuation)
stripped = [w.translate(table) for w in tokens]
#remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
#filter out stop words
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words[:100])

#stemming of words
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in tokens]
print(stemmed[:100])