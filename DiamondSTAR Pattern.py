num=int(input("Enter the no of rows for the diamond shape pattern\n"))
k=num//2
if num<=0 and num==1:
    print("Diamond shape pattern not possible for zero,1,and negetive numbers")
if num%2!=0:
    print("The diamond shape pattern of odd number of rows is as follows")
    for i in range(1,num+1):
        for j in range(1,num+1):
                 if i>=1 and i<=(k+1):
                     if j>=(k+1)-(i-1) and j<=(k+1)+(i+1):
                         print("* ",end="")
                     else:
                         print(" ",end="")
                 else:
                     l=k+1
                     m=i%l
                     if m>=1 and m<=k:
                         if m>=l-(i-1) and m<=l+(i+1):
                             print("* ",end="")
                         else:
                             print(" ",end="")
                         m=m+1
                 j=j+1
        print()
        i=i+1


else:
    print("The diamond shape pattern of even number of rows is as follows")
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i >= 1 and i <= k:
                if j >= k - (i - 1) and j <= k + (i + 1):
                    print("* ", end="")
                else:
                    print(" ", end="")
            else:
                m = i % k
                if m >= 1 and m <= k-1:
                    if j >= k - (i - 1) and j <= k + (i + 1):
                        print("* ", end="")
                    else:
                        print(" ", end="")
                    m = m + 1
            j = j + 1
        print()
        i = i + 1