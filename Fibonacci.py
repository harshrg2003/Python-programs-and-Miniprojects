def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

num=int(input("Enter a Number:"))
if num>0:
    print("fibonacci(",num,")=",fib(num),end="")
else:
    print("Error in input")