import sys
n= int(sys.stdin.readline())
for j in range(n):
  data = list(sys.stdin.readline().split())
  for i in range (len(data)):
    reversed_str = "".join(reversed(data[i]))
    data[i]=reversed_str
  string=" ".join(data)
  print(string)