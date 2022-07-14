# accept text (no function needed)
text_a = input('Enter any first sentence to be analyzed: ').lower().replace(',','')

# split the text into individual words that are not repeated and count every word
def decompose_sentence(text_a):
    dictionary_word = {}
    for word in text_a.split(' '):
        if word in dictionary_word.keys():
            dictionary_word[word] += 1
        else:
            dictionary_word[word] = 1
    return dictionary_word

# summing every word
def calculate_word(dictionary_word):
    sum_words = sum(dictionary_word.values())
    return sum_words

# calculating the word-to-sentence ratio
def ratio_words(dictionary_word, sum_words):
    for key,value in dictionary_word.items() :
        ratio = round(value*100 / sum_words,2)
        print(f'The word "{key}" has {ratio}% ratio in the sentence')

def main():
    dictionary_word = decompose_sentence(text_a)
    sum_words = calculate_word(dictionary_word)
    ratio_words(dictionary_word, sum_words)

if __name__ == '__main__':
    main()
