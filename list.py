listofnumbers=[1,3,5,6,10,20,22]
#Write a python code that will sum all the list of numbers above together and check if the result is 67
y=0
for i in listofnumbers:
    #print(i)
    y=y+i
    print(y)
    if y==50:
        z=y*1000
        print("my result is: " + str(z))
        #print("thank you jesus")
    else:
        f=y-20
        print("the result i got is: " + str(f))
       # print("the result is not 67 right now")            
