##################################################################################
#   Dissemble Class
#       Contains an instance of a text input of binary code, with each row in the
#       lists being an iteration of an instruction.  opt2 was not included in
#       instruction lists, for now.
##################################################################################
class Dissemble(object):
	def __init__(self):
		self.iFile = ''     # Holds name of input file (via command line).
		self.oFile = ''     # Holds name of output file (via command line).
		self.finalText = ''     # Holds final text to write out to file.
		self.machineCodeFile = ''     # Holds name of string of all binary data from input file.
		self.numLinesText = 0   # Holds the number of lines in binary text file.
		self.startMem = 96      # Holds beginning of memory address.
		self.rmMask = 0x1F0000  # Mask to extract Rn register (R1)
		self.rnMask = 0x3E0     # Mask to extract Rd register (R2)
		self.rdMask = 0x1F      # Mask to extract Rm register (R3)
		self.shamMask = 0xFC00  # Mask to extract shamt register.
		self.immI = 0x3FFC00    # Mask to extract immediate from I-format instruction.
		self.immIM = 0x1FFFE0   # Mask to extract immediate from IM-format instruction.
		self.addrD = 0x1FF000   # Mask to extract address from D-format instruction.
		self.addrCB = 0xFFFFE0  # Mask to extract address from CB-format instruction.
		self.addrB = 0x3FFFFFF  # Mask to extract address from B-format instruction.
		self.shiftMask = 0x600000   # Mask to extract shift.
		self.machineLines = []  # Holds RAW lines of binary text file, WITHOUT '\n' and '\t'
		self.instrSpaced = []   # Holds formatted lines of binary lines.
		# self.decEleven = []     # Holds list of first eleven bits of each line in decimal.
		self.opCodeStr = []     # Holds strings of opcodes, empty if data.
		self.isInstr = []       # Holds whether each column is instruction or data.
		self.insType = []       # Holds either: type of instruction (R, I, D, CB, IM, B, BREAK, NOP
		self.data = []          # Holds decimal value for data, empty if instruction.
		self.rmRegNum = []      # Holds register nums for Rm portion, empty if doesn't exist in instruction.
		self.shamNum = []       # Holds register nums for shamt portion, empty if doesn't exist in instruction.
		self.rnRegNum = []      # Holds register nums for Rn portion, empty if doesn't exist in instruction.
		self.rdRtRegNum = []      # Holds register nums for Rd/Rt portion, empty if doesn't exist in instruction.
		self.immNum = []        # Holds immediate value in instruction.
		self.addrNum = []       # Holds numeric address in instruction.
		self.shiftNum = []      # Holds shift in instruction.
		self.memLines = []      # Holds memory address of each line.
	##################################################################################
	#   openRead:  Opens binary text file and raw loads lines of binary code
	#   into machineCode list.
	##################################################################################
	def openRead(self):     # Opens file and reads binary lines into list.
		with open(self.iFile) as self.machineCodeFile:      # 18-20 read in lines WITHOUT tabs.
			self.machineLines = self.machineCodeFile.readlines()
		self.machineLines = [x.strip() for x in self.machineLines]
		# TESTPRINT
		# print
		# print 'Testing openRead()...' + '\niFile: ' + self.iFile
		# print 'machineCode[]: '
		# for item in self.machineLines:  # Print all raw binary lines in machineLines[].
		#     print item
		self.machineCodeFile.close()    # Clean up.
	##################################################################################
	#   processElvBits:  Takes 1st 11 bits of each line.  Tests for
	#   opcode via range.  Populates opcode string list, instruction type list,
	#   and data type list.  If line has no instruction type, then instruction type
	#   list left empty to maintain column integrity - and vice versa.
	##################################################################################
	def processElvBits(self):
		#TESTPRINT
		# print
		# print 'Testing processLinesBin()...'
		# print 'First eleven bits, binary & decimal:'
		k = self.startMem
		for line in self.machineLines:
			# Count lines
			self.numLinesText += 1
			# Populate memory.
			self.memLines.append(k)
			k += 4
			# Get the first bits in bin & dec.
			elvBin = line[0:11]
			elvDec = int(elvBin, 2)
			# TESTPRINT
			# print elvBin + '  -  '  + str(elvDec)
			# Check if each dec is recognized instruction.
			if (elvDec == 0):  # Check if nop
				if (int(line, 2) == 0):     # DOUBLE CHECK
					self.isInstr.append(True)
					self.opCodeStr.append("NOP")
					self.insType.append("NOP")
					self.data.append('')
			elif (elvDec >= 160 and elvDec <= 191):
				self.isInstr.append(True)
				self.opCodeStr.append("B")
				self.insType.append("B")
				self.data.append('')
			elif (elvDec == 1104):
				self.isInstr.append(True)
				self.opCodeStr.append("AND")
				self.insType.append("R")
				self.data.append('')
			elif (elvDec == 1112):
				self.isInstr.append(True)
				self.opCodeStr.append("ADD")
				self.insType.append("R")
				self.data.append('')
			elif (elvDec == 1160 or elvDec == 1161):
				self.isInstr.append(True)
				self.opCodeStr.append("ADDI")
				self.insType.append("I")
				self.data.append('')
			elif (elvDec == 1360):
				self.isInstr.append(True)
				self.opCodeStr.append("ORR")
				self.insType.append("R")
				self.data.append('')
			elif (elvDec == elvDec >= 1440 and elvDec <= 1447):
				self.isInstr.append(True)
				self.opCodeStr.append("CBZ")
				self.insType.append("CB")
				self.data.append('')
			elif (elvDec >= 1448 and elvDec <= 1455):
				self.isInstr.append(True)
				self.opCodeStr.append("CBNZ")
				self.insType.append("CB")
				self.data.append('')
			elif (elvDec == 1624):
				self.isInstr.append(True)
				self.opCodeStr.append("SUB")
				self.insType.append("R")
				self.data.append('')
			elif (elvDec == 1616):
				self.isInstr.append(True)
				self.opCodeStr.append("EOR")
				self.insType.append("R")
				self.data.append('')
			elif (elvDec == 1672 or elvDec == 1673):
				self.isInstr.append(True)
				self.opCodeStr.append("SUBI")
				self.insType.append("I")
				self.data.append('')
			elif (elvDec >= 1684 and elvDec <= 1687):
				self.isInstr.append(True)
				self.opCodeStr.append("MOVZ")
				self.insType.append("IM")
				self.data.append('')
			elif (elvDec >= 1940 and elvDec <= 1943):
				self.isInstr.append(True)
				self.opCodeStr.append("MOVK")
				self.insType.append("IM")
				self.data.append('')
			elif (elvDec == 1690):
				self.isInstr.append(True)
				self.opCodeStr.append("LSR")
				self.insType.append("R")
				self.data.append('')
			elif (elvDec == 1691):
				self.isInstr.append(True)
				self.opCodeStr.append("LSL")
				self.insType.append("R")
				self.data.append('')
			elif (elvDec == 1984):
				self.isInstr.append(True)
				self.opCodeStr.append("STUR")
				self.insType.append("D")
				self.data.append('')
			elif (elvDec == 1986):
				self.isInstr.append(True)
				self.opCodeStr.append("LDUR")
				self.insType.append("D")
				self.data.append('')
			elif (elvDec == 2038):
				self.isInstr.append(True)
				self.opCodeStr.append("BREAK")
				self.insType.append("BREAK")
				self.data.append('')
			else:
				self.isInstr.append(False)
				self.opCodeStr.append('')
				self.insType.append("DATA")
				self.data.append(42)
		# TESTPRINT
		# print 'isInstr[]:  '
		# print self.isInstr
		# print 'opCodeStr[]:  '
		# print self.opCodeStr
		# print 'data[]:'
		# print self.data
		# print 'insType[]: '
		# print self.insType
		# print 'number of lines in machineLines: ' + str(self.numLinesText)
		# print 'memory in memLines[]: ' + str(self.memLines)
	##################################################################################
	#   processRegs:  Uses masks and instruction types to populate the register lists.
	#   Nonexistent registers left empty in their respective list elements.
	##################################################################################
	def processRegs(self):
		# TESTPRINT
		# print
		# print 'Testing processRegs()...'
		k = 0
		for line in self.machineLines:
            # Grab binary line.
			tempBin = int(line, base=2)
			# Get Rm
			rmNum = ((tempBin & self.rmMask) >> 16)
			# Get sham
			shamNum = ((tempBin & self.shamMask) >> 10)
			# Get Rn
			rnNum = ((tempBin & self.rnMask) >> 5)
			# Get Rd/Rt
			rdRtNum = ((tempBin & self.rdMask) >> 0)
			# Get Immediate (I-format)
			immI = ((tempBin & self.immI) >> 10)
			# Get Immediate (IM-format)
			immIM = ((tempBin & self.immIM) >> 5)
			# Get Addr (D-Format)
			adD = ((tempBin & self.addrD) >> 12)
			# Get Addr (CB-Format)
			adCB = ((tempBin & self.addrCB) >> 5)
			# Get Addr (B-Format)
			adB = ((tempBin & self.addrB) >> 0)
			# Get op2
			# Get Shift
			shiftNum = ((tempBin & self.shiftMask) >> 21)
			# Test for R-Format
			if (self.insType[k] == 'R'):
				self.rmRegNum.append(rmNum)
				self.rnRegNum.append(rnNum)
				self.rdRtRegNum.append(rdRtNum)
				self.immNum.append('')
				self.addrNum.append('')
				self.shiftNum.append('')
				if (shamNum != 0):
					self.shamNum.append(shamNum)
				else:
					self.shamNum.append('')
			# Test for I-Format
			elif (self.insType[k] == "I"):
				self.rmRegNum.append('')
				self.rnRegNum.append(rnNum)
				self.rdRtRegNum.append(rdRtNum)
				self.immNum.append(immI)
				self.addrNum.append('')
				self.shiftNum.append('')
				self.shamNum.append('')
			# Test for D-Format
			elif (self.insType[k] == "D"):
				self.rmRegNum.append('')
				self.rnRegNum.append(rnNum)
				self.rdRtRegNum.append(rdRtNum)
				self.immNum.append('')
				self.addrNum.append(adD)
				self.shiftNum.append('')
				self.shamNum.append('')
			# Test for CB-Format
			elif (self.insType[k] == "CB"):
				self.rmRegNum.append('')
				self.rnRegNum.append('')
				self.rdRtRegNum.append(rdRtNum)
				self.immNum.append('')
				self.addrNum.append(adCB)
				self.shiftNum.append('')
				self.shamNum.append('')
			# Test for IM-Format
			elif (self.insType[k] == "IM"):
				self.rmRegNum.append('')
				self.rnRegNum.append('')
				self.rdRtRegNum.append(rdRtNum)
				self.immNum.append(immIM)
				self.addrNum.append('')
				# Test for proper quadrant of movk, movz:
				if (shiftNum == 0):
					self.shiftNum.append(0)
				elif (shiftNum == 1):
					self.shiftNum.append(16)
				elif (shiftNum == 2):
					self.shiftNum.append(32)
				else:
					self.shiftNum.append(48)
				self.shamNum.append('')
			# Test for B-Format
			elif (self.insType[k] == "B"):
				self.rmRegNum.append('')
				self.rnRegNum.append('')
				self.rdRtRegNum.append('')
				self.immNum.append('')
				self.addrNum.append(adB)
				self.shiftNum.append('')
				self.shamNum.append('')
			# Test for BREAK
			elif (self.insType[k] == "BREAK"):
				self.rmRegNum.append('')
				self.rnRegNum.append('')
				self.rdRtRegNum.append('')
				self.immNum.append('')
				self.addrNum.append('')
				self.shiftNum.append('')
				self.shamNum.append('')
			# Test for NOP
			elif (self.insType[k] == "NOP"):
				self.rmRegNum.append('')
				self.rnRegNum.append('')
				self.rdRtRegNum.append('')
				self.immNum.append('')
				self.addrNum.append('')
				self.shiftNum.append('')
				self.shamNum.append('')
			# Test for Data
			elif (self.insType[k] == 'DATA'):
				self.rmRegNum.append('')
				self.rnRegNum.append('')
				self.rdRtRegNum.append('')
				self.immNum.append('')
				self.addrNum.append('')
				self.shiftNum.append('')
				self.shamNum.append('')
				testBin = tempBin >> 31
				# If data is negative.
				if (testBin == 1):
					twoC = (0xFFFFFFFF ^ tempBin) + 1
					dataVal = int(twoC) * -1
					self.data[k] = dataVal
					# TESTPRINT
					# print " -" + str(twoC)
					# print " dataVal: " + str(dataVal)
				# If data is positive...
				else:
					self.data[k] = (int(tempBin))
			else:
				print "Error: unknown data type."
				self.rmRegNum.append('')
				self.rnRegNum.append('')
				self.rdRtRegNum.append('')
				self.immNum.append('')
				self.addrNum.append('')
				self.shiftNum.append('')
				self.shamNum.append('')
			k += 1
	##################################################################################
	#   getSpacedStr:  Takes 1st 11 bits, formats them, and populates
	#   spaced string list.
	##################################################################################
	def getSpacedStr(self):
		# TESTPRINT
		# print
		# print 'Testing getSpacedStr()...'
		k = 0
		for instr in self.machineLines:
			# TESTPRINT
			# print instr
			if (self.isInstr[k] == True):
				temp = "" + instr[0:8]
				temp = temp + " "
				temp = temp + instr[8:11]
				temp = temp + " "
				temp = temp + instr[11:16]
				temp = temp + " "
				temp = temp + instr[16:21]
				temp = temp + " "
				temp = temp + instr[21:26]
				temp = temp + " "
				temp = temp + instr[26:32]
				self.instrSpaced.append(temp)
			else:
				self.instrSpaced.append('')
			k += 1
		# TESTPRINT
		# print 'test instrSpaced: ' + str(self.instrSpaced)
	##################################################################################
	#   printAssem: iterates through the lists and prints assembley code.
	##################################################################################
	def printAssem(self):
		# TESTPRINT
		# print
		# print 'Testing printAssem()...'
		k = 0
		for k in range(k, self.numLinesText):
			# Pull single line of binary data, spaced.
			line = ''
			if (self.isInstr[k] == True):
				# Memory address.
				line += self.instrSpaced[k]
			else:
				line += self.machineLines[k]

			line = line + '\t' + str(self.memLines[k])
			# Print R formats
			if (self.insType[k] == 'R'):
				line = line + '\t' + self.opCodeStr[k]
				line = line + '\t' + 'R' + str(self.rdRtRegNum[k]) + ', '
				line = line + ' ' + 'R' + str(self.rmRegNum[k]) + ','
				# Does this R-format use shift?
				if (self.shamNum[k] == ''):
					line = line + ' ' + 'R' + str(self.rnRegNum[k])
				else:
					line = line + ' ' + '#' + str(self.shamNum[k])
			elif (self.insType[k] == 'I'):
				line = line + '\t' + self.opCodeStr[k]
				line = line + '\t' + 'R' + str(self.rdRtRegNum[k]) + ','
				line += ' R' + str(self.rnRegNum[k]) + ','
				line += ' #' + str(self.immNum[k])
			elif (self.insType[k] == 'D'):
				line += '\t' + self.opCodeStr[k]
				line += '\t' + 'R' + str(self.rdRtRegNum[k]) + ','
				line += ' ' + '[R' + str(self.rnRegNum[k]) +', #'
				line += str(self.addrNum[k]) + ']'
			elif (self.insType[k] == "CB"):
				line += '\t' + self.opCodeStr[k]
				line += '\t' + 'R' + str(self.rdRtRegNum[k]) + ','
				line += ' ' + '#' + str(self.addrNum[k])
			elif (self.insType[k] == "B"):
				line += '\t' + self.opCodeStr[k]
				line += '\t' + "#" + str(self.addrNum[k])
			elif (self.insType[k] == "IM"):
				line += '\t' + self.opCodeStr[k]
				line += '\t' + "R" + str(self.rdRtRegNum[k]) +','
				line += ' ' + str(self.immNum[k]) + ','
				line += ' ' + "LSL " + str(self.shiftNum[k])
			elif (self.insType[k] == 'BREAK'):
				line += '\t' + self.opCodeStr[k]
			elif (self.insType[k] == 'DATA'):
				line += '\t' + str(self.data[k])
			self.finalText += line + '\n'
			# print line
		print self.finalText
	##################################################################################
	#   writeOut:  writes final product to text file.
	##################################################################################
	def writeOut(self):
		outFile = open(self.oFile, 'w')
		outFile.write(self.finalText)
		outFile.close()
	##################################################################################
	#   run:  processes provided text file.
	##################################################################################
	def run(self):
	# Open inFile & store data to list.
		self.openRead()
		self.processElvBits()
		self.processRegs()
		self.getSpacedStr()
		self.printAssem()
		self.writeOut()
##################################################################################
#   main:  grabs arguments from command line.
##################################################################################
import sys, getopt
def main():

	diss = Dissemble()

	# Get command line data
	numCmdArgs = len(sys.argv)  # Store number of cmd args.
	cmdArgList = str(sys.argv)  # Store list of cmd args.
	# TESTPRINT
	# print "Number of command line arguments: %d" % numCmdArgs
	# print "List of command line arguments: %s" % cmdArgList

	# Check command line data
	inFile = ''     # Store input file name
	outFile = ''    # Store output file name
	for i in range(len(sys.argv)):
		if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
			inFile = sys.argv[i+1]
		elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
			outFile = sys.argv[i+1]
	# TESTPRINT
	# print "inFile: " + inFile
	# print "outFile: " + outFile

	# Store command line file names to class instance.
	print
	diss.iFile = inFile     # Save input file name to diss object.
	diss.oFile = outFile    # Save output file name to diss object.
	# TESTPRINT
	# print "In diss instance, iFile is: " + diss.iFile
	# print "In diss instance, oFile is: " + diss.oFile

	diss.run()

if __name__== "__main__":
    main()