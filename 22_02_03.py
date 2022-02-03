#값 여러개 입력
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))
#리스트 정렬
num_list.sort()

#가장 큰 수, 두번째로 큰 수 저장
first = num_list[n-1]
second = num_list[n-2]

#더하는 횟수 저장
first_count = m % (k+1)
second_count = m // (k+1)
first_count += k*second_count

#정답 계산
answer = first_count*first+second_count*second
print(answer)