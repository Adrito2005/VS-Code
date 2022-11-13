import random
def reco():
    
    print("")

    print("")
def main():
    print("Hi respected sir")
    print("How may I help you")

    choice = str(input("Data Updatetion [Y]  ----  Data Recolection [N] \n .........")).upper()
    print("...........")

    if (choice == "Y" or choice == "N"):
        if (choice == "Y"):
            updt()
        else:
            reco()
    else:
        print("Wrong option pressed")
        s = str(input("Do you want to retry Yes[Y] or No[N]")).upper()
        if (s == "Y" or s == "YES"):
            main()
def updt():
    def new():
        name =  str(input("Enter your name: ")).capitalize()
        age = int(input("Enter your age: "))
        email = str(input("Enter your email address"))
        mob = "+91 " + str(input("Enter your personal mobile number"))
        reg = name[:3]

        print ("Your new reg ID is: - ")
        k = random.randint(6,10)
        for i in range (k):
            reg = reg + (chr(random.randint(64, 126)))
        for j in range (k-4):
            reg = reg + str(random.randint(61,99))
        
        
        lines = [name , age , email, mob, reg]
        
        
        with open('readme.txt', 'w') as f:
            for line in lines:
                f.write(line)
                f.write('\n')
    
    def old():
        print("Howdy sir")
        x1 = str(input("Please enter your Registration number (REG. Number)"))
        

        print("I see you want to update your data")
    check = str(input("Are you new? (Yes[Y] --- No[N])")).upper()
    if (check == "Y"):
        new()
    else:
        old()
    
main()