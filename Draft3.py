x = int(input("Enter the Number of cycles: "))
y = float(input("Enter the intrest percent: "))
z = int(input("Enter the initial amount: "))

for i in range(x):
    res = 0
    
    res = z*(y/100)
    
    z = z+res
    
print("Your final amount is ", z)

 