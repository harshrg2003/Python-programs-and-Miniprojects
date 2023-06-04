import time
# initial= time.time()
# print(initial)
# k=0
# while(k<86):
#     print("This is Harsh")
#     k+=1
# print("While loop ran in",time.time()-initial,"Seconds")
localtime=time.asctime(time.localtime(time.time()))
print(localtime)

# k=0
# while(k<10):
#     print("This is Harsh")
#     time.sleep(3)
#     k+=1
localtime=time.asctime()
print(localtime)

localtime=time.ctime()
print(localtime)
print(time.asctime(time.gmtime(0)))