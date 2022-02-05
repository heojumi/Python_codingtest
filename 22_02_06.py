#무리가 가장 작은 0이나 1을 뒤집어야 최소한으로 뒤집을 수 있다. 따라서 zero 나 one 중 작은 수를 출력한다.

#문자열로 input을 받는다
n = input()
#길이를 구한다
length = len(n)

zero = 0
one = 0

#첫번째 그룹에 따라 값을 더한다.
if(int(n[0])==1):
  one += 1
else:
  zero +=1

#다음 수와 비교하여 다르다면 변수의 값을 올리고 같다면 패스한다.  
for i in range(length-1):
  if(int(n[i]) != int(n[i+1])):
    if(int(n[i+1]) == 1):
      one += 1
    else :
      zero += 1

#두 변수중 작은 수를 출력한다.
if(one >= zero):
  print(zero)
else:
  print(one)

