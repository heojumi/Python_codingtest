import sys
k = int(sys.stdin.readline())
food_time = list(map(int, sys.stdin.readline().split()))
length = len(food_time)
count = 0
for i in range (k+1):
  if(count == length):
    count = 0
  if(food_time[count]==0):
    count+=1
  if(i==k):
    print(count+1)
    break
  
  food_time[count] -= 1
  count +=1