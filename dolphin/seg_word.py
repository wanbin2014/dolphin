from dolphin.mmseg.simple import build_trier,get_first_max_len
from dolphin.mmseg.complex import *
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

        freq_path = dir_path + "/word_freq"
        dirs = os.listdir(freq_path)
        for dir in dirs:
            self.trier = build_trier(freq_path + "/" + dir,self.trier)
            self.freq_dict = self.build_freq_dict(freq_path + "/" + dir)

        single_word_freq_path = dir_path + "/single_word_freq"
        dirs = os.listdir(single_word_freq_path)
        for dir in dirs:
            self.single_word_freq_dict = self.build_single_word_freq_dict(single_word_freq_path + "/" + dir)


    def build_freq_dict(self,filename):
        freq_dict = dict()
        fp = open(filename)
        for line in fp:
            try:
                fields = line.split(" ")
                if len(fields) >= 2:
                    freq_dict[fields[0]] = int(fields[1])
            except Exception :
                continue
        fp.close()
        return freq_dict

    def build_single_word_freq_dict(self,filename):
        freq_dict = dict()
        fp = open(filename)
        for line in fp:
            try:
                fields = line.split("\t")
                if len(fields) >= 5:
                    freq_dict[fields[1]] = int(fields[2])
            except Exception:
                continue
        fp.close()
        return freq_dict




    def add_dict(self,filename):
        self.trier = build_trier(filename,self.trier)

    def simple_seg(self,context):
        res = list()
        sentences = get_chinese_word(context)
        for sentence in sentences:
            words = get_first_max_len(self.trier,sentence)
            print(words)
            res.append(words)
            while words:
                new_sentence = multi_lstrip(sentence,words)

                words = get_first_max_len(self.trier,new_sentence)
                print(words)
                sentence = new_sentence
                if words:
                    res.append(words)
        return res



    def complex_seg(self,context):
        res = list()
        sentences = get_chinese_word(context)
        print(sentences)
        for sentence in sentences:
            words = complex_seg(self.trier,self.freq_dict,self.single_word_freq_dict,sentence)

            res.append(words)

            while words:
                new_sentence = multi_lstrip(sentence,words)
                words = complex_seg(self.trier,self.freq_dict,self.single_word_freq_dict,new_sentence)
                sentence = new_sentence
                if words:
                    res.append(words)
        return res



