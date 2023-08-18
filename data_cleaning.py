from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Download NLTK data (if not already downloaded)
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
