import sys

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	return N, M


# 입력 받는 부분
N, M = Input_Data()

# 여기서부터 작성
def Dice1(n):
    # n번째 주사위 던졌을때 나올 숫자 선택 (중복순열)
    if n >= N:
        print(*dice)
        return
 
    for i in range(1, 6+1):
        # n번째 주사위 숫자 -> i
        dice[n] = i
        Dice1(n+1)
 
 
def Dice2(n, s):
    # 중복 조합
    if n>=N:
        print(*dice)
        return
 
    for i in range(s,6+1):
        dice[n] = i
        Dice2(n+1, i)
 
 
def Dice3(n):
    # 순열
    if n >= N:
        print(*dice)
        return
 
    for i in range(1,6+1):
        if sel[i]: continue
        dice[n] = i
        sel[i] = 1
        Dice3(n+1)
        sel[i] = 0

def Solve():
    # 주사위 던지기 순서번호 : 0 ~ N-1
    if M == 1: Dice1(0) # n : 주사위 던지기 순서번호
    elif M == 2: Dice2(0, 1) # n : 주사위 던지기 순서번호, s : 선택 시작 숫자
    elif M == 3: Dice3(0) # n : 주사위 던지기 순서번호

dice = [0] * N  # dice[n] : n번째 던지 주사위의 숫자
sel = [0] * (7) # sel[n] : n숫자의 현재 진행중인 경우의 수에서 선택 여부 (순열 경우의 수 시도에서 사용)
Solve()