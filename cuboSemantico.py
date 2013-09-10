#import pprint
#pp = pprint.PrettyPrinter(indent=4)
dir = {}
#variables[offsetProcedimiento] = variables.get(offsetProcedimiento,{})
#dimension de enteros
dir[0]= {}
	#dimensiones demttro de enteros
dir[0][0] = {}
		#agregamos operaciones
dir[0][0][1] = 0
dir[0][0][2] = 0
dir[0][0][4] = 0
dir[0][0][3] = 1
dir[0][0][15] =0
dir[0][0][5] = 2
dir[0][0][6] = 2
dir[0][0][7] = 2
dir[0][0][8] = 2
dir[0][0][9] = 2
dir[0][0][10] = 2
		#dimensiones demttro de enteros
dir[0][1] = {}
dir[0][1][1] = 1
dir[0][1][2] = 1
dir[0][1][4] = 1
dir[0][1][3] = 1
dir[0][1][15] =1
dir[0][1][5] = 2
dir[0][1][6] = 2
dir[0][1][7] = 2
dir[0][1][8] = 2
dir[0][1][9] = 2
dir[0][1][10] = 2

		#dimensiones demttro de enteros
dir[0][3] = {}
dir[0][3][1] = 3

#dimension de flotantes
dir[1]= {}
	#dimensiones demttro de enteros
dir[1][0] = {}
		#agregamos operaciones
dir[1][0][1] = 1
dir[1][0][2] = 1
dir[1][0][4] = 1
dir[1][0][3] = 1
dir[1][0][15] =1
dir[1][0][5] = 2
dir[1][0][6] = 2
dir[1][0][7] = 2
dir[1][0][8] = 2
dir[1][0][9] = 2
dir[1][0][10] = 2
		#dimensiones dentro de flotantes
dir[1][1] = {}
			#agregamos operaciones
dir[1][1][2] = 1
dir[1][1][1] = 1
dir[1][1][4] = 1
dir[1][1][3] = 1
dir[1][1][15] =1
dir[1][1][5] = 2
dir[1][1][6] = 2
dir[1][1][7] = 2
dir[1][1][8] = 2
dir[1][1][9] = 2
dir[1][1][10] = 2

		#dimensiones dentro de flotantes
dir[1][3] = {}
dir[1][3][1] = 3

#dimension de booleanos
dir[2]= {}
dir[2][2]= {}
dir[2][2][11] = 2
dir[2][2][12] = 2

#dimension de strings
dir[3]= {}
dir[3][0]= {}
dir[3][1]= {}
dir[3][3]= {}
dir[3][0][1]=3
dir[3][1][1]=3
dir[3][3][1]=3
dir[3][3][9]=2
dir[3][3][10]=2

#casos con vacios
dir[0][9]= {}
dir[1][9]= {}
dir[2][9]= {}
dir[0][9][14]=0
dir[1][9][14]=1
dir[2][9][13]=2
dir[2][9][14]=2


# for x in range(0, 3):
	# for y in range(0, 9):
		# print("\n")
		# for z in range(0, 15):
			# try:
			  # print("X:", x, " Y:", y, " Z:", z, "\n", dir[x][y][z])
			  #print(dir[x][y][z], " ")
			# except KeyError:
			  # print()
#pp.pprint(dir)
