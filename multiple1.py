a=int(input("Enter The First Number"))
b=int(input("Enter The Second Number"))
while (a>0 and  b>0 and a<=b):
        if(a%5==0):
                print("Multiple of 5 is",a)
                a=a+1
        else:
                print("Multiple of 5 is not",a)
                a=a+1       
	
input("Enter To Continue")
