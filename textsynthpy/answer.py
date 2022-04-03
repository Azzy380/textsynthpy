class Complete():
	"""
	Object handles response form TextSynth.text_complete().
	
	:param text: generated text
	:type text: str
	
	:param reached_end:
	:type reached_end: bool
	
	:param truncated_prompt: If true, indicate that it is the last answer. It is only useful in case of streaming output (stream = true in the request).
	:type truncated_prompt: bool
	
	:param input_tokens:
	:type input_tokens: int
	
	:param output_tokens: 
	:type output_tokens: int
	"""
	def __init__(self, text: str, reached_end: bool, input_tokens: int, output_tokens: int):
		self.text = text
		self.reached_end = reached_end
		self.input_tokens = input_tokens
		self.output_tokens = output_tokens
		
	def __iter__(self):
		yield "text", self.text
		yield "reached_end", self.reached_end
		yield "input_tokens", self.input_tokens
		yield "output_tokens", self.output_tokens
class Log():
	"""
	Object handles response form TextSynth.log_prob()
	
	:param logprob: Logarithm of the probability of generation of continuation preceeded by context. It is always <= 0.
	:type logprob: float
	
	:param is_greedy: true if continuation would be generated by greedy sampling from continuation.
	:type is_greedy: bool
	
	:param input_tokens: Indicate the total number of input tokens. It is useful to estimate the number of compute resources used by the request.
	:type input_tokens: int
	"""
	def __init__(
		self,
		logprob: float,
		is_greedy: bool,
		input_tokens: int
	):
		self.logprob = logprob
		self.is_greedy = is_greedy
		self.input_tokens = input_tokens
	
	def __iter__(self):
		yield "logprob", self.logprob
		yield "is_greedy", self.is_greedy
		yield "input_tokens", self.input_tokens