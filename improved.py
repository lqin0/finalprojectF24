import nltk

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

# reads the file

def fileconverter(filename):
    badcharacters = ["â","“","”","’","\x80\x99s", "\x80","\x80","\x99s","\x9d","\x99","\x9c"]
    with open(filename, 'r', encoding="latin1") as file:
        content = file.read()
    newlist = [char for char in content if char not in badcharacters]
    newlist = "".join(newlist)
    return newlist

# filters "step words" from text

def filter(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    filtered_text = " ".join(filtered_words)
    filtered_sentences = filtered_text.split(".")
    return filtered_sentences

# uses vader to take sentiment value for each sentence, then averages for full text

def sentiment_scores(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = []
    for sentence in text:
        if sentence:
            score = analyzer.polarity_scores(sentence)['compound']
            scores.append(score)
    average_score = sum(scores) / len(scores)
    return average_score

# allows for the code to process multiple articles

def averager():
    filelist = []
    scores = []
    while True:
        filepath = input("Enter a file path or type 'n' to end: ")
        if filepath.lower() == "n":
            break
        else:
            filelist.append(filepath)
    for path in filelist:
        basetext = fileconverter(path)
        filtered_sentences = filter(basetext)
        value = sentiment_scores(filtered_sentences)
        scores.append(value)
    if scores:
        average = sum(scores) / len(scores)
    else:
        average = 0 
    return average

# main

def main():
    value = averager()
    if value >= 0.05:
        print("positive", value)
    elif value <= -0.05:
        print("negative", value)
    else:
        print("neutral", value)
main()
