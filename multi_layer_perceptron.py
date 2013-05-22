#!/usr/bin/env python

import sys
try:
	import numpy as np
except ImportError:
	print 'check installed modules'
	print 'program require: numpy'
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
	def predict(self, input):
		return np.dot(self._weights, self.add_bias(input))

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

def main():
	print 'Multi layer perceptron'
	nn = NeuroNet((2, 2, 1))
	#nn.printnn()
	print 'nn predict = ', nn.predict( np.array([[0.], [0.]]) )

if __name__ == '__main__':
	main()
