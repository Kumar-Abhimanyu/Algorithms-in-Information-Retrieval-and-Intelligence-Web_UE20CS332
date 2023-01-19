
words = ["monday","monkey","money","moon"]
corrected_words = ["$"+word+"$" for word in words]

bigrams = {}

for word in corrected_words:
    for i in range(len(word)-1):
        bigram = word[i:i+2]
        if bigram in bigrams:
            bigrams[bigram].append(word.strip("$"))
        else:
            bigrams[bigram] = [word.strip("$")]

for i in bigrams.keys():
    print(i, bigrams[i])