

def multi_lstrip(src, trip_words):
    for ch in trip_words:
        src = src.lstrip(ch)
    return src

