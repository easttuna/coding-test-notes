# https://programmers.co.kr/learn/courses/30/lessons/43165
# 각 숫자는 양혹은 음의 부호를 가질 수 있음
# 부호를 부여하며 숫자를 모두 소진한 경우의 합이 타겟.
# 숫자가 n개 일 시, 2^n개의 조합이 나옴 -> 백만가량
# 리스트에 숫자를 넣고, 하나씩 더하거나 빼며 경우에 추가

def solution(numbers, target):
    num_sums = []
    n = numbers.pop()
    # 첫 숫자를 (양,음)의 경우로 넣어 초기화
    num_sums.extend([n, -n])
    
    # 리스트의 숫자가 소진될때까지 반복
    while numbers:
        x = numbers.pop()  # 한 숫자를 꺼내서
        # 기존 합리스트에 더하거나, 뺀 리스트를 생성해 합쳐줌
        num_sums = [s+x for s in num_sums] + [s+(-x) for s in num_sums]
    
    return num_sums.count(target)