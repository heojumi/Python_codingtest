#입력받은 배열을 정렬 후 가장 큰 공포도를 기준으로 n보다 작을시 그룹을 만든다.
# (정렬한 배열의 뒤에서부터 인원을 모집한다.) 그후 n에서 그룹인원만큼 마이너스 연산을 한다.
#  남은 사람 중 가장 큰 공포도를 기준으로 그룹을 만든다.
#  단, n이 공포도보다 작을시 그룹을 생성할 수 있다. 

#n과 data를 입력받는다
n = int(input())
data = list(map(int, input().split()))

#data를 정렬한다
data.sort()


count = 0

#공포도가 n보다 작거나 같을때만 연산을 수행한다.
while(data[n-1] <= n):
  n -= data[n-1]
  count += 1

print(count)