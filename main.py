print("Python Program Running...\n")
#coverts binary to decimal. EX: bin_to_dec("1001011") = 75
def bin_to_dec(number = ""):
	#init return value to 0
	decimal_number = 0
	# 5 ** 3 = 5 to the power of  3 = 125
	
	#this if is for error checking
	if(len(number) <= 0):
		return 0;
	
	#power = the highest binary digit in decimal EX if 1001011, power = 2 ** 6
	power = 2 ** (len(number) - 1)
	
	#traverse through the binary string number
	for i in number:
		#if it is one, add power to the final decimal number. Else do not
		if(i == '1'):
			decimal_number = decimal_number + power
		
		#reduce the power by two to switch to the next digit
		power = power / 2
		
	#return the decimal number
	return decimal_number
################################################################
#	
#bin = "1001011"
#print bin, " in decimal is ", bin_to_dec(bin)
#bin = "1010"
#print bin, " in decimal is ", bin_to_dec(bin)
#bin = "10100"
#print bin, " in decimal is ", bin_to_dec(bin)
#bin = "101000"
#print bin, " in decimal is ", bin_to_dec(bin)

#open and read file

################################################################
#data structures
################################################################
opcodeStr = []  	# <type 'list'>: ['Invalid Instruction', 'ADDI', 'SW', 'Invalid Instruction', 'LW', 'BLTZ', 'SLL',...]
validStr= [] 		# <type 'list'>: ['N', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y',...]
instrSpaced = [] 	# <type 'list'>: ['0 01000 00000 00001 00000 00000 001010', '1 01000 00000 00001 00000 00000 001010',...]
arg1 = [] 			# <type 'list'>: [0, 0, 0, 0, 0, 1, 1, 10, 10, 0, 3, 4, 152, 4, 10, 1, 0, 112, 0]
arg2 = [] 			# <type 'list'>: [0, 1, 1, 0, 1, 0, 10, 3, 4, 5, 0, 5, 0, 5, 6, 1, 1, 0, 0]
arg3 = [] 			# <type 'list'>: [0, 10, 264, 0, 264, 48, 2, 172, 216, 260, 8, 6, 0, 6, 172, -1, 264, 0, 0]
arg1Str = [] 		# <type 'list'>: ['', '\tR1', '\tR1', '', '\tR1', '\tR1', '\tR10', '\tR3', '\tR4', .....]
arg2Str = [] 		# <type 'list'>: ['', ', R0', ', 264', '', ', 264', ', #48', ', R1', ', 172', ', 216', ...]
arg3Str = [] 		# <type 'list'>: ['', ', #10', '(R0)', '', '(R0)', '', ', #2', '(R10)', '(R10)', '(R0)',...]
mem = [] 			# <type 'list'>: [-1, -2, -3, 1, 2, 3, 0, 0, 5, -5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
binMem = [] 		# <type 'list'>: ['11111111111111111111111111111111', '11111111111111111111111111111110', ...]
valid = []
opcode = []
################################################################

machineCodeFile = open("test2_bin.txt")
machineCode = machineCodeFile.readlines()
machineCodeFile.close()
for i in machineCode:
	op = bin_to_dec(i[0:11])
	if(op >= 160 and op <= 191):
		opcodeStr.append("B")
		opcode.append(i[0:6])
	elif(op == 1104):
		opcodeStr.append("AND")
		opcode.append(i[0:11])
	elif(op == 1112):
		opcodeStr.append("ADD")
		opcode.append(i[0:11])
	elif(op == 1160 or op == 1161):
		opcodeStr.append("ADDI")
		opcode.append(i[0:10])
	elif(op == 1360):
		opcodeStr.append("ORR")
		opcode.append(i[0:11])
	elif(op >= 1440 and op <= 1447):
		opcodeStr.append("CBZ")
		opcode.append(i[0:8])
	elif(op >= 1448 and op <= 1455):
		opcodeStr.append("CBNZ")
		opcode.append(i[0:8])
	elif(op == 1624):
		opcodeStr.append("SUB")
		opcode.append(i[0:11])
	elif(op == 1672 and op == 1673):
		opcodeStr.append("SUBI")
		opcode.append(i[0:10])
	elif((op >= 1648 and op <= 1687) and (op != 1672 or op != 1673)):
		opcodeStr.append("MOVZ")
		opcode.append(i[0:9])
	elif(op >= 1940 and op <= 1943):
		opcodeStr.append("MOVK")
		opcode.append(i[0:9])
	elif(op == 1690):
		opcodeStr.append("LSR")
		opcode.append(i[0:11])
	elif(op == 1691):
		opcodeStr.append("LSL")
		opcode.append(i[0:11])
	elif(op == 1984):
		opcodeStr.append("STUR")
		opcode.append(i[0:11])
	elif(op == 1986):
		opcodeStr.append("LDUR")
		opcode.append(i[0:11])
	elif(op == 2038):
		opcodeStr.append("BREAK")
		opcode.append(i[0:11])
print opcodeStr
print opcode


