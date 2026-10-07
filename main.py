import time
lister = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(lister)
print(lister[0])
print(lister[9])
print(lister[-1])
print(lister[-2])
lister.append(16)
print(lister)
lister.insert(5,9032190123901902309132)
print(lister)
lister.remove(5)
print(lister)
lister.pop(4)
print(lister)

#2D list omg ndpjasdpk
listing = [[1,2,3],[4,5,6],[7,8,9]]
print(listing)
print("num of rows :",len(listing))
print("num of colum ;",len(listing[0]))
print(listing[1][1])
print(listing[0][2])
print(listing[2][0])

for i in range(3):
    for j in range(3):
        print(listing[i][j],end=" ")
    print("\n")

rows = int(input("How many rows do you want\n \n"))
col = int(input("How many colunms do you want\n \n"))
matrix1 = []
for i in range(rows):
    temp = []
    for j in range(col):
        a = int(input("What elements do you want?\n"))
        temp.append(a)
    matrix1.append(temp)
print(matrix1) 

for i in range(rows):
    for j in range(col):
        print(matrix1[i][j],end=" ")
    print("\n")

matrixA = [[1,2],[3,4]]
matrixB = [[5,6],[7,8]]
result = [[0,0],[0,0]]
for i in range(0,2):
    for j in range(0,2):
        result[i][j] = matrixA[i][j] + matrixB[i][j]

for i in range(0,2):
    for j in range(0,2):
        print(result[i][j],end=" ")
    print("\n")

    


