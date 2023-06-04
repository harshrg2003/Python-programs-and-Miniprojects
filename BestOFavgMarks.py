marks1=int(input("Enter first test marks\n"))
marks2=int(input("Enter second test marks\n"))
marks3=int(input("Enter thrid test marks\n"))
minimum=min(marks1,marks2,marks3)
SumOFbestTWO=marks1+marks2+marks3-minimum
AVGOFbest2=SumOFbestTWO/2
print("The average of the best of two test marks is",AVGOFbest2)