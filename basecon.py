# basecon.py JM

def bincon(num,addSpace):
	n = num
	s = addSpace
	print(n,s) #debug
	d = 128
	binString ="" #creat a string using binstring
	for i in range(0,8):
		q = int(n / d)
		r = int(n % d)
		n = r
		d = int(d / 2)
		binString = binString+str(q)
		if(s == 1 and i == 3):
			binString = binString = + " "
	print(binString)
def main():
	bincon(191,0)
	bincon(7,1)
	bincon(15,0)
	bincon(31,0)
main()
