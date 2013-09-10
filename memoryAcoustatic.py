class memoryAcoustatic:
	def __init__(self):
		self.memoriaInt = []
		self.memoriaFloat= []
		self.memoriaBoolean= []
		self.memoriaString= []
		self.memoriaSonido= []
		self.memoriaInstrumento= []
		self.memoriaPista= []

	def initialize(self, espInt, espFloat, espBoolean, espString, espSonido, espInstrumento, espPista):
		for foo in range(espInt):
			self.memoriaInt.append(0)
		for foo in range(espFloat):
			self.memoriaFloat.append(0.0)
		for foo in range(espBoolean):
			self.memoriaBoolean.append(None)
		for foo in range(espString):
			self.memoriaString.append("")
		for foo in range(espSonido):
			self.memoriaSonido.append("")
		for foo in range(espInstrumento):
			self.memoriaInstrumento.append("")
		for foo in range(espPista):
			self.memoriaPista.append("")
	def printMem(self):
		print("self.memoriaInt", self.memoriaInt)
		print("self.memoriaFloat", self.memoriaFloat)
		print("self.memoriaBoolean", self.memoriaBoolean)
		print("self.memoriaString", self.memoriaString)


	def saveInt(self, direccion, valor):
		self.memoriaInt[direccion] =valor

	def saveFloat(self, direccion, valor):
		self.memoriaFloat[direccion] =valor
		
	def saveBoolean(self, direccion, valor):
		self.memoriaBoolean[direccion] =valor

	def saveString(self, direccion, valor):
		self.memoriaString[direccion] =valor

	def saveSound(self, direccion, valor):
		self.memoriaSonido[direccion] =valor

	def saveInstrument(self, direccion, valor):
		if(isinstance(self.memoriaInstrumento[direccion], list )):
			self.memoriaInstrumento[direccion] = []
		self.memoriaInstrumento[direccion].append(valor)

	def saveTrack(self, direccion, valor):
		self.memoriaPista[direccion] =valor
		
	#METODOS PARA PASO DE PARAMETROS 
	# def appendInt(self, direccion, valor):
		# self.memoriaInt[direccion].append(valor)

	# def appendFloat(self, direccion, valor):
		# self.memoriaFloat[direccion].append(valor)
		
	# def appendBoolean(self, direccion, valor):
		# self.memoriaBoolean[direccion].append(valor)

	# def appendString(self, direccion, valor):
		# self.memoriaString[direccion].append(valor)

	# def appendSound(self, direccion, valor):
		# self.memoriaSonido[direccion].append(valor)

	# def appendInstrument(self, direccion, valor):
		# self.memoriaInstrumento[direccion].append(valor)

	# def appendTrack(self, direccion, valor):
		# self.memoriaPista[direccion].append(valor)
		
	def getInt(self, direccion):
		return self.memoriaInt[direccion] 

	def getFloat(self, direccion):
		return self.memoriaFloat[direccion] 
		
	def getBoolean(self, direccion):
		return self.memoriaBoolean[direccion] 

	def getString(self, direccion):
		return self.memoriaString[direccion] 

	def getSound(self, direccion):
		return self.memoriaSonido[direccion] 

	def getInstrument(self, direccion):
		return self.memoriaInstrumento[direccion] 

	def getTrack(self, direccion):
		return self.memoriaPista[direccion] 