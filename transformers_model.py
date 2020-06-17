from transformers import pipeline
import sys

class TransformersModel():

    def __init__(self, options):
        options = options # I don't know how to put nothing here.

    # Ask a question about a given text.
    def query(self, document, question):
        nlp = pipeline('question-answering')
        return nlp({
            'question': question,
            'context': document
        })
    
    # Measure sentiment of a given text.
    def sentiment(self, document):
        nlp = pipeline('sentiment-analysis')
        return nlp(document)[0]
