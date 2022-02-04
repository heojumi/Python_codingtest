#n이 1이되면 종료되기 때문에 n이 1이 아닐때를 while의 조건문으로 설정했다. if문을 사용해 조건을 나누어 문제를 해결했다.

#n과 k를 입력받는다
n, k = map(int, input().split())
count = 0

#n이 1이 아니라면 계속 계산한다.
while(n!=1):
  #나머지가 0이면 몫을 n에 저장하고 count를 올린다.
  if n%k==0:
    n /= k
    count += 1
  #나머지가 0이 아니라면 n에서 1을 빼고 count를 올린다.
  else:
    n -= 1
    count += 1

print(count)