a=input("Enter The Fees Paid: ")
b=input("Enter The Numbers Of Days: ")
a=int(a)
b=int(b)
if (b<5):
 c=(10*a)/100
 c=a-c
 print("10% will be deducted")
elif(b<10):
  c=(15*a)/100
  c=a-c
  print("15% will be deducted")
elif(b<15):
  c=(20*a)/100
  c=a-c
  print("20% will be deducted")
else:
  c=(30*a)/100
  c=a-c
  print("30% will be deducted")
  
print("You will get Rs:" , c)

input("Enter To Continue")
