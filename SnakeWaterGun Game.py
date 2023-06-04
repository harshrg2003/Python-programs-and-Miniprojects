import random
def games():
    YourScore=0
    CPUscore=0
    totalNoOFtimes=10
    i=0
    count=0
    while(i<totalNoOFtimes):
           lst=["Snake","Water","Gun"]
           choices=random.choice(lst)
           print("Enter what u choose among the following:Snake,Water,Gun.\n."
                 "Press 'S' for Snake,'W' for water,'G' for gun\n")
           urChoice=input()
           if (urChoice.lower()=="s") and (choices=="Water"):
               YourScore+=1
           elif (urChoice.lower()=="w") and (choices=="Snake"):
               CPUscore+=1
           elif (urChoice.lower()=="w") and (choices=="Gun"):
               YourScore+=1
           elif (urChoice.lower()=="g") and (choices=="Water"):
               CPUscore+=1
           elif (urChoice.lower()=="g") and (choices=="Snake"):
               YourScore+=1
           elif (urChoice.lower()=="s") and (choices=="Gun"):
               CPUscore+=1
           elif (urChoice.lower()=="s") and (choices=="Snake"):
               print("Oh!!!Its a draw!! TRY AGAIN")
               continue
           elif (urChoice.lower()=="w") and (choices=="Water"):
               print("Oh!!!Its a draw!! TRY AGAIN")
               continue
           elif (urChoice.lower()=="g") and (choices=="Gun"):
               print("Oh!!!Its a draw!! TRY AGAIN")
               continue
           else:
               if count<=3:
                    print("Invaild Input!!TRY AGAIN")
                    count+=1
                    continue
               else:
                   print("WRONG INPUT MORE THAN THREE TIMES!!!EXITING THE GAME ABRUPTLY.")
                   exit()
           i+=1

    print("Your score is:",YourScore,"Out of",totalNoOFtimes)
    print("Computer's score is:",CPUscore,"Out of",totalNoOFtimes)
    if YourScore>=CPUscore:
         print("U are the winner!!!WOHOO!!Well done")
    else:
        print("Sorry!!U lose.Better luck next time.\nComputer is the winner!!!!")


print("Welcome to Snake Water Gun Game")
while(True):
    print("Are u ready to play,let's Go!!!!")
    games()
    print("Do u want to play the game once again??\nPress 'y' for yes\nPress 'n' for no")
    c=input()
    if c=="Y" or c=="y":
        continue
    else:
        break
print("Thank u for playing the Game.HOPE U ENJOYED PLAYING!!!SEE U SOON")
