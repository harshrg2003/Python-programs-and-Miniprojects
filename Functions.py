# a=9
# b=8
# c=sum((a,b))
# print(c)
def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)


num=int(input("Enter a number\n"))
result=factorial(num)
print("The factorial of the number",num,"is",result)