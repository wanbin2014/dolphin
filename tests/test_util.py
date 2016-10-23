import pytest
from dolphin.mmseg.util import split_by_punctuation



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




