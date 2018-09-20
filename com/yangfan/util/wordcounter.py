#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Vermouth'

import re
import io

# Define a class to process text and calculate words frequency
class CounterWords():
    # Read text file and save the words in dict
    def __init__(self, path):
        self.word_dict = dict()

        with io.open(path, encoding = "utf-8") as f:
            data = f.read()
            words = [single.lower() for single in re.findall("\w+", data)]
            for word in words:
                self.word_dict[word] = self.word_dict.get(word, 0) + 1

                # Calculate the top used words frequency

    def word_frequency(self, n):
        assert n > 0, "n should be large than 0"
        word_sort = sorted(self.word_dict.items(), key = lambda item: item[1], reverse = True)
        return word_sort[:n]


if __name__ == "__main__":
    filepath = 'C://Users//mr_yo//Desktop//work//工作//AIServer定时任务配置说明.md'
    top_commom_word = CounterWords(filepath).word_frequency(10)
    print("The top used words:")
    for word in top_commom_word:
        print(word)