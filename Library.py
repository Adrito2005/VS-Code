import pwinput
x = {"adrito_25":"45as7d","nishu_89":"hg3$g45a","kushagra_78":"12@3dasd","arth_69":"as6w7e4","pankaj_25":"ahgfffer","kavya_56":"1d2asd454"}
un = ""
flag = 0
def login():
    global flag
    if (uname() == True):
        for i in range(3):
            if (pwd() == True):
                print("Welcome")
                t = True
                break
            else:
                print("INVALID PASSWORD")
                print(f"You have {2-i} attempts left")
                t = False
                flag = flag +1
            if (t == False and flag  == 3 ):
                print("Your Account has been blocked. Contact admin to renew ur account")
                
    else:
        print("INVALID USERNAME RETRY")
        login()
        
def uname():
    global x
    global un
    un = input("Enter your Username ")
    if (un in x.keys()):
        return True
    else:
        return False

def pwd():
    global x
    global un
    pw = pwinput.pwinput(prompt= f"Enter the password of {un} --> ", mask = "*")
    if (x[un] == pw):
        return True
    else:
        return False
    


login()