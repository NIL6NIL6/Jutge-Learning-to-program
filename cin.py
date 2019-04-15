#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import queue


class StringIO:
	s = ""
	
	def set(self, newString):
		self.s = newString

	def get(self):
		return self.s


def cin(var):
	try:
		if not q.empty():
			var.set(q.get())
		else:
			while q.empty():
				for x in input().split():
					q.put(x)
			var.set(q.get())
		return True
	except EOFError:
		return False


def main():
	s = StringIO()
	while cin(s):
		print(s.get())


q = queue.Queue()
main()
