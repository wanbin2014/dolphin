

chinese = set(list(range(0x4E00, 0xA000)) +
              list(range(0x3400, 0x4DC0)) +
              list(range(0x20000, 0x2A6E0)) +
              list(range(0x2A700, 0x2B740)) +
              list(range(0x2B740, 0x2B820)) +
              list(range(0xF900, 0xFB00)) +
              list(range(0x2F800, 0x2FA20)) +
              list(range(0x9FA6, 0x9FCC)))



def multi_lstrip(src, trip_words):
    trip_words_str = ''.join(trip_words)
    pos = src.find(trip_words_str)
    if pos == 0:
        src = src[len(trip_words_str):]
        return src
    else:
        return src


def split_by_punctuation(sentence):

    res = list()
    s = ""
    for c in sentence:
        if ord(c) in chinese:
            s += c
            continue
        else:
            if s:
                res.append(s)
            s = ""
    return res


def get_chinese_word(sentence):
    return split_by_punctuation(sentence)


