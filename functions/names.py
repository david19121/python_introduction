def applicant():
    print("welcome applicant please enter your fullname")
    fullname=input()
    print("please enter your age") 
    age=int(input())
    print("please enter your job description")
    jobdescription=input()
    print("Hi, my name is " + fullname + ", and I am " + str(age) + " years, and my job description are : " + jobdescription )
    
applicant()