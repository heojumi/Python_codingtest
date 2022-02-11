import sys
n= int(sys.stdin.readline())
data = list(map(int, input().split()))
data.sort()
target=1
for i in data:
  if(i>target):
    print(target)
    break
  target += i
 