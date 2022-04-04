 
 ​Usage 
 ​===== 
  
 ​.. ​_​installation​: 
  
 ​Installation 
 ​------------ 
  
 ​To use TextSynthPy, first install it using pip: 
  
 ​.. ​code-block​:: ​console 
  
 ​   (.venv) $ pip install textsynthpy
  
 ​Basic generation
 ​---------------- 
  
 Create a connector:
  ```con = textsynthpy.TextSynth("api_key")```​ 
  
 ​.. ​autofunction​:: ​textsynthpy.TextSynth
  
 ​The ​``key``​ parameter must be an api key received at. Otherwise, textsynth won't let you pass.
 
 Generate text by using ```text_complete()``` method:
  >>> answer = con.text_complete("prompt")
  
  ```prompt``` parameter must be a string, otherwise will receice an exception.
  
  
  Generated text is under ```text``` atrribute:
  ```answer.text```
  
 ​For example: 
  
 ​>>> ​import​ textsynthpy
 ​>>> con = textsynthpy.TextSynth("api_key")
 >>> print(answer.text)
