============
Sentence Sim
============

A small sentence similarity library using lemmatization and word2vec

Sentsim uses the following pipeline for sentense-similiarty:
    - data clean -> remove words in brackets, words with numbers
    - tokenize using punkt tokenizer
    - lemmatize the words using the nltk wordnet lemmatization dictionary
    - embed each individual word into a feature word similarity space using the word2vec pre-trained model
    - average the each setence word2vec vectors to create a feature space
    - take the cosine distance between the two sentence vectors to obtain a similarity score between the average embeddings

Analysis
--------
Tested against the SICK https://www.kaggle.com/ozgeozkaya/sick-dataset
dataset which contains sentence pairs and a manually annotated relatendess score

You can see a quick analysis of the performance here:
https://github.com/agonopol/sent-sim/blob/master/notebooks/sick-explore.ipynb

Requirements
------------

* Download and install the wordnet corpus for lemmatization. punkt for tokenzation and stopwords english corpus:
.. code-block:: python
   import nltk
   nltk.download('wordnet', download_dir='assets')
   nltk.download('punkt', download_dir='assets')
   nltk.download('stopwords', download_dir='assets')
* Download the pre-trained word2vec model from google:
  https://drive.google.com/u/0/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM&export=download
  gunzip it into assets/word2vec/GoogleNews-vectors-negative300.bin


Install
--------

.. code-block:: shell
   pip install -f requirements.txt # to use the package as library
   python setup.py build && python setup.py install
   pip install -f requirements-dev.txt # to do more exploratory analysis with the lib
   import sentsim
   sentsim.set_assets('<PATH TO ASSETS DIR>')

