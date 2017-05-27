#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import os
import re
############################
#File Name: segment.py
#Author: weitao
#Mail: weitao@meituan.com
#Created Time: 2017-05-20 12:38:33
#Description:
############################

from pynlpir import nlpir
nlpir.Init(nlpir.PACKAGE_DIR, nlpir.UTF8_CODE,None)
nlpir.SetPOSmap(nlpir.ICT_POS_MAP_FIRST)

#pynlpir.SetPOSmap(pos_map)
#pynlpir.pos_map
#sys.exit()

for line in sys.stdin:
    content=line.strip().split(",",1)[1]
    label=line.strip().split(",")[0]
    items=nlpir.ParagraphProcess(line.strip(),1)
    print label+","+items
