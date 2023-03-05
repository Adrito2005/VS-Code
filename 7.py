x = int(input("Enter a number to act the function upon"))
n = int(input("Enter a range the function to act upon"))

f = 1
r = 1
for i in range(1, n+1):
    r += (x**i)/f
    f = f*i

print("Result = ", r)
