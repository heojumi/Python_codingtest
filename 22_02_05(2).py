#가장 큰 수를 만들기 위해서는 0,1일때 덧셈을 실행해야하고 다른 숫자일 때는 곱셈을 실행해야한다. 
n = input()
length = len(n)

#순서를 저장한다.
seq = 0

#문자열을 정수로 변환한다.
num = int(n[seq])

for i in range(length-1):
  #0과 1일때 덧셈을 실행한다
  if(num == 0 or num == 1):
    num += int(n[seq+1])
    seq += 1
  
  #나머지일 경우 연산을 실행한다.
  else:
    num *= int(n[seq+1])
    seq += 1


print(num)
  