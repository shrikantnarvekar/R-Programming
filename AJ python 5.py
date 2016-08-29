x=0
y=1
count=0
print(x)
print(y)
while count<=7:
    fib=x+y
    print(fib)
    x=y
    y=fib
    count+=1
