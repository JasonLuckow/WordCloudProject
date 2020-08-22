# Project - Word Cloud
# Author: Jason Luckow
# Date: 08/21/2020
# File: WordCloud.py
# Description:
#    This script needs to process the text, remove punctuation, ignore case and words that do not contain all alphabets,
#    count the frequencies, and ignore uninteresting or irrelevant words.  A dictionary is the output of the
#   `calculate_frequencies` function. The `wordcloud` module will then generate the image from your dictionary.

import wordcloud
from matplotlib import pyplot as plt


def _upload():
    # This is the file uploader
    file_contents = open('Eminem Word Cloud.txt')
    return file_contents.read()


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we",
                           "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by",
                           "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more",
                           "some", "such", "no", "nor", "too", "very", "can", "will", "just", "on", "so", "like", "in",
                           "up", "for", "name", "get", "know", "not", "go", "say", "out", "want", "then", "got",
                           "gonna", "every", "even", "these", "could", "come", "back", "give", "one", "see", "make",
                           "through", "thing", "down", "still", "call", "why", "about", "put", "never", "off", "take",
                           "wanna", "only", "time", "little", "people", "look", "goes", "now", "think", "next", "would",
                           "maybe", "please", "let", "way", "other", "right", "tell", "ever", "way", "than", "other",
                           "own", "around", "day", "gotta", "walk", "need", "world", "though", "grow", "sit", "lose",
                           "once", "talk", "into", "smile", "keep", "old", "before", "while", "inside", "miss",
                           "everybody", "big", "full", "stay", "run", "true", "monday", "school", "over", "yes",
                           "whatever", "save", "since", "mine", "turn", "kiss", "eyes", "head", "yourself", "spit",
                           "buy", "chance", "hit", "there", "guess", "play", "myself", "said", "made", "comes",
                           "should", "lil", "hold", "least", "mouth", "tryna"]

    punctuation_list = []
    for punctuation in punctuations:
        punctuation_list += punctuation
    frequencies = {}

    file_contents = file_contents.lower()
    file_contents = file_contents.split()
    for word in file_contents:
        if (word in (x for x in uninteresting_words)) or not word.isalpha():
            continue
        elif word not in frequencies:
            frequencies[word] = 1
        else:
            frequencies[word] += 1

    # wordcloud
    cloud = wordcloud.WordCloud(width=1000, height=1000)
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


# Display wordcloud image
file_contents = _upload()
myimage = calculate_frequencies(file_contents)

fig = plt.figure()

plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()

fig.savefig('MyWordCloud.png', dpi = 1000)




