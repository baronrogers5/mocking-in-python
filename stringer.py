def cut_it(message: str):
    if not isinstance(message, str):
        raise TypeError(f'Expected message to be type str, got: {type(message)}')

    # We will cut all messages to be of length less than or equal to 40
    if len(message) > 40:
        message.replace('!', '')
    
    if len(message) > 40:
        message = message[:40]

    return message