"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:
    global frequencies
    frequencies = {}

    if text == None or type(text) != str:
        return frequencies
    elif not text:
        return frequencies
    elif type(text) == str:
        for spam in text:
            if spam in """1234567890-_+=()"*&?^:%$;№'#"@!`~:<>/\|].,}[{""":
                text = text.replace(spam, ' ')

        split_text = text.lower()
        split_text = text.split(' ')

        if '\n' in split_text or '' in split_text:
            while '\n' in split_text:
                split_text.remove('\n')
            while '' in split_text:
                split_text.remove('')
                
        for word in split_text:
            quantity_words = split_text.count(word)
            frequencies[word] = quantity_words

        return frequencies
    else:
        return frequencies



def filter_stop_words(freq_dict: dict, stop_words: tuple) -> dict:
    
    new_frequencies = frequencies.copy()

    if stop_words == None or new_frequencies == None:
        return new_frequencies

    if stop_words:
        for s_w in stop_words:
            if s_w in new_frequencies:
                new_frequencies.pop(s_w)

    return new_frequencies

def get_top_n(frequencies: dict, top_n: int) -> tuple:
    if not top_n > 0:
        return ()
    else:
        n = 0
        top_n_list = []
        for key in frequencies.keys():
            if top_n == n:
                break
            else:
                n = n + 1
                top_n_list.append(key)

    top_n_list = tuple(top_n_list)
    return top_n_list
