class cuadruplo:
	def __init__(self, op, opd1, opd2, res):
		self.op = op
		self.opd1 = opd1
		self.opd2 = opd2
		self.res = res
		
	def printME(self):
		print (self.op, " ", self.opd1, " ", self.opd2, " ", self.res)