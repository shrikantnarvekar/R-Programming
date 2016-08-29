a=input("Enter your age:")
b=input("Enter amount in lakhs:")
a=int(a)
b=int(b)
if(a<60):
	if(b<5):
		print("you will get 6% Interest ")
	elif(b>=5 and b<=10):
		print("You will get 8% Interest ")
	elif(b>10):
		print("you will get 10% Interest")
else:
	if(a>=60):
		print("you will get 8% Interest ")
	elif(b>=5 and b<=10):
		print("You will get 9% Interest ")
	elif(b>10):
		print("you will get 11% Interest")

input("enter to continue")
