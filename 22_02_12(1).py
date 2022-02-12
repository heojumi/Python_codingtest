import sys
n,m= map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
sum=n*(n-1)//2
count=1
for i in range(n-1):
  if(data[i]==data[i+1]):
    count+=1
  else:
    sum -= count*(count-1)//2
    count=1
if(count !=1):
  sum -=count*(count-1)//2
print(sum)
  