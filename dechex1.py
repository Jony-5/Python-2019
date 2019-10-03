# dechex1.py JMM
def hexcon(num):
	h16s = ""; h1s ="";
	h16 = int(num/16)
	temp = str(chr(87+h16))
	print("chr",temp)
	h1 = num % 16
	h = str(h16)+str(h1); h1s = str(h1)
	h = h16s = h1s
	return h


def main ():
	hs = "";hs2 = ""
	hs = hexcon(147)
	print(147,hs)
	
main()
