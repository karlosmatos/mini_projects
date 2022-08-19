# accept text
def get_text():
    text = input('Enter any first sentence to be analyzed: ').lower().replace(',','')
    return text

# split the text into individual words that are not repeated and count every word
class WordToSentenceRatio:

    def __init__(self, text):
        self.text = text
        self.dictionary_word = {}
        
    def decompose_sentence(self):
        for word in self.text.split(' '):
            if word in self.dictionary_word.keys():
                self.dictionary_word[word] += 1
            else:
                self.dictionary_word[word] = 1
        return self.dictionary_word

    # summing every word
    def calculate_word(self):
        sum_words = sum(self.dictionary_word.values())
        return sum_words

    # calculating the word-to-sentence ratio
    def ratio_words(self, sum_words):
        for key, value in self.dictionary_word.items() :
            ratio = round(value*100 / sum_words,2)
            print(f'The word "{key}" has {ratio}% ratio in the sentence')

def main():
    text = get_text()
    function = WordToSentenceRatio(text)
    dictionary_word = function.decompose_sentence()
    sum_words = function.calculate_word()
    function.ratio_words(sum_words)

if __name__ == '__main__':
    main()