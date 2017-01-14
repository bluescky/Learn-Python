# -*- coding: utf-8 -*-
'''
函数注意事项
函数定义后记得加冒号
函数内容记得缩进
'''
# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes on argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# this one takse no arguments
def print_none():
	print "I got nothin'."

	
print_two("Han", "Xin")
print_two_again("Han", "Xin")
print_one("First!")
print_none()