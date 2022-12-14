n=int(input ('Enter a number: '))
def fib(n):
    a,b,c=0,1,1
    print(a,b,end=" ")
    for i in range(n-2):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
fib(n)        
