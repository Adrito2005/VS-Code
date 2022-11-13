import random
name =  str(input("Enter your name: ")).capitalize()
age = int(input("Enter your age: "))
email = str(input("Enter your email address"))
mob = "+91 " + str(input("Enter your personal mobile number"))
s = name[:3]
print(type(s))
print(s)

print ("Your new reg ID is: - ")
k = random.randint(6,10)
for i in range (k):
    s = s + (chr(random.randint(64, 126)))
for j in range (k-4):
    s = s + str(random.randint(61,99))
print(s)