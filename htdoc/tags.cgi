#!/usr/bin/python3
#

from defs import *

#----------------------------------------------------------#

anls.set_stop_words(dirname + "/jieba/stop_words.txt")

words = text_rank(form_field("content"))

output_json(words)
