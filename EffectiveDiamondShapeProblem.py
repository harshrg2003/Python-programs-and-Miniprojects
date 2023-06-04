n=int(input("Enter the number of rows for the diamond shaped pattern\n"))
for i in range(-n,n+1):
    for j in range(-n,n+1):
        if ((abs(i)+abs(j))<=n):
            print("* ",end="")
        else:
            print("  ",end="")
    print("")