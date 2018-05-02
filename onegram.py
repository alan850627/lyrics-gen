#!/usr/bin/env python

import os
import io
import argparse
import string
import math
from random import randint

def get_word(wf):
    count = 0
    for key in wf:
        count += wf[key]
    rand = randint(1, count)
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
    for i in range(0, len(text)):
        word = text[i]
        if word not in wordfreq:
            wordfreq[word] = 1
        else:
            wordfreq[word] += 1

    sentence = ""
    word = "bless"
    for i in range(0,200):
        sentence += word + " ";
        word = get_word(wordfreq)

    print(sentence)

if __name__ == "__main__":
    main()
