#내가 생각했던 방식은 다음과 같다. 먼저 값을 n만큼 받은 후 특정 행에서 가장 작은수만 다른리스트에 저장한다.
# 그 리스트를 또 정렬하여 가장 큰 수만 출력한다면 어떠한 값이 입력되어도 조건에 맞는 답을 도출해낼 수 있을 것이다.


#값 여러개 입력
n, m = map(int, input().split())

#빈 리스트 선언
data_list=[]

#반복문을 사용해 n만큼 값을 받을 수 있도록 설정했다.
for i in range(n):
  data = list(map(int, input().split()))
  #리스트 정렬
  data.sort()
  #리스트 정렬 후 가장 작은 수만 data_list 리스트에 저장한다.
  data_list.append(data[0])

#data_list를 정렬해 가장 큰수를 출력한다.
data_list.sort()
print(data_list[n-1])