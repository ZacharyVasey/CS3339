##################################################################################
#   this
#       Takes:
#       Returns:
##################################################################################
class Dissemble(object):
    def __init__(self):
        self.iFile = ''     # Holds name of input file (via command line).
        self.oFile = ''     # Holds name of output file (via command line).
        self.machineCodeFile = ''     # Holds name of string of all binary data from input file.
        self.machineLines = []  # Holds RAW lines of binary text file, WITHOUT '\n' and '\t'
        self.instrSpaced = []   # Holds formatted lines of binary lines.
        self.decEleven = []     # Holds list of first eleven bits of each line in decimal.
        self.refOpBin = []      # Holds refined opcodes in binary (correct number of digits).
        self.opCodeStr = []     # Holds string literals of opcodes.
        self.dataSection = False    # Data flag
        self.isData = []        # ???
    def run(self):
        print '\n**************************    Inside Dissemble.run()    **************************'
    def openRead(self):     # Opens file and reads binary lines into list.
        with open(self.iFile) as self.machineCodeFile:      # 18-20 read in lines WITHOUT tabs.
            self.machineLines = self.machineCodeFile.readlines()
        self.machineLines = [x.strip() for x in self.machineLines]
        print
        print 'Testing openRead()...' + '\niFile: ' + self.iFile
        print 'machineCode[]: '
        for item in self.machineLines:  # Print all raw binary lines in machineLines[].
            print item
        self.machineCodeFile.close()    # Clean up.
    def loadInstrSpaced(self):      # loads instrSpaced[] with formatted binary lines.
        for line in self.machineLines:
            temp = "" + line[0:8]
            temp = temp + " "
            temp = temp + line[8:11]
            temp = temp + " "
            temp = temp + line[11:16]
            temp = temp + " "
            temp = temp + line[16:21]
            temp = temp + " "
            temp = temp + line[21:26]
            temp = temp + " "
            temp = temp + line[26:32]
            self.instrSpaced.append(temp)
        print '\nTesting loadIntrSpaced()...'
        print 'Testing instrSpaced[]: '
        for item in self.instrSpaced:       # Print all lines in instrSpaced[].
            print item
    def fillDecOps(self):   # Gets decimal values from 1st 11 bits and fills decEleven list.
        print
        print 'Testing fillDecOps()...'
        for line in self.machineLines:
            temp = line[0:11]       # Grab first 11 characters in string.
            dec = int(temp, 2)      # Convert from binary to decimal.
            self.decEleven.append(dec)      # Slap into decELeven[].
        print 'Testing decEleven[]: '
        print self.decEleven
    def fillOpCodeStr(self):        # Fills opCodeStr[] with human-readable opcode words.
        print '\nTesting fillOpCodeStr()...'
        index = 0
        for op in self.decEleven:
            if (self.dataSection == False):
                self.isData.append(False)
                if (op >= 160 and op <= 191):
                    self.opCodeStr.append("B")
                    # self.refOpBin.append(i[0:6])
                    # btype(arg1, arg1Str, i)
                    # arg2Str.append("")
                    # arg2.append("")
                    # arg3Str.append("")
                    # arg3.append("")
                    # validStr.append('Y')
                elif (op == 1104):
                    self.opCodeStr.append("AND")
                    # self.refOpBin.append(i[0:11])
                    # rtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
                    # validStr.append('Y')
                elif (op == 1112):
                    self.opCodeStr.append("ADD")
                    # self.refOpBin.append(i[0:11])
                    # rtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
                    # validStr.append('Y')
                elif (op == 1160 or op == 1161):
                    self.opCodeStr.append("ADDI")
                    # self.refOpBin.append(i[0:10])
                    # itype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
                    # validStr.append('Y')
                elif (op == 1360):
                    self.opCodeStr.append("ORR")
                    # self.refOpBin.append(i[0:11])
                    # rtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
                    # validStr.append('Y')
                elif (op >= 1440 and op <= 1447):
                    self.opCodeStr.append("CBZ")
                    # self.refOpBin.append(i[0:8])
                    # c_btype(arg1, arg1Str, arg2, arg2Str, i)
                    # arg3Str.append("")
                    # arg3.append("")
                    # validStr.append('Y')
                elif (op >= 1448 and op <= 1455):
                    self.opCodeStr.append("CBNZ")
                    # self.refOpBin.append(i[0:8])
                    # c_btype(arg1, arg1Str, arg2, arg2Str, i)
                    # arg3Str.append("")
                    # arg3.append("")
                    # validStr.append('Y')
                elif (op == 1624):
                    self.opCodeStr.append("SUB")
                    # self.refOpBin.append(i[0:11])
                    # rtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
                    # validStr.append('Y')
                elif (op == 1672 or op == 1673):
                    self.opCodeStr.append("SUBI")
                    # self.refOpBin.append(i[0:10])
                    # itype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
                    # validStr.append('Y')
                elif (op >= 1684 and op <= 1687):
                    self.opCodeStr.append("MOVZ")
                    # self.refOpBin.append(i[0:9])
                    # imtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
                    # validStr.append('Y')
                elif (op >= 1940 and op <= 1943):
                    self.opCodeStr.append("MOVK")
                    # self.refOpBin.append(i[0:9])
                    # imtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
                    # validStr.append('Y')
                elif (op == 1690):
                    self.opCodeStr.append("LSR")
                    # self.refOpBin.append(i[0:11])
                    # rtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
                    # validStr.append('Y')
                elif (op == 1691):
                    self.opCodeStr.append("LSL")
                    # self.refOpBin.append(i[0:11])
                    # rtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
                    # validStr.append('Y')
                elif (op == 1984):
                    self.opCodeStr.append("STUR")
                    # self.refOpBin.append(i[0:11])
                    # dtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
                    # validStr.append('Y')
                elif (op == 1986):
                    self.opCodeStr.append("LDUR")
                    # self.refOpBin.append(i[0:11])
                    # dtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
                    # validStr.append('Y')
                elif (op == 2038):
                    self.opCodeStr.append("BREAK")
                    # self.refOpBin.append(i[0:11])
                    # arg1.append("")
                    # arg2.append("")
                    # arg3.append("")
                    # arg1Str.append("")
                    # arg2Str.append("")
                    # arg3Str.append("")
                    # validStr.append('Y')
                    # data_section = True
                else:
                    self.opCodeStr.append("error")
                    self.refOpBin.append("")
                    # arg1.append("")
                    # arg2.append("")
                    # arg3.append("")
                    # arg1Str.append("")
                    # arg2Str.append("")
                    # arg3Str.append("")
                    # validStr.append('N')
            else:
                print
                # isData.append(True)
                # arg1.append("")
                # arg2.append("")
                # arg3.append("")
                # arg1Str.append("")
                # arg2Str.append("")
                # arg3Str.append("")
                # validStr.append('Y')
        print 'Testing opCodeStr[]:'
        for op in self.opCodeStr:
            print op


##################################################################################
#   this
#       Takes:
#       Returns:
##################################################################################
import sys, getopt
def main():
    print '\n**************************    Inside main program    **************************\n'

    diss = Dissemble()

    # Get command line data
    numCmdArgs = len(sys.argv)  # Store number of cmd args.
    cmdArgList = str(sys.argv)  # Store list of cmd args.
    print "Number of command line arguments: %d" % numCmdArgs
    print "List of command line arguments: %s" % cmdArgList

    # Check command line data
    inFile = ''     # Store input file name
    outFile = ''    # Store output file name
    for i in range(len(sys.argv)):
        if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
            inFile = sys.argv[i+1]
        elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
            outFile = sys.argv[i+1]
    print "inFile: " + inFile
    print "outFile: " + outFile

    # Store command line file names to class instance.
    print
    diss.iFile = inFile     # Save input file name to diss object.
    print "In diss instance, iFile is: " + diss.iFile
    diss.oFile = outFile    # Save output file name to diss object.
    print "In diss instance, oFile is: " + diss.oFile

    # Open inFile & store data to list.
    diss.openRead()

    # Fill list decOps with decimal values of first 11 bits
    diss.fillDecOps()

    # Fill list instrSpaced with formatted binary strings.
    diss.loadInstrSpaced()

    # Fill list in opCodeStr with opcode words.
    diss.fillOpCodeStr()


    print '\n**************************    End main program    **************************\n'

if __name__== "__main__":
  main()




