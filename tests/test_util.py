import pytest
from dolphin.mmseg.util import split_by_punctuation,get_chinese_word,strip_stop_word



def test_split_by_punctuation():
    res = split_by_punctuation("今天天气真好!")
    assert(res[0] == "今天天气真好")
    assert(len(res) == 1)

    res = split_by_punctuation("今天天气好，我要出去走走。")
    assert(res[0] == "今天天气好")
    assert(res[1] == "我要出去走走")
    assert(len(res) == 2)

    res = split_by_punctuation("今天天气very good，我要出去走走。")
    assert(res[0] == "今天天气")
    assert(res[1] == "我要出去走走")
    assert(len(res) == 2)

    res = get_chinese_word("尽管之前发生了一些事故")
    assert(res[0] == "尽管之前发生了一些事故")

    res = get_chinese_word("代表北大的人大代表，代表人大的北大博士")
    assert(res[1] == "代表人大的北大博士")

    res = strip_stop_word("代表北大的人大代表，代表人大的北大博士")
    print(res)




