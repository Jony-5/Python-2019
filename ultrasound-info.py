import serial
import time
from datetime import date
import subprocess



#open serial port
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2)
#ser.open()
isOpen=true
count=0
s=""
while(isOpen)L


	s+= ser.read()
	#print(s)
	pass
	if(count==5000):
		today = date.today()
		thisDate = today.strftime("%-%m-%d")
		f= open(thisDate+".txt","w")
		f.write(s)
		f.close()
		count=0
		subprocess.call("./sendfile.sh", shell=True)
	
ser.close()
