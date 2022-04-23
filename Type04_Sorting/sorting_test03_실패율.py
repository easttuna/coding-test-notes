# 전체 스테이지의 개수 N
# 사용자가 현재 멈춰았는 스테이지의 번호가 담길 배열 stages
# 배열의 길이 -> 사용자 수
# 배열에서 스테이지가 존재하는 횟수 -> 머물러있는 사람
# 배열 길이 - (1스테이지사람, 2스테이지사람)
# x 스테이지 인원 = len(stages) - (x-1인원, x-2 인원...)

from collections import Counter


def solution(N, stages):
    num_user = len(stages)  # 어레이의 길이가 유저의 숫자
    counter = Counter(stages)  # 각 스테이지 단계에 머물러 있는 유저 숫자 카운트
    
    f_rates = []  # 실패율을 저장하기 위한 리스트
    for s in range(1, N+1):  # 1단계 ~ N단계의 스테이지에 대해 반복
        
        if num_user == 0:  # 잔여 유저의 수가 0일 때는 실패율이 0
            f_rates.append(0)
            continue
            
        in_stage = counter[s]  # 현 스테이지 s에 있는 인원
        rate = (in_stage / num_user)  # 잔여 인원 중 아직 클리어하지 못한 인원으로 실패율
        f_rates.append(rate)
        
        num_user -= in_stage  # 다음 단계까지 올라가는 인원 계산
    # 실패율은 내림차순, 각 스테이지에 대해서는 오름차순으로 정렬
    answer = [s for s,f in sorted(zip(range(1, N+1), f_rates), key=lambda x: (-x[1], x[0]))]
    return answer