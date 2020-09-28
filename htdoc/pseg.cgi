#!/usr/bin/python3
#

from defs import *

#----------------------------------------------------------#

jieba.load_userdict(dirname + "/jieba/dict_user.txt")

words = pseg_cut(form_field("content"))

output_json(words)
