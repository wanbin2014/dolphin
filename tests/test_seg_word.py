from dolphin.seg_word import *

seg = seg_word()

def test_seg_word_init():

    res = seg.simple_seg("尽管之前发生了一些事故")
    assert(len(res) == 5)

    res = seg.simple_seg("学习习近平纪念长征胜利讲话")
    assert(len(res) == 6)

    res = seg.simple_seg("有人私信问我什么才叫天王。我的定义，你说你是天王，你就是“天王”。然后我包个活给你搞。")
    assert(len(res) > 10)

    res = seg.complex_seg("有人私信问我什么才叫天王。我的定义，你说你是天王，你就是“天王”。然后我包个活给你搞。")

    res = seg.complex_seg("吉林省长春药店")

    res = seg.complex_seg("代表北大的人大代表，代表人大的北大博士")
    res = seg.complex_seg("咬死猎人的狗")
    res = seg.complex_seg("我到东门去买米，东门人多挤又挤")
    res = seg.complex_seg("房产的一次性交易流程")
