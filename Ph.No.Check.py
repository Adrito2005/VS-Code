st = input()

v = True
if len(st) > 12:
    v = False
if st[3] != '-' or st[7] != '-':
    v = False
for i in st:
    if ord(i) >= 48 and ord(i) <= 57 or ord(i) == 45:
        continue
    else:
        v = False

if v == True:
    print("Correct number given")
else:
    print("wrong number given")
