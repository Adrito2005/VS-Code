r = int(input("Enter the number of rows "))
c = int(input("Enter the number of column "))
l = []
tem = []
evensum, oddsum = 0, 0
for i in range(r):
    for j in range(c):
        x = int(input("Enter the number"))
        tem.append(x)
    l.append(tem)

for i in range(r):

    for j in range(len(l[i])):  # loop visit value in matrix

        if (j % 2 == 0):  # if the number is even position

            print('even=', l[i][j])
            evensum += l[i][j]

        else:
            print('odd=', l[i][j])
            oddsum += l[i][j]


print('Evensum=', evensum)

print('Oddsum=', oddsum)


# numbers = [[1, 4, 7, 6], [8, 5, 1, 11]]

# evensum = 0
# oddsum = 0
# dim = int(input("Enter dimension 0/1 vertical/horizontal:\n"))

# for i in range(len(numbers)):
#     for j in range(len(numbers[i])):
#         if dim == 0:
#             if (j % 2 == 0):
#                 evensum += numbers[i][j]
#             else:
#                 oddsum += numbers[i][j]
#         elif dim == 1:
#             if (i % 2 == 0):
#                 evensum += numbers[i][j]
#             else:
#                 oddsum += numbers[i][j]
# print(evensum, oddsum)
