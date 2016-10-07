import pytest
from dolphin.mmseg.simple import build_trier,search_trier_all,get_first_max_len
from dolphin.mmseg.util import *


def test_build_trier():
    root = build_trier("tests/dict.txt")
    assert "中" in root
    assert "国" in root["中"]
    assert "人" in root["中"]["国"]
    assert b'\1' in root["中"]["国"]
    assert b'\1' in root["中"]["国"]["人"]
    assert b'\1' not in root["中"]
    assert not b'\1' in root["中"]
    assert len(root["中"]) == 1

def test_search_trier_all():
    trier = build_trier("tests/dict.txt")
    all_first_words = search_trier_all(trier,"中国人")
    assert len(all_first_words) == 3
    all_first_words = search_trier_all(trier,"中国家")
    assert len(all_first_words) == 2


def test_get_first_max_len():
    trier = build_trier("tests/dict.txt")
    sentence = "我是中国人"
    first_words = get_first_max_len(trier,sentence)
    assert len(first_words) == 1
    assert first_words[0] == "我"
    new_sentence = multi_lstrip(sentence,first_words)
    second_words = get_first_max_len(trier,new_sentence)
    assert second_words[0] == "是"
    new_new_sentence = multi_lstrip(new_sentence,second_words)
    third_words = get_first_max_len(trier,new_new_sentence)
    assert len(third_words) == 3
    assert third_words[0] == "中"
    assert third_words[2] == "人"




