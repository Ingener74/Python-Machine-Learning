#!/usr/bin/env python

import sys
try:
	import numpy as np
	import cPickle as pk
	from optparse import OptionParser
	import sys
except ImportError:
	print 'i need numpy, cPickle'
	print 'install it'
	sys.exit(1)

class Layer:
	def __init__(self, inputs, neurons):
		self._neurons = neurons
		self._inputs = inputs + 1
		self._weights = np.random.rand(self._neurons, self._inputs)
	def printl(self):
		print 'neurons = ', self._neurons, ', inputs = ', self._inputs
		print 'weights:\n', self._weights
	def add_bias(self, input):
		x = np.resize(input, (input.shape[0] + 1, input.shape[1]))
		x[input.shape[0], input.shape[1] - 1] = 1.0
		return x
	def transfer_function(self, input):
		return 1.0 / ( 1 + np.exp(-1.0 * input) )
	def predict(self, input):
		return self.transfer_function( np.dot(self._weights, self.add_bias(input)) )

class NeuroNet:
	def __init__(self, configuration):
		self.conf = configuration
		self.layers = []
		for n in range(0, len(self.conf) - 1):
			self.layers.append(Layer(self.conf[n], self.conf[n + 1]))
	def printnn(self):
		print 'NeuroNet configuration = ', self.conf
		for x in self.layers:
			x.printl()
	def predict(self, input):
		for x in self.layers:
			if x == self.layers[0]:
				y = x.predict(input)
			else:
				y = x.predict(y)
		return y

class NeuroNetIO:
	def __init__(self, filename):
		self.fn = filename
	def save(self, nn):
		self.file = open(self.fn, 'w')
		pk.dump(nn, self.file)
		self.file.close()
	def load(self):
		self.file = open(self.fn, 'r')
		x = pk.load(self.file)
		self.file.close()
		return x
		

def main():
	print 'Multi layer perceptron'
	parser = OptionParser(usage="Usage: ./mlp <options>")
	parser.add_option("-m", "--mode", type="int", default="0", help="working mode", dest="mode")
	(options, args) = parser.parse_args()

	nnio = NeuroNetIO('nn.dat')

	if options.mode == 0:
		print 'load and use NeuroNet'

	elif options.mode == 1:
		print 'create and save NeuroNet'
		nn = NeuroNet((2, 2, 1))
		nnio.save(nn)

	else:
		parser.print_help()
		sys.exit()

if __name__ == '__main__':
	main()
