num=int(input("Enter the no of rows for the V-Shape star pattern\n"))
if num<=0 and num==1:
    print("Not possible to print V-shape pattern for 1,zero and negetive numbers.ERROR!!")
    exit()
else:
    for i in range(1,num+1):
        for j in range(1,2*num):
            if j>=i and j<=num:
                print("* ",end="")
            else:
                print(" ",end="")
            j=j+1
        print()
        i=i+1