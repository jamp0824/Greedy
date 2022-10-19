# N, M, K를 공백으로 구분하여 입력받기.
n, m, k = map(int, input().split())

print('n = ', n)
print('m = ', m)
print('k = ', k)

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))
print('data =', data)
data.sort()             # 입력받은 수들 정렬하기
print('data = ', data)
print('n = ', n)
first = data[n-1]       # 가장 큰 수
print('first', first)
second = data[n-2]      # 두 번째로 큰 수
print('n = ', n)
print('second', second)
result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:      # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1          # 더할 때마다 1씩 빼기
    if m == 0:          # m이 0이라면 반복문 탈출
        break
    result += second    # 두 번째로 큰 수를 더하기
    m -= 1              # 더할 때마다 1씩 빼기

print("result = ", result)           # 최종 답안 출력

