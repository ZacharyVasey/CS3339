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
	
bin = "1001011"
print bin, " in decimal is ", bin_to_dec(bin)
bin = "1010"
print bin, " in decimal is ", bin_to_dec(bin)
bin = "10100"
print bin, " in decimal is ", bin_to_dec(bin)
bin = "101000"
print bin, " in decimal is ", bin_to_dec(bin)