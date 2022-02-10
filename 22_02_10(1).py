import sys
stack=[]
n=int(sys.stdin.readline())
for i in range(n):
  order=sys.stdin.readline()
  if(order[0:4] == 'push'):
    num=int(order[5:])
    stack.append(num)
  elif(order[0:3]=='pop'):
    if(len(stack)==0):
      print(-1)
    else:
      print(stack.pop())
  elif(order[0:4]=='size'):
    print(len(stack))
  elif(order[0:5]=='empty'):
    if(len(stack)==0):
      print(1)
    else:
      print(0)
  elif(order[0:3]=='top'):
    if(len(stack)==0):
      print(-1)
    else:
      print(stack[len(stack)-1])