'''
tip!!
    1. 시간제한, 메모리제한을 제일먼저 체크해야함.
        - '연산량'이 많은 코드가 실행시간이 오래걸림
        - '입력'을 보고 대충 시간을 계산할 수 있음!!
        - +와 *의 연산은 20~100배 차이남. 이럿듯, 연산에 따라 속도는 모두 다름
        - 모든 연산을 다 counting 할 수 없음. > 대충계산하기!(점근적 표기법)
            ex) 연산회수가 2n^2 + 4n 이라면? 시간복잡도는 다 떼고 n^2라고 계산
        - 시간복잡도 O(N)이라고 표현. > 항상 최악을 고려해야함
'''

# 백준 1748번 문제
# https://www.acmicpc.net/problem/1748

'''
입력 > 첫째 줄에 N(1=<N=<100,000,000)이 주어진다.
        O(N) 이상의 알고리즘은 불가능함을 알아야함!
        1초 제한에 max(N) = 10억
'''

# 시간제한 무제한이라 치고 풀어보자!

def solution(n):
    ret = 0
    for i in range(1, n+1):
        ret += len(str(i))
    return ret

# 깔끔히 정리해서

def solution(n):
    return sum(map(lambda x : len(str(x)), range(1, n+1)))

'''
변수저장 > 한개씩 더함 > 최정저장
lst 원소의 개수 n개라면
예) 더하기 연산1번, 반복문 n번 > 약 2n번 >> 입력n 일때 시간복잡도 2n
    lst이 길이가 2일때 : 더하기 2번
    lst이 길이가 10일때 : 더하기 10번
'''
def sum(self, lst):
    tot = 0
    for i in range(lst):
        tot += i
    return tot

'''
1부터 N까지 합을 구하시오.
'''

def sum_N(self, N):
    return N(N+1)//2

'''
O(logN) 예시 : 계속 길이가 절반으로 줄어들때
BigO(빅오) notation은 점근적 표현법
보통 천만~오천만 > 1초에 가능하게!
'''



