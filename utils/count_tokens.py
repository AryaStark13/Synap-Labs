import tiktoken


def count_tokens(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string.
    Args:
        string (str): The text string to count tokens in.
        model_name (str): The name of the model to use for tokenization.
        Can be one of gpt-4, gpt-3.5-turbo, text-embedding-ada-002, Codex models, text-davinci-002, text-davinci-003, davinci
    Returns:
        int: The number of tokens in the text string.
    """
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens
