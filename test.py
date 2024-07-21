def an():
    j = 0
    dict={}

    a = input("Enter your username ")
    j = 0
    while j < 5:
        b  = input("Enter its password [Must be longer than 5 charecters] ")
        j=len(b) 
        if j <5:
            print("Password Length is not sufficient")
        else:
            file1 = open("my_file.txt","a")
            file1.write("sep" + "\n"+a+"\n" +b+"\n")
            file1.close
            dict[b] = a
def old():
    dict = {}
    username = input("Enter the userid")
    file = open("my_file.txt","r")
    dict = (file.read())
    lis = []
    lis = dict.split()
    for i in len(lis):
        if lis(i)  == "sep":
            uname = lis(i+1)
            if username == uname:
                password = input("Enter the User ID password")
                while password == lis(i+2):
                    print("Hello user ")
                    break
                else:
                    print("Incorrect password")
def new():
    print("Hello new user !")
    print("Are you a New User or Old Service User (N/O): ", end="")
    a = input(" ")
    a = a.upper()
    if a == "O":
        print("Old user")
    elif a == "N":
        an()
    else:
        print("invalid arguemt called ")
        x = input(" Do You want to retry (Y/n) ")
        x= x.upper()
        if x =="Y":
            new()

old()
