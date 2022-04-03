# Medium multiply
A small demo wrapper for a TextSynth api. To use, you need textsynth.com account to get api key. 

### Installation
```
pip install textsynthpy
```

### Get started
How to use:

```Python
from textsynthpy import TextSynth, Complete

# Initantiate a TextSynth object
con = TextSynth(API_KEY_HERE)

# text completion 
answer = con.text_complete("prompt")

# print only generated text
print(answer.text)

#print all generated results as dictionary 
print(dict(answer)) 
```

### Log probabilities
```Python
from textsynthpy import TextSynth, Log

con = TextSynth(API_KEY_HERE)

answer = con.log_prob("continuation", "optional prompt")

# print all results as dictionary 
print(dict(answer)) 
```
