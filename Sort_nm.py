def main(name):

    res = name.title().split(' ')
    
    flag = ''
    f = 0

    for i in res:
        if f == len(res)-1:
            flag = flag + res[f]
        else:
            flag  = flag + (res[f])[0]+"."
        f += 1
    return (flag)
    
def file():
    lines = []
    flag = 0
    inp  = (str(input("You want File Input [Y] or Manual Input [N]  ")).upper())[0]
    if (inp[0].upper() == 'Y'):
        file_nm = str(input(("Specify the name of the file: ")))+".txt"
        with open (file_nm,'r') as a:
            abc= a.readlines()
        for f in range(len(abc)):
            abc[f] = ((abc[f])[:-1]).title()
        for p in range(len(abc)):
            x = main(abc[p])
            lines.append(x)
            lines[p] = abc[p] + " in short form is ----" + lines[p]
        with open('Names.txt', 'w') as f:
            for line in lines:
                f.write(line)
                f.write('\n')
                
    else:
        n = int(input("Enter the number of names you want to add: "))
        
        for i in range(n):
            nm = str(input(f"Enter the {i+1} -- name: "))
            lines.append(nm)
            x = main(nm)
            lines[flag] = lines[flag].title() + " in the short for is ---- \""+x+"\""
            x = ''
            flag += 1
        
    with open('Names.txt', 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')

file()