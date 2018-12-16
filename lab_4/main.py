import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    if not texts or not isinstance(texts, list):
        return []
    lst_corpus = []
    for text in texts:
        if text and isinstance(text, str):
            lst_text = []
            words = text.split()
            for ind, el in enumerate(words):
                el.lower()
                if el.isalpha():
                    lst_text.append(el)
                else:
                    clean_word = ''
                    for element in el:
                        if element.isalpha():
                            clean_word += element
                    if clean_word:
                        lst_text.append(clean_word)
            lst_corpus.append(lst_text)


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if self.corpus:
            for text in self.corpus:
                tf = {}
                len_text = len(text)
                for word in text:
                    if word not in tf.keys():
                        num = text.count(word)
                        tf[word] = num / len_text
                self.tf_values += [tf]
        return self.tf_values

    def calculate_idf(self):
        if self.corpus:
            dict_count_texts = {}
            for text in self.corpus:
                if not text:
                    continue
                word_list = []
                for word in text:
                    if word not in word_list:
                        word_list.append(word)
                for element in word_list:
                    count_word_in_corpus = 0
                    for another_text in self.corpus:
                        if element in another_text:
                            count_word_in_corpus += 1
                    dict_count_texts[element] =count_word_in_corpus
                    self.idf_values[element] = math.log(len(self.corpus / dict_count_texts.get(element)))
            return self.idf_values

    def calculate(self):
        if self.tf_values and self.idf_values:
            for elenent in self.tf_values:
                tf_idf = {}
                for word, tf in elenent.items():
                    tf_idf[word] = tf * self.idf_values.get(word)
                self.tf_idf_values += [tf_idf]
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if not self.tf_idf_values or document_index >= len(self.tf_idf_values):
            return ()
        tf_idf = self.tf_idf_values[document_index]
        significance = sorted(tf_idf)
        return tf_idf.get(word, significance.index(word))


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
