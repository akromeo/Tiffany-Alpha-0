import tiktoken

TIK_GPT2_ENCODER = tiktoken.get_encoding("gpt2")

def encode(data):
    return TIK_GPT2_ENCODER.encode_ordinary(data)

def decode(data):
    return TIK_GPT2_ENCODER.decode(data)

def get_tiktoken_vocab_count():
    return TIK_GPT2_ENCODER.n_vocab