# import pickle

# file1 = open("coms.dat","rb")

# try:
#     while True:
#         x = pickle.load(file1)
#         print(x)
# except EOFError:
#     file1.close()

# x = "PKG is my fater"
# pickle.dump(x,file1)

# file1.close()
import csv

file1 = open("Names.csv" , "r+")

# writer = csv.writer(file1)
# writer.writerows([["hi"],["bye"],["billo"],["tillo"],["pillo"]])
reder = csv.reader(file1)
for i in reder:
    print(i)
    print(".")

file1.close()