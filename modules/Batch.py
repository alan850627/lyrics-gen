#!/usr/bin/env python

import codecs
from modules.Vocabulary import *


class Batch:
    dataset_full_passes = 0

    def __init__(self, data_file_name, vocabulary_file_path, batch_size, sequence_length):
        with io.open(data_file_name,'r',encoding='utf8') as f:
            text = f.read()
            self.tok = [x for x in text.split(' ')]
        self.vocabulary = Vocabulary()
        self.vocabulary.retrieve(vocabulary_file_path)

        self.batch_size = batch_size
        self.sequence_length = sequence_length
        self.pt = 0

    def get_next_batch(self):
        batch_len = self.batch_size * self.sequence_length + self.batch_size
        current_batch = []

        if self.pt+batch_len > len(self.tok):
            current_batch = self.tok[self.pt:]
            while len(current_batch) < batch_len:
                current_batch.append('')
            self.pt = 0
            self.dataset_full_passes += 1
            print("Pass {} done".format(self.dataset_full_passes))
        else:
            current_batch = self.tok[self.pt:self.pt+batch_len]
            self.pt += batch_len

        batch_vector = []
        label_vector = []

        for i in np.arange(0, batch_len, self.sequence_length + 1):
            sequence = current_batch[i:i + self.sequence_length]
            label = current_batch[i]
            sequences_vector = []

            for word in sequence:
                sequences_vector.append(self.vocabulary.binary_vocabulary[word])
            batch_vector.append(sequences_vector)
            label_vector.append(self.vocabulary.binary_vocabulary[label])

        return np.asarray(batch_vector), np.asarray(label_vector)
