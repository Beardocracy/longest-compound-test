#!/usr/bin/env python3
''' This file contains the class Trie
    The script below takes a filename for a file with a list of words,
    prints the number of words that are constructed wholly from other words,
    and finally prints the longest compound word.
'''

import sys
import requests
import json


class Trie:
    ''' Prefix data structure for storing words '''
    def __init__(self):
        self.root = {'*': '*'}

    def add_word(self, word):
        ''' Adds word to trie, adds * at end of word to denote end '''
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                current_node[letter] = {}
            current_node = current_node[letter]
        current_node['*'] = '*'

    def does_word_exist(self, word):
        ''' Checks if word is a word in the trie '''
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return '*' in current_node

    def is_compound(self, word):
        ''' Checks if word is made up entirely of other words in trie '''
        current_node = self.root
        for i in range(0, len(word)):
            if word[i] not in current_node:
                return False
            current_node = current_node[word[i]]
            if '*' in current_node and i + 1 < len(word):
                if self.does_word_exist(word[i + 1:]):
                    return True
                if (self.is_compound(word[i + 1:])):
                    return True
        return False


# initialize instance of data structure
trie = Trie()

words = []
'''
# Parse gist_id from url
url = sys.argv[1]
gist_id = url.split('/')[-1]
x = requests.get('https://api.github.com/gists/{}'.format(gist_id))

py_dict = x.json()
raw_url = py_dict['files']['words.txt']['raw_url']

# build list of words from raw data from gist using raw_url
words = requests.get(raw_url).text.split('\n')
'''

'''
with open('small_list.txt', 'r') as fp:
    for line in fp:
        words.append(line.strip())
'''

with open('big_list.txt', 'r') as fp:
    for line in fp:
        words.append(line.strip())

# create trie structure
for word in words:
    trie.add_word(word)

compound_words = 0
longest_compound = ['']

# count the compound words and save the longest
for word in words:
    is_compound = trie.is_compound(word)
    if is_compound:
        compound_words = compound_words + 1
        # Handle edge case of multiple longest compounds
        if len(longest_compound[0]) < len(word):
            longest_compound = []
            longest_compound.append(word)
        elif len(word) == len(longest_compound[0]):
            longest_compound.append(word)

# print both longest compound words in case of ties
if len(longest_compound) == 1:
    print('{}'.format(longest_compound[0]))
else:
    for compound in longest_compound:
        print('{}'.format(compound))

print('{}'.format(compound_words))
