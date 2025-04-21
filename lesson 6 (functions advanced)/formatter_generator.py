def formatter_generator(formats):
    def format(message):
        words = []
        for i, word in enumerate(message.split(' ')):
            words.append(formats[i % len(formats)](word))
        return ' '.join(words)
    return format

def alternating(message):
    msg = ""
    for i, l in enumerate(message):
        msg += l.upper() if i%2==0 else l.lower()
    return msg

format = formatter_generator([lambda m: m.upper(), lambda m: '-'.join(list(m)), alternating])
print(format("hello! my name is andre"))