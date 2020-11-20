from textblob import TextBlob

text = TextBlob('it was a wonderful movie, i liked it')
print(text.sentences)

print('Positive{} '.format(text.sentiment.polarity))

print('Negativity{} '.format(text.sentiment.subjectivity))
