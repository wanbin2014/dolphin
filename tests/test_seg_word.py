from dolphin.seg_word import *

seg = seg_word()

def test_seg_word_init():

    res = seg.simple_seg("尽管之前发生了一些事故")
    assert(len(res) == 5)

    res = seg.simple_seg("学习习近平纪念长征胜利讲话")
    assert(len(res) == 6)

    res = seg.simple_seg("有人私信问我什么才叫天王。我的定义，你说你是天王，你就是“天王”。然后我包个活给你搞。")

