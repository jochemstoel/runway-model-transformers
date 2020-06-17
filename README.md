# Runway Transformers Model Port

This repository contains a Runway port of the [transformers model](https://github.com/huggingface/transformers). It can be used for natural language processing and sentiment analysis.

This model has two methods.

### Query
Ask a question about a text. It will return a score (confidence), the answer, and the start/end position of the answer in the document.

* Inputs: document (string), question (string)
* Outputs: answer (string), start (number), end (number), score (float number)

```js 
fetch('http://localhost:8000/query', {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            document: 'My brother is 13 years old and he likes computer games',
            question: 'How old is my brother?'
        })
    })
    .then(response => response.json())
    .then(console.log) // { answer: '13', end: 16, score: 0.9058668142651101, start: 14 }
```

### Sentiment
Sentiment: determine sentiment of a text.

* Inputs: document (string)
* Outputs: label (string 'POSITIVE' or 'NEGATIVE'), score (float number)
```js 
fetch('http://localhost:8000/sentiment', {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            document: 'We are happy to announce to have successfully ported transformers to Runway!'
        })
    })
    .then(response => response.json())
    .then(console.log) // { label: 'POSITIVE', score: 0.9997140765190125 }
``` 

### Developer notes:
I am used to transformers needing something called _freeze_support()_. I am unaware what exactly this is but it does not work without. Somebody explain this to me.