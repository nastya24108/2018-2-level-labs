"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
     def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        id = 1
        if word and type(word) == str:
            if word not in self.storage.keys():
                id = max(self.storage.values()) + 1
                self.storage[word] = id
            else:
                self.storage[word] = id
            return self.storage[word]
        else:
            return self.storage

    def get_id_of(self, word: str) -> int:
        if word and type(word) == str:
            if word in self.storage.keys():
                return self.storage[word]
            else:
                return None

    def get_original_by(self, id: int) -> str:
        if id and type(id) == int:
            if id in self.storage.values():
                for word in self.storage.keys():
                    if id == self.storage[word]:
                        return word
         else:
            return None

    def from_corpus(self, corpus: tuple):
        if corpus and type(corpus) == tuple:
            WordStorage.put(self, word)
        else:
            return {}


class NGramTrie:
    def __init__(self, n):
        self.size = n
        self.gram_frequencies = {}
        gram_log_probabilities = {}
        
    def fill_from_sentence(self, sentence: tuple) -> str:
        if sentence and type(sentence) == tuple:
            for i in range(len(sentence) - 1):
                bi_gram = (sentence[i], sentence[i + 1])
                if bi_gram not in self.gram_frequencies.keys():
                    self.gram_frequencies[bi_gram] = 1
                else:
                    freq = self.gram_frequencies[bi_gram]
                    self.gram_frequencies[bi_gram] = freq + 1
            return 'OK'
        else:
            return 'ERROR'

    def calculate_log_probabilities(self):
        pass

    def predict_next_sentence(self, prefix: tuple) -> list:
        pass


def encode(storage_instance, corpus) -> list:
    if storage_instance and corpus:
        list_of_id = []
        for word in corpus:
            list_of_id.append(WordStorage.get_id_of(self, word))
        return list_of_id


def split_by_sentence(text: str) -> list:
    if not text:
        return []

    my_text = []
    text = text.lower()
    text = text.replace('\n', ' ')
    if '  ' in text:
        text = text.replace('  ', ' ')

    import re
    sentence = re.split(r'[.?!]', text)

    for i in range(len(sentence)):
        one_sent = ['<s>', ]
        sentences = sentence[i].split()
        word = ''
        for el in sentences:
            for el_el in
                if el_el[1] in 'abcdefghijklmnopqrstuvwxyz':
                    word += el_el[1]
            if word:
                one_sent.append(word)
        one_sent.append('</s>')
        my_text.append(one_sent)
    return my_text
