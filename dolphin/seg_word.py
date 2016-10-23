from dolphin.mmseg.simple import build_trier,get_first_max_len
from dolphin.mmseg.util import *
import os

class seg_word:
    def __init__(self):
        cur_path = os.path.abspath(__file__)
        dir_path = os.path.dirname(cur_path)
        dict_path = (dir_path + "/dict")
        dirs = os.listdir(dict_path)
        self.trier = dict()
        for dir in dirs:
            if os.path.isdir(dict_path + "/" + dir):
                sub_dirs = os.listdir(dict_path + "/" + dir)
                for sub_dir in sub_dirs:
                    self.trier = build_trier(dict_path + "/" + dir + "/" + sub_dir,self.trier)

    def add_dict(self,filename):
        self.trier = build_trier(filename,self.trier)

    def simple_seg(self,context):
        res = list()

        words = get_first_max_len(self.trier,context)
        print(words)
        res.append(words)
        while words:
            new_sentence = multi_lstrip(context,words)

            words = get_first_max_len(self.trier,new_sentence)
            print(words)
            context = new_sentence
            if words:
                res.append(words)
        return res




    def complex_seg(self,context):
        pass