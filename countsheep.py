# Write a python code that can calculate how many sheep are in the list as present
sheep=[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

sheepcount=0
presentsheep=[]

    
for i in sheep:
    if i ==True: #meaning present
        sheepcount=sheepcount=+1
        presentsheep.append(i)
        #print(presentsheep)
       
    else:
        continue
print(sheepcount)
   