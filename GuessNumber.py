num=26
TotalnoOfGuess=10
NoOFguess=0
while(True):
    inpNum=int(input("Enter any number\n"))
    if NoOFguess>TotalnoOfGuess:
        print("U lost in this game!!Better luck next time\nGAME OVER.")
        break
    if inpNum==num:
        NoOFguess=NoOFguess+1
        print("Congratulations you have guessed the correct number")
        print("No of attempted guess in which u got correct answer:",NoOFguess,"Out of",TotalnoOfGuess,"Guesses")
        break
    elif inpNum>num:
        NoOFguess = NoOFguess + 1
        print("Sorry!!Number you have guessed is GREATER.TRY AGAIN!!")
        continue
    elif inpNum<num:
        NoOFguess = NoOFguess + 1
        print("Sorry!!Number you have guessed is LESSER.TRY AGAIN!!")
        continue

