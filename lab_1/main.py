"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:
    import string
    global frequencies
    frequencies = {}

    if text == None or type(text) != str:
        return frequencies
    elif not text:
        return frequencies
    elif type(text) == str:
        split_text = text.lower()
        split_text = text.split(' ')
        for word in split_text:
            for i in string.punctuation:
                text = text.replace(i, '')
                
            if not word or word.isdigit():
                continue
            
            if frequencies.get(word) == None:
                frequencies[word] = 1
            
            else:
                frequencies.update({word: frequencies[word] + 1})
                
        return frequencies
    
#         spam_symb = """1234567890-_+=()"*&?^:%$;№'#"@!`~:<>/\|].,}[{"""
#         for spam in text:
#             if spam in spam_symb:
#                 text = text.replace(spam, ' ')

#         split_text = text.lower()
#         split_text = text.split(' ')
        
#         if '\n' in split_text or '' in split_text:
#             while '\n' in split_text:
#                 split_text.remove('\n')
#             while '' in split_text:
#                 split_text.remove('')   
      
#         for word in split_text:
#             new_line = ''
#             for symbol in word:
#                 if symbol not in spam_symb:
#                     new_line = new_line + symbol
            
#             if new_line:
#                 if new_line not in frequencies:
#                     frequencies[new_line] = 1
#                 else:
#                     new_value = frequencies[new_line] + 1
#                     frequencies[new_line] = new_value
                    
#             quantity_words = split_text.count(word)
#             frequencies[word] = quantity_words
            
#         return frequencies
#     else:
#         return frequencies



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
