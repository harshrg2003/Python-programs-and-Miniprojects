l=10
def func1(n):
    global l
    l=l+45
    m=8
    print(l,m)
    print(n,"I have printed")

func1("Its me")
print(l)