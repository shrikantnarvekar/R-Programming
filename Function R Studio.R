getmode <- function(v)
{
  uniqv=unique(v)
  uniqv[which.max(tabulate(match(v,uniqv)))]
}
v=c(2,1,2,3,1,2,3,4,1,5,5,3,2,3,4,1,1,1,1,1)
getmode(v)

n=c(8,8,8,9,6,6,6,4,5,3,9,8,2,1,3,4,6,7,8,9)
getmode(n)

m=c(1,4,90,87,66,54,32,66,66,54,54,54)
getmode(m)

o=c(25,37,8,40,45,29,42,12,25,16,20,36,30,33,24,24,11,35,30,45)
getmode(o)

p=c(8,9,9,7,10,6,7,8,9,7)
getmode(p)
