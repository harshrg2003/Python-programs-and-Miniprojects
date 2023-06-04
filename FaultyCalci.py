num1=input("Enter the first number")
print("Enter the operator among any of the following:+,-,*,/")
Opr=input()
num2=input("Enter the second number")
if Opr=="*":
    if num1=="45" and num2=="3":
        print("Your answer is 555")
    else:
        print("Result= ",int(num1)*int(num2))
elif Opr=="+":
    if num1=="56" and num2=="9":
        print("Your answer is 77")
    else:
        print("Result= ",int(num1)+int(num2))
elif Opr=="/":
    if num1=="56" and num2=="6":
        print("Your answer is 4")
    else:
        print("Result= ",int(num1)/int(num2))
else:
    result=int(num1)-int(num2)
    print("Result= ",result)
