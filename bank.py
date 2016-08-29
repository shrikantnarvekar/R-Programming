pin=0000
a=1
while(a<=3):
	sec=int(input("Enter The Pin To Continue"))
	a+=1
	if(sec==pin):
			print("Welcome User")
	else:
			print("Incorrect")
			continue

input("Thank You")	
