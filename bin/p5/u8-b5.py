# -*- coding: utf-8 *-*

import os, codecs, sys

#################################################
# 處理單檔
#################################################
def trans_file(fn1, fn2):
	f1=open(fn1, "r", encoding="utf-8")
	f2=open(fn2, "w", encoding="cp950", errors='cbeta')
	for line in f1:
		f2.write(line)
	f1.close()
	f2.close()


#################################################
# 處理無法直接由 utf8 轉 big5 的文字
#################################################
def my_err_handler(exc):
	c = exc.object[exc.start:exc.end]
	try:
		r = c.encode('cp950')
		r = ''
	except:
		i = ord(c)
		r = "&#x%04X;" % i
	return (r, exc.end)

#################################################
# main 主程式
#################################################
codecs.register_error('cbeta', my_err_handler) 	# 先登記遇到缺字時的 error handler
trans_file('input.txt', 'outout.txt')