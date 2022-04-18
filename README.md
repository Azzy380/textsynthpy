# TextSynthPy
A small demo wrapper for a TextSynth api. To use, you need textsynth.com account to get api key. 

### Installation
```
pip install textsynthpy
```

### Get started
How to use:

```Python
import os
from textsynthpy import TextSynth, Complete

# Load your API key from an environment variable or secret management service
key = os.getenv("TEXTSYNTH_API")

# Initantiate a TextSynth object
con = TextSynth(key))

# text completion 
answer = con.text_complete("prompt")

# print generated text
print(answer.text)
```

### Engines
```Python
# You can print engine list by using
TextSynth.engines()

# adding True as parametr will return you a dict of engines
engines = TextSynth.engines(True)
```