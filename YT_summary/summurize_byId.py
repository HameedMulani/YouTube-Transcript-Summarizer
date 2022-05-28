import bs4 as bs
import urllib.request
import re
import nltk
import heapq
from youtube_transcript_api import YouTubeTranscriptApi as yta
#nltk.download('punkt')
nltk.download('stopwords')
#nltk.download('corpus')



#get youTube video ID https://www.youtube.com/watch?v=UUheH1seQuE 
#https://www.youtube.com/watch?v=AwA0Jnfj3ao
vid_link = "https://www.youtube.com/watch?v=UUheH1seQuE"
vid_id = vid_link.split("=")[1]
# vid_id = 'UUheH1seQuE'

# get transcript from id 
data = yta.get_transcript(vid_id)

transcript = ""
for value in data:
    for key, val in value.items():
        if key == "text":
            transcript += val 

lines = transcript.splitlines()
final_transcript = ". ".join(lines)
# print(final_transcript)


# Removing Square Brackets and Extra Spaces
final_transcript = re.sub(r'\[[0-9]*\]', ' ', final_transcript)
final_transcript = re.sub(r'\s+', ' ', final_transcript)

# Removing special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', final_transcript )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
sentence_list = nltk.sent_tokenize(final_transcript)
# print(sentence_list)

stopwords = nltk.corpus.stopwords.words('english')


# print(stopwords_o)

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
    maximum_frequncy = max(word_frequencies.values())
# print(word_frequencies)


for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    sentence_scores = {}


for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 35:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
# print(sentence_scores)



summary_sentences = heapq.nlargest(9, sentence_scores, key=sentence_scores.get)
# print(summary_sentences)
summary = ' '.join(summary_sentences)

#summary = re.sub("[|/'-<>]", ' ', summary)
print(summary)

print(len(final_transcript))

print(len(summary))

