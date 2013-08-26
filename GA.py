#!/usr/bin/env python

import sys
try:
	from PIL import Image, ImageDraw
	import matplotlib.pyplot as plt
except:
	print 'install dependencies PIL, MatPlotLib'
	print 'sudo apt-get install python-imagine python python-matplotlib'
	sys.exit(1)

def test_Image():
	print 'test Image'
	im = Image.new("RGB", (1024, 1024))
	im.show()
	dr = ImageDraw.Draw(im)
	dr.ellipse((100, 100, 102, 102), (0, 255,0))
	del dr
	im.show()
	print 'save image'
	im.save('test.png', 'PNG')
	print 'end test Image'
	pass

def test_MatPlotLib():
	pass

def main():
	print('main')
	test_Image()
	#test_MatPlotLib()
	pass

if __name__ == '__main__':
	main()
	print('end program')
