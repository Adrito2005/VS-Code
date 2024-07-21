def montly(n,p):
    day = "SUN MON TUE WED THU FRI SAT"
    der = "---------------------------"
    s = day.split()
    flag = 0

    print(day , "\n" , der)
    for j in s:
        if (n.upper() == j):
            break
        else:
            flag = flag + 1 
    print("   |"*flag, end  = "")
    for i in range(1,(p+1)):
        if(i  < 10 ):
            flag = flag + 1
            print(f"  {i}|",  end  = "")
            if(flag == 7):
                print()
                flag = 0
        if(i  > 9):
            flag = flag + 1
            print(f" {i}|", end  = "" )
            if(flag == 7):
                print()
                flag = 0
                
    print()
    return flag


yr = int(input(" "))

if (yr % 400 != 0):
    k = ((((yr - yr//4)%7 + ((yr//4)*2)%7))%7) - 1
    
else:
    k = (yr%400)-1
if k == 7:
    k =0
day = "SUN MON TUE WED THU FRI SAT"
s = day.split()
if (yr % 4 == 0):
    flag = 1

        
else:
    flag = 0
m = f"JAN 31 FEB {28 + flag} MAR 31 APR 30 MAY 31 JUN 30 JUL 31 AUG 31 SEPT 30 OCT 31 NOV 30 DEC 31"
month  = m.split()
for i in range(0,len(month),2):
    print()
    print(month[i])
    print()

    k = montly(s[k], int(month[i+1]))
   