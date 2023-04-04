

for row in range (0,4,1):
  for col in range(0,4,1):
    if row==0 or col==3 :
      print("*",end="")
    else:
      print("",end="")
  print()

for row in range(0,4,1):
  for col in range(0,4,1):
    if row==0 or col==0 or col==3:
      print("*",end="")
    else:
      print(" ",end="")
  print()
for row in range(4):
  print("*",end="")