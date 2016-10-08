

def build_trier(filename):
    fp = open(filename)
    trier_root = dict()
    for line in fp:

        trier = trier_root
        for ch in line:
            if ch == '\n':
                trier[b'\1'] = 0  # Expressing end of word.
                continue
            if ch in trier:
                trier = trier[ch]
            else:
                trier[ch] = dict()
                trier = trier[ch]
    return trier_root

def search_trier_all(trier,sentence):
    if sentence == None or sentence == "":
        return None
    chs = list()
    all_chs = list()
    for ch in sentence:
        if ch in trier:
            trier = trier[ch]
            chs.append(ch)

            if b'\1' in trier:
                all_chs.append(chs.copy())
        else:
            break

    all_chs.append(sentence[0])
    return all_chs


def get_first_max_len(trier,sentence):
    all_chs = search_trier_all(trier,sentence)
    if all_chs == None:
        return None
    max_len = 0
    max_pos = 0
    i = 0
    for chs in all_chs:
        if len(chs) > max_len:
            max_pos = i
            max_len = len(chs)
        i += 1
    return all_chs[max_pos]




