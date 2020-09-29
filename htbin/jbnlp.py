import os

import jieba
import jieba.posseg as pseg
import jieba.analyse as anls

dirname = os.path.dirname(os.path.abspath(__file__))


class Jbnlp():

    def __init__(self):
        jieba.initialize()
        jieba.load_userdict(dirname + "/jieba/dict_deny.txt")
        jieba.load_userdict(dirname + "/jieba/dict_user.txt")
        anls.set_stop_words(dirname + "/jieba/stop_words.txt")

    def text_rank(self, text, topK=7):
        return anls.textrank(text, topK)

    def pseg_cut(self, text, filter=[]):
        result = {}
        for word, flag in pseg.cut(text):
            if len(filter) == 0 or flag in filter:
                result[word] = flag
        return result
