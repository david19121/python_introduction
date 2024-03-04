listmaximum=[20,60,70,90,500,700,800,99]
       
def findgreaterthan():
      for item in listmaximum:
        if item >=70:
            print(item)
        else:
            continue
      
       #print("No maximum items")  
print("This are the maximum number above the threshold " + str(findgreaterthan()))