import math
from dolphin.mmseg.simple import search_trier_all,get_first_max_len
from dolphin.mmseg.util import *

def get_three_word_chunk(trier,sentence):
    first_chs_all = search_trier_all(trier,sentence)
    all_chunk = list()

    for chs in first_chs_all:
        chunk = list()
        chunk.append(chs)
        after_first_lstrip_sentence = multi_lstrip(sentence,chs)
        if after_first_lstrip_sentence == "":
            all_chunk.append(chunk)
            continue
        second_chs = get_first_max_len(trier,after_first_lstrip_sentence)

        chunk.append(second_chs)
        after_second_lstrip_sentence = multi_lstrip(after_first_lstrip_sentence,second_chs)
        if after_second_lstrip_sentence == "":
            all_chunk.append(chunk)
            continue
        third_chs = get_first_max_len(trier,after_second_lstrip_sentence)
        chunk.append(third_chs)
        all_chunk.append(chunk)

    max_len_chunks = list()
    max_len = 0
    len_chunks = list()
    for chunk in all_chunk:
        len_chunk = 0
        for word in chunk:
            len_chunk += len(word)
        if len_chunk > max_len:
            max_len = len_chunk
        len_chunks.append(len_chunk)

    i = 0
    for len_chunk in len_chunks:
        if len_chunk == max_len:
            max_len_chunks.append(all_chunk[i])
        i += 1

    return max_len_chunks
'''
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

'''

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


def smallest_var_word_length(chunks):
    len_chunk_all = list()
    avg_len_chunk_all = list()
    count_len_chunk_all = list()
    for chunk in chunks:
        len_chunk = list()
        sum = 0
        count = 0
        for word in chunk:
            len_chunk.append(len(word))
            sum += len(word)
            count += 1
        avg_len_chunk_all.append(float(sum)/count)
        len_chunk_all.append(len_chunk)

    i = 0
    var_chunk_all = list()
    min_var = 10000
    for len_chunk in len_chunk_all:
        var = 0
        for len_val in len_chunk:
            var += math.pow((len_val - avg_len_chunk_all[i]),2)
        if var <= min_var:
            min_var = var
        var_chunk_all.append(var)
        i += 1

    max_var_chunks = list()
    i = 0
    for var in var_chunk_all:
        if var == min_var:
            max_var_chunks.append(chunks[i])
        i += 1

    return max_var_chunks


def largest_low_freq_one_word(freq_dcit,chunks):
    largest_low = 0
    largest_low_pos = 0
    i = 0
    for chunk in chunks:
        low = 10000
        for word in chunk:

            if ''.join(word) in freq_dcit:
                if freq_dcit[''.join(word)] < low:
                    low = freq_dcit[''.join(word)]


        if low != 10000 and low > largest_low:
            largest_low = low
            largest_low_pos = i
        i += 1

    return chunks[largest_low_pos]



def largest_sum_freq_one_word(freq_dict,chunks):
    largest_sum_log_freq = 0.0
    largest_sum_log_freq_pos = 0
    i = 0
    for chunk in chunks:
        for word in chunk:
            freq = 0
            if len(word) == 1:
                if word in freq_dict:
                    freq += freq_dict[word]
        if freq > 0:
            log_freq = math.log(freq)
        else:
            log_freq = 0
        if largest_sum_log_freq < log_freq:
            largest_sum_log_freq = log_freq
            largest_sum_log_freq_pos = i
        i += 1

    if largest_sum_log_freq == 0.0:
        return largest_low_freq_one_word(freq_dict,chunks)
    return chunks[largest_sum_log_freq_pos]


def complex_seg(trier,freq_dict,sentence):
    if not sentence:
        return None
    chunks = get_three_word_chunk(trier,sentence)
    if len(chunks) > 1:
        largest_avg_chunks = largest_avg_word_len(chunks)
        if len(largest_avg_chunks) > 1:
            smallest_var_word_chunks = smallest_var_word_length(largest_avg_chunks)
            print("smallest_var_word_chunks:")
            print(smallest_var_word_chunks)
            if len(smallest_var_word_chunks) > 1:
                largest_sum_freq_chunk = largest_sum_freq_one_word(freq_dict,smallest_var_word_chunks)
                print("largest_sum_freq_chunk:")
                print(largest_sum_freq_chunk)
                words = ''.join(largest_sum_freq_chunk[0])
            else:
                words = ''.join(smallest_var_word_chunks[0][0])

        else:
            words = ''.join(largest_avg_chunks[0][0])
    else:
        words = ''.join(chunks[0][0])
    return words



