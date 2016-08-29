a=input("Enter The Fees Paid ")
b=input("Enter The Numbers Of Days")
a=int(a)
b=int(b)
if (b<5):
 c=(10*a)/100
 c=a-c
elif(b<10):
  c=(15*a)/100
  c=a-c
elif(b<15):
  c=(20*a)/100
  c=a-c
else:
  c=(30*a)/100
  c=a-c
  
print("You will get Rs" , c)

input("Enter To Continue")
