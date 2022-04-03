from requests import post
from .answer import Complete, Log

class TextSynth():
	"""
	An connector for textsynth.com
	
	:param key: Textsynth API key. You need textsynth.com account to get this.
	:type key: str
	
	:param engine: Textsynth engine to use. It is optional parameter, in default uses "gptj_6B". Aviable engines are on 'https://textsynth.com/documentation.html'
	:param engine: str
	"""
	def __init__(self, key: str, engine = None):
		self.key = key
		if isinstance(engine, str):
			self.engine = engine
		else:
			self.engine = "gptj_6B"
		self.answer = {}
		print(f"Chosen engine: {self.engine}")
	
	def _check(self, max_tokens):
		if self.engine == "gptj_6B":
			max = 2048
		else:
			max = 1024
		if max_tokens > max:
			raise ValueError(f"max_tokens can't be higher than {max} for used engine")
	
	def text_complete(
		self,
		prompt: str,
		max_tokens: int = 100,
		temperature: float = 1,
		top_k: int = 40,
		top_p: float = 0.9,
		stop: str = None,
		together = False
	):
			"""
			Returns Answer object of completed text by given prompt.
			
			:param prompt: The input text to complete.
			:type prompt: str
			
			:param max_tokens: Optional (Default = 100). Maximum number of tokens to generate. A token represents about 4 characters for English texts. The total number of tokens (prompt + generated text) cannot exceed the model's maximum context length. It is of 2048 for GPT-J and 1024 for the other models. If the prompt length is larger than the model's maximum context length, the beginning of the prompt is discarded.
			:type max_tokens: int
			
			:param temperature: Optional (Default = 1). Sampling temperature. A higher temperature means the model will select less common tokens leading to a larger diversity but potentially less relevant output. It is usually better to tune top_p or top_k.
			:type temperature: int
			
			:param top_k: optional (Range: 1 to 1000, Default = 40). Select the next output token among the top_k most likely ones. A higher top_k gives more diversity but a potentially less relevant output.
			:type top_k: int
			
			:param top_p: optional (Range: 0 to 1, Default = 0.9). Select the next output token among the most probable ones so that their cumulative probability is larger than top_p. A higher top_p gives more diversity, but a potentially less relevant output.
			:type top_p: float
			
			:param stop: (Default = None). Stop the generation when the string(s) are encountered. The generated text does not contain the string. stream must be set to false when this feature is used. The length of the array is at most 5.
			:type stop: str
			
			:param together: Optional (Default = False). If true, saves prompt AND generated text, otherwhise saves only generated text
			:type together: bool
			"""
			self._check(max_tokens)
			
			data = {"prompt": prompt, "max_tokens": max_tokens, "temperature": temperature, "top_k": top_k, "top_p": top_p, "stream": False, "stop": stop}
			headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.key}"}
			
			answer = (post(f"https://api.textsynth.com/v1/engines/{self.engine}/completions", json = data, headers = headers)).json()
			if together:
				answer["text"] = prompt + answer["text"]
			return Complete(answer["text"], answer["reached_end"], answer["input_tokens"], answer["output_tokens"])
		
	def log_prob(continuation: str, context: str = ""):
		"""
		This endpoint returns the logarithm of the probability that a continuation is generated after a context. It can be used to answer questions when only a few answers (such as yes/no) are possible. It can also be used to benchmark the models. 
			
		:param continuation: Must be a non empty string.
		:type continuation: str
			
		:param context: If empty string, the context is set to the End-Of-Text token.
		:type context: str
		"""
			
		data = {"context": context, "continuation": continuation}
		headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.key}"}
		answer = (post(f"https://api.textsynth.com/v1/engines/{self.engine}/logprob", json = data, headers = headers)).json()
		return Log(answer["logprob"], answer["is_greedy"], answer["input_tokens"])