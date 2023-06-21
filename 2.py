article_text=input("Enter Data:")
import re
import nltk
article_text = article_text.lower()
article_text
# remove spaces, punctuations and numbers
clean_text = re.sub('[^a-zA-Z]', ' ', article_text)
clean_text = re.sub('\s+', ' ', clean_text)
clean_text
# split into sentence list
sentence_list = nltk.sent_tokenize(article_text)
sentence_list
## run this cell once to download stopwords
# import nltk
# nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(clean_text):
    if word not in stopwords:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
maximum_frequency = max(word_frequencies.values())

for word in word_frequencies:
    word_frequencies[word] = word_frequencies[word] / maximum_frequency
sentence_scores = {}

for sentence in sentence_list:
    for word in nltk.word_tokenize(sentence):
        if word in word_frequencies and len(sentence.split(' ')) < 30:
            if sentence not in sentence_scores:
                sentence_scores[sentence] = word_frequencies[word]
            else:
                sentence_scores[sentence] += word_frequencies[word]
word_frequencies

sentence_scores
# get top 5 sentences
import heapq
summary = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)

print(" ".join(summary))
