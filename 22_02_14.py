import sys
n = int(sys.stdin.readline())
data = list(sys.stdin.readline().split())
type = ['L','R','U','D']
dy = [-1,1,0,0]
dx = [0,0,-1,1]
des_x=1
des_y=1
for word in data:
  for i in range(4):
    if word == type[i]:
      x = des_x + dx[i]
      y = des_y + dy[i]
    
  if(x<1 or y<1 or x>n or y>n):
    continue
  
  des_x = x
  des_y = y
print(des_x,des_y)