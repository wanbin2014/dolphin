from dolphin.mmseg.complex import get_three_word_chunk,largest_avg_word_len,smallest_var_word_length,largest_sum_freq_one_word,complex_seg
from dolphin.mmseg.simple import build_trier,search_trier_all

def test_get_three_word_chunk():
    trier = build_trier("tests/dict.txt")
    all_chunks = search_trier_all(trier,"国际化")
    assert len(all_chunks) == 3

    all_chunks = get_three_word_chunk(trier,"国际化")
    assert len(all_chunks) == 3

    all_chunks = get_three_word_chunk(trier,"一次性交易流程")




def test_largest_avg_word_len():
    trier = build_trier("tests/dict.txt")
    all_chunks = get_three_word_chunk(trier,"国际化")
    largest_avg_chunk = largest_avg_word_len(all_chunks)
    assert len(largest_avg_chunk) == 1

    all_chunks = get_three_word_chunk(trier,"一次性交易流程")
    largest_avg_chunk = largest_avg_word_len(all_chunks)


def test_smallest_var_word_length():
    trier = build_trier("tests/dict.txt")
    all_chunks = get_three_word_chunk(trier,"研究生命起源")
    assert len(all_chunks) == 2

    largest_avg_chunk = largest_avg_word_len(all_chunks)
    assert len(largest_avg_chunk) == 2

    smallest_var_chunk = smallest_var_word_length(all_chunks)
    assert len(smallest_var_chunk) == 1
    assert smallest_var_chunk[0][0] == ['研','究']
    assert smallest_var_chunk[0][1] == ['生','命']
    assert smallest_var_chunk[0][2] == ['起','源']

def test_largest_sum_freq_one_word():
    freq_dict = {"是":100,"主":10}
    trier = build_trier("tests/dict.txt")
    all_chunks = get_three_word_chunk(trier,"主要是因为")
    assert len(all_chunks) == 2
    largest_avg_chunk = largest_avg_word_len(all_chunks)
    assert len(largest_avg_chunk) == 2
    smallest_var_chunk = smallest_var_word_length(all_chunks)
    assert len(smallest_var_chunk) == 2
    largest_sum_freq = largest_sum_freq_one_word(freq_dict,dict(),all_chunks)
    assert largest_sum_freq[0] == ["主","要"]
    assert largest_sum_freq[1] == "是"
    assert largest_sum_freq[2] == ["因","为"]











