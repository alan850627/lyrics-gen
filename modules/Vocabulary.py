
import numpy as np
import codecs
import io
import sys
import re

class Vocabulary:
    vocabulary = {}
    binary_vocabulary = {}
    char_lookup = {}
    size = 0
    separator = '->'

    def generate(self, input_file_path):
        with io.open(input_file_path,'r',encoding='utf8') as f:
            text = f.read()
            tok = [x for x in text.split(' ')]
            index = 0
            for word in tok:
                if word not in self.vocabulary:
                    self.vocabulary[word] = index
                    self.char_lookup[word] = word
                    index += 1
            self.set_vocabulary_size()
            self.create_binary_representation()

    def retrieve(self, input_file_path):
        with io.open(input_file_path,'r',encoding='utf8') as f:
            text = f.read()
            tok = [x for x in text.split(self.separator)]
            for i in range(0, len(tok)-1, 2):
                key = tok[i]
                value = tok[i+1]
                value = np.fromstring(value, sep=',')
                self.binary_vocabulary[key] = value
                self.vocabulary[key] = np.where(value == 1)[0][0]
                self.char_lookup[np.where(value == 1)[0][0]] = key
        self.set_vocabulary_size()

    def create_binary_representation(self):
        for key, value in list(self.vocabulary.items()):
            binary = np.zeros(self.size)
            binary[value] = 1
            self.binary_vocabulary[key] = binary

    def set_vocabulary_size(self):
        self.size = len(self.vocabulary)
        print("Vocabulary size: {}".format(self.size))

    def get_serialized_binary_representation(self):
        string = ""
        np.set_printoptions(threshold=sys.maxsize)
        for key, value in list(self.binary_vocabulary.items()):
            array_as_string = np.array2string(value, separator=',', max_line_width=self.size * self.size)
            string += "{}{}{}{}".format(key, self.separator, array_as_string[1:len(array_as_string) - 1], self.separator)
        return string
