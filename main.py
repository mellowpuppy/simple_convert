'''
A simple converter tool.
Converts decimal, hex, binary, and ascii.

Author: mp
'''

# take first value to be converted
print("Convert what type of value?\n")
print("Type b for binary, d for decimal, h for hex, or a for ascii\n")
convertfrom = str(input())
print("Ok, please enter the value: ")
if convertfrom == "h" or convertfrom == "a":
	start_value = input()
else:
	start_value = int(input())
print(f"Thank you, we will start with {start_value}.\n")

# choose what to convert the value into
print("And what would you like to convert this to?\n")
print("Type b for binary, d for decimal, h for hex, or a for ascii\n")
convert2 = str(input())

dnum = 0
i = 1
# convert decimal to hex
if convertfrom == "d" and convert2 == "h":
	print("\n" + hex(start_value))

# convert binary to decimal
elif convertfrom == "b" and convert2 == "d":
	while start_value != 0:
		rem = start_value % 10
		dnum = dnum + (rem*i)
		i = i*2
		start_value = int(start_value/10)

	print("\nEquivalent Decimal Value = ", dnum)

# convert decimal to ascii
elif convertfrom == "d" and convert2 == "a":
	print(chr(start_value))

# convert hex to ascii
elif convertfrom == "h" and convert2 == "a":
	print(bytearray.fromhex(start_value).decode())

# convert hex to decimal
elif convertfrom == "h" and convert2 == "d":
	dnum = int(start_value, 16)
	print(f"\n {dnum}")

# convert decimal to binary
elif convertfrom == "d" and convert2 == "b":
	dnum = bin(start_value)
	print(f"\n {dnum}")

# convert ascii to decimal
elif convertfrom == "a" and convert2 == "d":
	dnum=ord(start_value)
	print(f"\n {dnum}")

# if nothing fits quit the program
else:
	print("The input was not correct, please try again.")
	quit()
