import sys
n= int(sys.stdin.readline())
for j in range(n):
  data = sys.stdin.readline()
  left = 0
  right = 0
  test = 0
  for i in range(len(data)):
    if(data[i]=="("):
      left += 1
    elif(data[i]==")"):
      right +=1
    if(left<right):
      test = 1
  if(left == right and test == 0):
    print("YES")
  else:
    print("NO")
