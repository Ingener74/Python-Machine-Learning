#!/usr/bin/env python

import numpy as np

class Layer:
	def __init__(self, inputs, neurons):
		self._neurons = neurons
		self._inputs = inputs + 1
		self._weights = np.random.rand(self._neurons, self._inputs)
		print "w = \n", self._weights.type
	def printl(self):
		print 'neurons = ', self._neurons, ', inputs = ', self._inputs
		print 'weights:\n', self._weights
	def predict(self, input):
		print "predict input = \n", input		
		input_t = input
		input_t
		print "predict input_t = \n", input_t 
		#return np.dot(self._weights, input)
		pass

def main():
	print 'Multi layer perceptron'
	l1 = Layer(2, 2)
	l2 = Layer(2, 1)
	l1.printl()
	l2.printl()
	
	print 'output l1 = ', l1.predict(np.array([[1],[0]], 'double'))
	pass

if __name__ == '__main__':
	main()
