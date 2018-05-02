#!/usr/bin/env python

import os
import io
import argparse
import string
import pandas as pd
import math
from random import randint

def get_word(df):
    rand = randint(1, len(df.word))
    for index, row in df.iterrows():
        if (rand <= row['frequency']):
            return row['word']
        else:
            rand -= row['frequency']

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--training_file', type=str, required=True)
    args = parser.parse_args()
    
    training_file = args.training_file
    text = []
    with io.open(training_file,'r',encoding='utf8') as f:
        text = f.read().lower().split(' ')

    # Count the words
    totalwords = 0
    wordfreq = []
    words = []
    for word in text:
        if word not in words:
            count = text.count(word)
            wordfreq.append([word, count])
            words.append(word)
            totalwords += count

    # Make into pandas dataframe
    df = pd.DataFrame(wordfreq, columns=['word','frequency'])

    # Find the top 10 words
    print("Top 10 most common words from all the papers:")
    print(df.nlargest(10, 'frequency')['word'].tolist())
    print 

    # Calculate entropy
    SUM = 0
    for index, row in df.iterrows():
        pi = float(row['frequency'])/float(totalwords)
        SUM += pi * math.log(pi, 2)
    entropy = -SUM
    print("Entropy of words: %f bits" % entropy)


    sentence = ""
    for i in range(0,200):
        sentence += get_word(df) + " ";

    print("Here is our generated paragraph:")
    print(sentence)

if __name__ == "__main__":
    main()
