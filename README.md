# Text to speech

A simple Python command line tool to generate speech as mp3 file from text provided as a txt file.

## Setup environment

```
$ python3.12 -m venv .venv
$ source .venv/bin/activate
(venv) $ pip install -r requirements.txt
```


## Example usage

```
(venv) $ python text_to_speech.py -i data_examples/ibiza_en.txt -o output/ibiza_en.mp3 -l en
(venv) $ python text_to_speech.py -i data_examples/ibiza_es.txt -o output/ibiza_es.mp3 -l es
```
