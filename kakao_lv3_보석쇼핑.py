from math import inf
from collections import defaultdict

def solution(gems):
    answer = []
    
    min_size = inf
    TOTAL_CNT = len(set(gems))  # 존재하는 보석의 종류
    MAX_IDX = len(gems) - 1  # 진열대의 마지막 인덱스
    
    cnt_dict = defaultdict(int)  # 보석별 구간내 빈도
    
    left = 0
    right = 0
    cnt_dict[gems[left]] += 1
    
    while  left <= MAX_IDX and right <=  MAX_IDX:
        current_cnt = len(cnt_dict)
        
        if current_cnt == TOTAL_CNT:
            if (right - left) < min_size:  # 새로운 최적 구간 발견 시.
                min_size = (right - left)
                answer = [left+1, right+1]
                
            left_gem = gems[left]
            cnt_dict[left_gem] -= 1

            if cnt_dict[left_gem] == 0:
                cnt_dict.pop(left_gem)
            left += 1
            
        else:  # current_cnt < total_cnt
            right += 1
            if right > MAX_IDX:
                break
            cnt_dict[gems[right]] += 1
    
    return answer

print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))