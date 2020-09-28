#!/usr/bin/python3
#

import os, cgi, json

import jieba
import jieba.posseg as pseg
import jieba.analyse as anls

dirname = os.path.dirname(os.path.abspath(__file__))

#----------------------------------------------------------#

def form_field(name):
    return cgi.FieldStorage().getvalue(name)

def output_json(output):
    print("content-type:application/json\r\n")
    print(json.dumps(output, ensure_ascii=False))

def text_rank(text, topK = 7):
    return anls.textrank(text, topK)

def pseg_cut(text, filter = []):
    result = {}
    for word, flag in pseg.cut(text):
        if len(filter) == 0 or flag in filter:
            result[word] = flag
    return result;
