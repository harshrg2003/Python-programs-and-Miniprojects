#This is a mini-Project in python where u can keep track of exercises or food taken during the day by logging it and retriving it.
def getdate():
    import datetime
    return datetime.datetime.now()

def log():
    print("Choose among the following people .\n.Press 1.Harsh\n2.Alan\n3.Eshwar")
    k=int(input())
    Choice=int(input("Press 1.Exercise\n2.Food"))
    if k==1 and Choice==1:
        while(True):
           try:
               fp=open("Harsh_Exercise.txt","a")
               print("Enter the exercise recommended for u by the doctor")
               exercise=input()
               fp.write("Exercise:"+exercise+"["+str(getdate())+"]"+"\n")
               fp.close()
               print("Do u want to append more?? Press 'y' for yes ,'n' for no")
               ans=input()
               if ans=="y" or ans=="Y":
                   continue
               else:
                   print("All Exercises recommended and done succesfully saved")
                   break
           except Exception as e:
               print(e)
    elif k==1 and Choice==2:
        while(True):
            try:
                fl=open("Harsh_Food.txt","a")
                food=input("Enter the food recommended to u by the doctor")
                fl.write("Food taken:"+food+"["+str(getdate())+"]"+"\n")
                fl.close()
                print("Do u want to append more?? Press 'y' for yes and 'n' for no")
                ans1=input()
                if ans1=="y" or ans1=="Y":
                    continue
                else:
                    print("All the food recommended and taken saved succesfully")
                    break
            except Exception as e:
                print(e)
    elif k==2 and Choice==1:
        while(True):
            try:
                f=open("Alan_Exercise.txt","a")
                exercise2=input("Enter the exercises recommended by the doctor")
                f.write("Exercise done:"+exercise2+"["+str(getdate())+"]"+"\n")
                f.close()
                print("Do u want to append more?? Press 'y' for yes and 'n' for no")
                ans3=input()
                if ans3=="y" or ans3=="Y":
                    continue
                else:
                    print("All Excersises  recommended and done succesfully saved")
                    break
            except Exception as e:
                print(e)
    elif k==2 and Choice==2:
        while(True):
            try:
                f=open("Alan_Food.txt","a")
                food2=input("Enter the food items recommended by the doctor")
                f.write("Food taken:"+food2+"["+str(getdate())+"]"+"\n")
                f.close()
                print("Do u want to append more?? Press 'y' for yes and 'n' for no")
                ans4=input()
                if ans4=="y" or ans4=="Y":
                    continue
                else:
                    print("All food items  recommended and taken succesfully saved")
                    break
            except Exception as e:
                print(e)
    elif k==3 and Choice==1:
        while(True):
            try:
                f=open("Eshwar_Exercise.txt","a")
                exercise3=input("Enter the exercises recommended by the doctor")
                f.write("Exercise done:"+exercise3+"["+str(getdate())+"]"+"\n")
                f.close()
                print("Do u want to append more?? Press 'y' for yes and 'n' for no")
                ans5=input()
                if ans5=="y" or ans5=="Y":
                    continue
                else:
                    print("All exercises done are succesfully saved")
                    break
            except Exception as e:
                print(e)
    elif k==3 and Choice==2:
        while(True):
            try:
                f=open("Eshwar_Food.txt","a")
                food3=input("Enter the food items recommended by the doctor")
                f.write("Food taken:"+food3+"["+str(getdate())+"]")
                f.close()
                print("Do u want to append more?? Press 'y' for yes and 'n' for no")
                ans6=input()
                if ans6=="y" or ans6=="Y":
                    continue
                else:
                    print("All food items  recommended and taken succesfully saved")
                    break
            except Exception as e:
                print(e)

def retrieve():
    print("Choose among the following people for retrieval of their exercises done or food items taken",
          "Press 1 for 'Harsh'\n, Press 2 for 'Alan'\n,Press 3 for 'Eshwar'\n")
    a=int(input())
    print("Press 1.Exercises done\n2.Food Items taken")
    ch=int(input())
    if a==1 and ch==1:
        try:
            with open("Harsh_Exercise.txt") as fd:
                for line in fd:
                    print(line)
        except Exception as e:
            print(e)
    elif a==1 and ch==2:
        try:
            with open("Harsh_Food.txt") as fv:
                for line in fv:
                    print(line)
        except Exception as e:
            print(e)
    elif a==2 and ch==1:
        try:
            with open("Alan_Exercise.txt") as fs:
                for line in fs:
                    print(line)
        except Exception as e:
            print(e)
    elif a==2 and ch==2:
        try:
            with open("Alan_Food.txt") as file:
                for line in file:
                    print(line)
        except Exception as e:
            print(e)
    elif a==3 and ch==1:
        try:
            with open("Eshwar_Exercise.txt") as hp:
                for line in hp:
                    print(line)
        except Exception as e:
            print(e)
    elif a==3 and ch==2:
        try:
            with open("Eshwar_Food.txt") as z:
                for line in z:
                    print(line)
        except Exception as e:
            print(e)


print("Welcome to Health Management System")
count=0
while(True):
    print("Choose whether to Log or retrieve data .\nPress 1.Log\n2.Retreive\n")
    task=int(input())
    if task==1:
        print("Log ur data\n")
        log()
    elif task==2:
        print("Retrive the data stored\n")
        retrieve()
    else:
        print("OOPS!! Invalid input.TRY AGAIN")
        count+=1
        if count<=3:
              continue
        else:
            print("INVAID!!.EXITING THE APPLICATION")
            exit()
    print("Do u want to use this Health management application once again??\nPress 'y' for yes,'n' for no\n")
    choice=input()
    if choice=="y" or choice=="Y":
        continue
    elif choice=="n" or choice=="N":
        break
    else:
        print("Invalid input!!!Exiting the application.")
        exit()
print("Thank u for using the Health management System.")
exit()
