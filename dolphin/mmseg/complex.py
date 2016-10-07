from dolphin.mmseg.simple import search_trier_all,get_first_max_len
from dolphin.mmseg.util import *

def get_three_word_chunk(trier,sentence):
    first_chs_all = search_trier_all(trier,sentence)
    all_chunk = list()
    for chs in first_chs_all:
        chunk = list()
        chunk.append(chs)
        after_first_lstrip_sentence = multi_lstrip(sentence,chs)
        if after_first_lstrip_sentence == None:
            break
        second_chs = get_first_max_len(trier,after_first_lstrip_sentence)
        chunk.append(second_chs)
        after_second_lstrip_sentence = multi_lstrip(sentence,second_chs)
        if after_second_lstrip_sentence == None:
            break
        third_chs = get_first_max_len(trier,after_second_lstrip_sentence)
        chunk.append(third_chs)
        all_chunk.append(chunk)

    return all_chunk

def get_max_length_chunk(trier,sentence):
    all_chunk = get_three_word_chunk(trier,sentence)
    max_len = 0
    max_pos = 0
    i = 0
    for chunk in all_chunk:
        len += len(chunk[0]) if len(chunk) > 0 else 0
        len += len(chunk[1]) if len(chunk) > 1 else 0
        len += len(chunk[2]) if len(chunk) > 2 else 0
        if len > max_len:
            max_len = len
            max_pos = i
        i += 1

    return all_chunk[i]
"""

"""

def largest_avg_word_len(chunks):

    min_chunk_size = 3
    for chunk in chunks:
        if len(chunk) < min_chunk_size:
            min_chunk_size = len(chunk)
    if min_chunk_size == 3:
        return chunks

    eq_size_chunks = list()
    for chunk in chunks:
        if len(chunk) == min_chunk_size:
            eq_size_chunks.append(chunk)

    return eq_size_chunks












