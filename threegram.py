#!/usr/bin/env python

import os
import io
import argparse
import string
import math
from random import randint

def get_word(wf):
    rand = randint(1, len(wf))
    for key in wf:
        if (rand <= wf[key]):
            return key
        else:
            rand -= wf[key]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--training_file', type=str, required=True)
    args = parser.parse_args()
    
    training_file = args.training_file
    text = []
    with io.open(training_file,'r',encoding='utf8') as f:
        text = f.read().lower().split(' ')

    # Count the words
    wordfreq = {}
    for i in range(0, len(text)-2):
        word1 = text[i]
        word2 = text[i+1]
        word3 = text[i+2]
        if word1 not in wordfreq:
            wordfreq[word1] = {}
        if word2 not in wordfreq[word1]:
            wordfreq[word1][word2] = {}
        if word3 not in wordfreq[word1][word2]:
            wordfreq[word1][word2][word3] = 1
        else:
            wordfreq[word1][word2][word3] += 1

    sentence = "bless the "
    word1 = sentence.split()[0]
    word2 = sentence.split()[1]
    for i in range(0,200):
        word3 = get_word(wordfreq[word1][word2])
        sentence += word3 + " ";
        word1 = word2
        word2 = word3

    print("Here is our generated paragraph:")
    print(sentence)

if __name__ == "__main__":
    main()
