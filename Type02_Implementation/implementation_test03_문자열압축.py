# 긴 길이 압축이 가능하다면 --> 
# 원래 문자열 길이 l
# 압축이 유의미한 길이는 (l//2)
# 반복되는 숫자를 뒤에 더해준다고 생각하자!! (ex. ab2 cd3...)

def solution(s):
    length = len(s)
    # 각 경우별 압축 문자열 길이 저장
    answer = length

    # 유의미한 모든 압축 길이에 대해 반복
    for chunksize in range(1, length//2 + 1):
        total_count = 0  # 누적 문자열 수
        temp_count = 1  # 반복문자 카운트
        last_val = None  # 이전 값

        for idx in range(0,length, chunksize):
            current_val = s[idx:idx+chunksize]  # 압축대상
            # 기존과 동일한 값이 반복될 시
            if current_val == last_val:
                temp_count += 1  # temp_count + 1
            # 기존과 다른 값이 들어오면
            else:
                if temp_count >= 2:
                    total_count += len(str(temp_count))  # 누적된 temp_count의 문자열 길이를 더해줌 (0일경우 제외)
                temp_count = 1  # temp_count 초기화
                # 새롭게 들어온값길이 더해줌
                total_count += len(current_val)
                
            last_val = current_val  # 현재 값을 저장
            
        # 마지막에 2이상의 temp_count가 남은 경우 처리
        if temp_count >= 2:
            total_count += len(str(temp_count))

        # 현재 정답이 기존보다 작다면 업데이트
        if total_count < answer:
            answer = total_count
        total_count = 0  # 카운트 초기화
    
    return answer