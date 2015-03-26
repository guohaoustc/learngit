# -*- coding: utf-8 -*-

import threading
import time

loops = [4,2]

class ThreadFun():
	def __init__(self, fun, args):
		self.fun = fun
		self.args = args
	
	def __call__(self):
		self.fun(*self.args)
		



def loop(nloop, nsec):
	print ' ----- start loop', nloop, 'at:',  time.ctime()
	time.sleep(nsec)
	print ' +++++ end loop', nloop, 'at:',  time.ctime()



def main():
	print 'main start, at:', time.ctime()
	threads = []
	nloops = range(2)
	
	for i in nloops:
		t = threading.Thread(target=ThreadFun(loop, args=(i, loops[i])) )
		threads.append(t)
	
	for i in nloops:
		print 'active count:', threading.activeCount()
		threads[i].start()
		time.sleep(0.1)
	print 'active count:', threading.activeCount()
	
	for i in nloops:
		threads[i].join()
		
	print 'All Donw at:', time.ctime()

if __name__ == '__main__':
	main()
