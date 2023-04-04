row=int(input())
for i in range (row):
    for j in range (row-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()

for i in range(row):
    for j in range(row):
        if (j==9):
            print("*",end="")
        else:
            print(" ",end="")
    print()