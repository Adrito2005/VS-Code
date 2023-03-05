a = input("Enter to check weather it is palindrome or not ")
s = ""
for i in range(-1, -((len(a))+1), -1):
    s = s+a[i]

if s == a:
    print("It is palindrome ")
else:
    print("It is not a palindrome number")
