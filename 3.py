s = int(input("Enter the number of subjects you have "))
tot = 0
avg = 0
for i in range(s):
    tot += int(input("Enter the obtained marks "))
avg = tot//s
if avg >= 81 and avg <= 100:
    print("Your Grade is A")
elif avg >= 61 and avg < 81:
    print("Your Grade is B")
elif avg >= 41 and avg < 61:
    print("Your Grade is C")
elif avg >= 33 and avg < 41:
    print("Your Grade is D")
elif avg >= 21 and avg < 33:
    print("Your Grade is E")
elif avg >= 0 and avg < 21:
    print("Your Grade is f")
else:
    print("Invalid Input!")
