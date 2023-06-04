num=int(input("Enter the number of rows for which u want mountain like star pattern\n"))
if num<=0 and num==1:
    print("Invalid !! no star pattern can be made for negetive numbers,zero and 1")
    exit()

for i in range(0,num+1):
    for j in range(0,2*num):
        if i+j>num and j<=num:
            print("* ",end="")
        else:
            print(" ",end="")
        j=j+1
    print()
    i=i+1

