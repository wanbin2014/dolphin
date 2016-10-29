from dolphin.seg_word import *


seg = seg_word()

def test_seg_word_init():

    res = seg.simple_seg("尽管之前发生了一些事故")
    assert(len(res) == 5)

    res = seg.simple_seg("学习习近平纪念长征胜利讲话")
    assert(len(res) == 6)

    res = seg.complex_seg("吉林省长春药店")
    assert(res[1] == '长春')

    res = seg.complex_seg("代表北大的人大代表，代表人大的北大博士")
    assert(res[1] == '北大' and res[3] == '人大代表' and res[6] == '北大')
    res = seg.complex_seg("咬死猎人的狗")
    assert(res[2] == '猎人')
    res = seg.complex_seg("我到东门去买米，东门人多挤又挤")
    assert(res[2] == '东门' and res[6] == '东门')
    res = seg.complex_seg("房产的一次性交易流程")
    assert(res[2] == '一次性')
    res = seg.complex_seg("乒乓球拍卖啦！")
    assert(res[1] == '拍卖')
    res = seg.complex_seg("人大代表群体性事件")
    assert(res[0] == '人大代表')
    assert(res[1] == '群体性事件')
    res = seg.complex_seg("孩子想死妈妈了")
    assert(res[1] == '想死')
    res= seg.complex_seg("薄熙来到重庆")
    assert(res[0] == '薄熙来')
    res = seg.complex_seg("赵军坑秦兵四十万于长亭")
    assert(res[2] == '秦')





