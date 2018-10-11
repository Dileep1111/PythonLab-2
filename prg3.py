import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import bigrams

def Summarize():
    with open(r'input.txt', 'r') as f:
        data = f.read()
        print(f'Text from the input file: \n\n,{data}')
    # Word Tokenizer , which tokenizes into words
    data_word = word_tokenize(data)
    # Sentence Tokanizer, which tokenizes into words
    data_sent = sent_tokenize(data)
    lemmatizer = WordNetLemmatizer()
    data_lemmatized = []
    for word in data_word:
        # Lemmatize the words from tokenized words
        fr_lema = lemmatizer.lemmatize(word.lower())
        data_lemmatized.append(fr_lema)

    print(f'**Lemmatized Data:** \n\n, {data_lemmatized}', "\n")

    bigram_data = []
    # Forms the bigrams from the lemmatized data
    for grams in bigrams(data_lemmatized):
        bigram_data.append(grams)
    print(f'**Bigram Data:** \n\n,{bigram_data}', "\n")
    # Calculates the frequency of the bigram_data
    fdist1 = nltk.FreqDist(bigram_data)
    # Finds the most common
    bigram_freq = fdist1.most_common()
    print(f'**Bigrams with Frequency:** \n,{bigram_freq}',"\n")
    # Finds the to 5 common elements
    top_five = fdist1.most_common(5)
    print(f'**Top five Bigrams with frequency:** \n,{top_five}',"\n")
    #Summarizing the data
    rep_sent1 = []
    for sent in data_sent:
        for word, words in bigram_data:
            for ((s, t), l) in top_five:
                if (word, words == s, t):
                    rep_sent1.append(sent)
    print("**Summarized Data** \n")
    print(max(rep_sent1, key=len))


if __name__ == '__main__':
    Summarize()