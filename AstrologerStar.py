num=int(input("Enter a number of rows for the star pattern,possibly greater than 1\n"))
if num<=0:
    print("Invalid!!There can be no star pattern for zero or negetive number")
    exit()
value=int(input("Enter either 0->For False or 1->For True\n"))
if value==0:
    val1=bool(value)
elif value==1:
    val1=bool(value)
else:
    print("Invalid!! You are supposed to enter either 0 or 1,and nothing else other than this")
    exit()
print("Star pattern would be as follows")

if val1==True:
    count = "*"
    while(num>0):
        print(count)
        count=count+"*"
        num=num-1

else:
    print(num*"*",end="")
    while(num>0):
        num=num-1
        print()
        print(num*"*",end="")

