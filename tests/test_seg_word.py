from dolphin.seg_word import *

seg = seg_word()

def test_seg_word_init():

    res = seg.simple_seg("尽管之前发生了一些事故")
    assert(len(res) == 5)

    res = seg.simple_seg("学习习近平纪念长征胜利讲话")

