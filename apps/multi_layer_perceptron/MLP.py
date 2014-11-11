#!/usr/bin/env python

import sys, os
try:
	import numpy as np
	import cPickle as pk
	from optparse import OptionParser
	from PySide.QtGui import QApplication, QWidget
	
	from main import Ui_MainWidget
	
except ImportError as e:
	raise SystemExit(str(e))

class MainWidget(QWidget, Ui_MainWidget):
	def __init__(self, parent=None):
		super(MainWidget, self).__init__(parent)
		self.setupUi(self)

class Layer(object):
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
		return 1.0 / ( 1.0 + np.exp(-1.0 * input) )
	def predict(self, input):
		return self.transfer_function( np.dot(self._weights, self.add_bias(input)) )

class NeuroNet(object):
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

class NeuroNetIO(object):
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

class TermCriteria(object):
	""" Termination criteria class for NeuroNet Trainers """
	CRIT_ERROR = 0
	CRIT_ITER  = 1
	def __init__(self, criteria, maxIteration, desiredError):
		self.criteria = criteria
		self.maxIteration = maxIteration
		self.desiredError = desiredError
		if self.criteria == self.CRIT_ERROR:
			print 'desired error criteria, with error = ', self.desiredError
		elif self.criteria == self.CRIT_ITER:
			print 'max iteration criteria, with max iteration = ', self.maxIteration
		else:
			print 'unknown criteria'

class BackPropTrainer(object):
	def __init__(self, learning_rate):
		self._learning_rate = learning_rate
		print 'BackProp trainer'
		print 'Leaning rate = ', self._learning_rate

	def train(self, nn, termCrit, train_inputs, train_desired_outputs):
		print 'BackProp Trainer.train'
		print 'train inputs = \n', train_inputs
		print 'train desired outputs = \n', train_desired_outputs
		print 'train inputs shape = \n', train_inputs.shape
		if(train_inputs.shape[1] != train_desired_outputs.shape[1]):
			print 'error train sequence not match'
			return
		mse = 0.0
		for i in range(0, train_inputs.shape[1]):
			#
			# W[i + 1] = W[i] + learning_rate * error *  * input
			#
			#
			#
			#
			dW     = []
			inputs = []
			errors = []

			

			print 'i = ', i
		pass
		
def mode_0():
	print 'load and use NeuroNet'

def mode_1():
	print 'create, train and save NeuroNet'
	nn = NeuroNet((2, 5, 5, 1))
	print 'NeuroNet before training'
	nn.printnn()
	
	train_inputs = np.array([
		[0, 1, 0, 1],
		[0, 0, 1, 1],
		])
	train_desired_outputs = np.array([
		[0, 1, 1, 0],
		])
	#print 'train inputs = \n', train_inputs
	#print 'train desired outputs = \n', train_desired_outputs
	sys.stdout.write('train NeuroNet... ')
	bpt = BackPropTrainer(0.2)
	bpt.train(nn, TermCriteria(TermCriteria.CRIT_ERROR, 1000, 0.001), train_inputs, train_desired_outputs)
	print 'done'
	
	sys.stdout.write('save NeuroNet...')
	nnio = NeuroNetIO('nn.dat')
	nnio.save(nn)
	print 'done'

def mode_2():
	test = (1, 'test', np.array([0, 1]))
	print 'test = ', test
	print 'test shape = ', len(test)
	for i in range(0, len(test)):
		print test[i]
	print 'for future'

def mode_3():
	print 'for future'

def main():
# 	os.system('clear')
# 	print '================================================================================'
# 	print '==========================   Multi layer perceptron   =========================='
# 	print '================================================================================'
# 	parser = OptionParser(usage="Usage: ./mlp <options>")
# 	parser.add_option("-m", "--mode", type="int", default="0", help="working mode", dest="mode")
# 	(options, args) = parser.parse_args()
# 
# 	nnio = NeuroNetIO('nn.dat')
# 
# 	if options.mode == 0:
# 		mode_0()
# 	elif options.mode == 1:
# 		mode_1()
# 	elif options.mode == 2:
# 		mode_2()
# 	elif options.mode == 3:
# 		mode_3()
# 	else:
# 		parser.print_help()
# 		sys.exit()

	app = QApplication(sys.argv)
	
	mainWindow = MainWidget()
	mainWindow.show()

	return sys.exit(app.exec_())

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print str(e)






