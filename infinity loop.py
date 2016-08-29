var = 'y'
a=0
s=0
while var == 'y' :
   num = int(input("Enter a number  :"))
   a=a+1
   s=s+num
   print ("You entered: ", num)
   var=input("Do You Want To Continue (y/n):")
print ("Sum Is",s)
print ("Total Numbers Entered Are",a)
print ("Average is",s/a)
print ("Good bye!")
input("Enter To Continue")
