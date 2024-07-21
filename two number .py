#Enter a Number 1
# Enter another Number 7
# 1 7 
# 1 4 7 
# 1 3 5 7 
# 1 2 3 4 5 6 7 


a =  int(input("Enter a Number "))
b = int(input("Enter another Number "))
x = abs(a-b)

for i in range(x,0,-1):
    if (x%i == 0):
        for m in range(a,b+1,i):
            print(m,end = " ")
            
        print("")