#!/usr/bin/python3
#

from defs import *

#----------------------------------------------------------#

jieba.load_userdict(dirname + "/jieba/dict_deny.txt")

words = pseg_cut(form_field("content"), ["deny"])

output_json(words)
