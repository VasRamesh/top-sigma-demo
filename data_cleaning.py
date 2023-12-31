from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from youtube_transcript_api import YouTubeTranscriptApi

# Download NLTK data (if not already downloaded)
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


def preprocess(data: list) -> str:
    stopwords = nltk.corpus.stopwords.words('english')
    lemmatizer = WordNetLemmatizer()
    script = ""
    for dic in data:
        text = dic['text'].split()
        for word in text:
            if word not in stopwords:
                script += lemmatizer.lemmatize(word.lower()) + " "

    sentences = []
    sentence = ""
    for i in range(1, len(script.split())):
        sentence += script.split()[i - 1] + " "
        if i % 15 == 0:
            sentences.append(sentence)
            sentence = ""

    return sentences


def add_transcript(videos: list):
    count = 0
    for i, video in enumerate(videos):
        video_id = video['video_id']

        try:
            data = YouTubeTranscriptApi.get_transcript(video_id=video_id)
            sentences = preprocess(data)
            video['sentences'] = sentences
        except:
            count += 1
            print(f"Error for video_id={video_id} ({count}/{i})")

def cleanup(videos: list):
    # 20 video captions with errors: 180 left
    """ Delete video entries with no captions """
    for i, video in enumerate(videos):
        if 'sentences' not in video.keys():
            del videos[i]


