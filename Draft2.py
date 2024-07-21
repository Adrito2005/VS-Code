z = int(input("Enter a number "))
res = ""
f = 0
file = open("num.txt" , "w+")
for s in range(3,z):
    file.write("-***************************************-\n")
    file.write(str(s) + "\n")
    for i in range(1 , s):
        f = 0
        res = ""
        for j in range(i , s):
            f = f + j
            res = res + str(j) + "+"
            if(f == s and len(res) > 0):
                file.write((res[:-1]) + "\n")
                break
file.close()