len1 = []
len2 = []

n = int(input("Enter the total number of data you want in here "))

for i in range(n):
    x = input("Enter the DOB in dd-mm-yyyy format ")
    y = input("Entter the nem of the person haveing DOB ")

    len1.append(x)
    len2.append(y)

s = input("Enter the year you want ")
for i in range(len(len1)):

    if (len1[i])[-4:] == s:
        print(len2[i])
