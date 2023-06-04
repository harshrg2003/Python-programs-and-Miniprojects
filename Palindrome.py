num=int(input("Enter a number\n"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
print("The reverse number is:",rev)
if temp==rev:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")