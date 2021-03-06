'''
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.
이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6
이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12
답은 12와 6의 차인 6을 출력한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


[입력 예]
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176	 

[출력 예]
#1 21
#2 11088
#3 1090
'''

# T 입력
T = int(input())

if T >= 1 and T <= 50: # T 조건
    minmax = [0] * T # 구간합 차이를 구할 minmax변수 선언

    for k in range(1, T+1): # T 조건
        N = list(map(int, input().split())) # N[0] = N, N[1] = M 

        if N[0] >= 10 and N[0] <= 100: # N 조건
            a = list(map(int, input().split()))
            
            x = [0]
            # 입력된 a의 각각 요소들이 조건에 맞으면 진행
            for i in a: # 각각의 요소들이 1이상 10000이하일 경우 각각의 요소들에 대해 1 반환
                if i >= 1 and i <= 10000:
                    x.append(1)

            # 모든 요소들이 조건을 만족하면 길이도 N이 될 것
            if sum(x) == N[0]: # N[0] = N, N[1] = M
                N_iter = N[0]+1-N[1] # 부분합 조각이 N+1-M개 발생함. ex) N = 10, M = 3 이면 8개의 연속 구간이 생김
                s = [0] * N_iter # 구간합 저장을 위해 구간의 갯수만큼 리스트 초기화

                # 구간합을 구함
                for i in range(0, N_iter):
                    for j in range(i,i+N[1]): # 한 칸씩 옮겨가며
                        s[i] += a[j]
                minmax[k-1] = max(s) - min(s)
            x = [0]

# 요구되는 양식에 맞게 출력
for i in range(0, T):
    print("#{0} {1}".format(i+1, minmax[i]))
