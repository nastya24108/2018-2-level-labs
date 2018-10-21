"""
Labour work #2
 Check spelling of words in the given  text
"""
from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)

def propose_candidates(word: str, max_depth_permutations: int=1) -> list:

    if not word:
        return []
    if max_depth_permutations <= 0 or type(max_depth_permutations) != int:
        return []

    candidates = []
    alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(len(word)):
        word_1 = word[:i] + word[i + 1:]
        if word_1 not in candidates:
            candidates.append(word_1)

    for i in alphabet:
        for l in range(len(word)):
            word_2 = word[:l] + str(i) + word[l:]
            if word_2 not in candidates:
                candidates.append(word_2)

    for i in alphabet:
        for l in range(len(word)):
            word_3 = word[:l] + str(i) + word[l + 1:]
            if word_3 not in candidates:
                candidates.append(word_3)

    for i in range(1, len(word)):
        word_4 = word[:i - 1] + word[i] + word[i - 1] + word[i + 1:]
        if word_4 not in candidates:
            candidates.append(word_4)

    return candidates

def keep_known(candidates: tuple, frequencies: dict) -> list:

    if not candidates or not frequencies:
        return []

    known_candidates = []

    for i in candidates:
        if i in frequencies:
            known_candidates.append(i)

    return known_candidates

def choose_best(frequencies: dict, candidates: tuple) -> str:

    if not candidates or not frequencies:
        return 'UNC'

    max_num = 0
    max_num_word = ''

    for i in candidates:
        if i in frequencies:
            if int(frequencies[i]) > max_num:
                max_num = int(frequencies[i])
                max_num_word = i

    return max_num_word

def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:

    if not frequencies or frequencies == None:
        return 'UNC'

    if word in as_is_words:
        return word

    if word in frequencies:
        return word

    candidates = propose_candidates(word)
    known_candidates = keep_known(tuple(candidates), frequencies)
    best_variant = choose_best(frequencies, candidates)

    return best_variant




