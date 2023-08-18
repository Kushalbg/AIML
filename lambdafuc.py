x=lambda a: a+5
print(x(5))

grt=lambda x,y: x if (x>y) else y
print(grt(6,9))

lst=[4,2,6]
a=list(map(lambda y: y+5,lst))
print(a)

lst=[3,6,2]
a=list(map(lambda x: x*x,lst))
print(a)

fib=[0,1,1,2,3,5,8,13,21,34]
f=list(filter(lambda x: x%2==0,fib))
print(f)

from functools import reduce
lst=[2,6,3,7,6,1,3]
l=reduce(lambda x,y: x+y,lst)
print(l)

from functools import reduce
lst=[2,6,3,7,6,1,3]
l=reduce(lambda x,y: x if (x>y) else y,lst)
print(l)

