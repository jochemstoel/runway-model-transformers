import runway
from runway.data_types import number, text, image
from transformers_model import TransformersModel
from multiprocessing import Process, freeze_support

# No options needed for this model.
setup_options = {

}

#
@runway.setup(options=setup_options)
def setup(opts):
    model = TransformersModel(opts)
    return model

# Query a text with a question
@runway.command(name='query',
                inputs={ 'document': text(), 'question': text() },
                outputs={ 'answer': text(), 'score': number(), 'start': number(), 'end': number() },
                description='Ask a question about a text.')
# 
def query(model, args):
    answer = model.query(args['document'], args['question'])
    return answer

# Sentiment analysis
@runway.command(name='sentiment',
                inputs={ 'document': text() },
                outputs={ 'label': text(), 'score': number() },
                description='Meassure the sentiment of a text.')
#
def sentiment(model, args):
    answer = model.sentiment(args['document'])
    return answer

# Freeze support is required by transformers, unsure why.
if __name__ == '__main__':
    freeze_support()
    runway.run(host='0.0.0.0', port=8000)