months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
dictionary = {}
flag = 0
for i in months:
    dictionary[i.upper()] = days[flag]
    flag += 1


n = input("Enter the month of the year or the number of days ")

if (n == "31" or n == "30" or n == "28"):
    n = int(n)
else:
    n = n.upper()

fl_ag = 0
for i in months:
    i = i.upper()
    if i == n:
        print(dictionary[i])
    elif (dictionary[i] == n):
        print(months[fl_ag])
    fl_ag += 1
