import re
import string
from typing import List
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
from .singleton import singleton
from gensim.models import KeyedVectors
from pathlib import Path
import numpy as np
from scipy import spatial
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

nltk.data.path.append(str(Path(__file__).parent.parent / "assets"))


@singleton
class Lemmatizer(object):
    def __init__(self) -> None:
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize(self, text: str) -> str:
        return self.lemmatizer.lemmatize(text)


@singleton
class Embedder(object):
    def __init__(self, path: Path) -> None:
        if not path:
            path = (
                Path(__file__).parent.parent
                / "assets"
                / "word2vec"
                / "GoogleNews-vectors-negative300.bin"
            )
        self.model = KeyedVectors.load_word2vec_format(str(path), binary=True)

    def embed(self, word):
        if word in self.model:
            return self.model[word]
        return None

    def __contains__(self, word):
        return word in self.model


def clean(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[.*?]", "", text) # remove anything in brackets
    text = re.sub(r"[%s]" % re.escape(string.punctuation), "", text) # remove spaces within brackets
    text = re.sub(r"\w*\d\w*", "", text) # remove words with digits in them
    text = re.sub(r"[‘’“”…]", "", text) # remove quotes
    text = re.sub(r"\n", "", text) # strip newlines
    return text


def avg(embeddings: List[np.array]) -> np.array:
    if not embeddings:
        return np.empty(0)
    features = np.zeros(embeddings[0].shape)
    for embedding in embeddings:
        features = np.add(features, embedding)
    return np.divide(features, len(embeddings))


def vectorize(text: str, remove_stopwords: bool) -> np.array:
    text = clean(text)
    tokens = word_tokenize(text)
    if remove_stopwords:
        tokens = [token for token in tokens if token not in stopwords.words("english")]
    lemmatizer = Lemmatizer.instance()
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    embedder = Embedder.instance()
    embeddings = [embedder.embed(lemma) for lemma in lemmas if lemma in embedder]
    return avg(embeddings)


def set_assets(assets: Path):
    embedder = Embedder.instance(
        path=Path(assets) / "word2vec" / "GoogleNews-vectors-negative300.bin"
    )
    nltk.data.path.append(assets)


def similarity(x: str, y: str, remove_stopwords: bool = True) -> float:
    xembed = vectorize(x, remove_stopwords)
    yembed = vectorize(y, remove_stopwords)
    return 1 - spatial.distance.cosine(xembed, yembed)
