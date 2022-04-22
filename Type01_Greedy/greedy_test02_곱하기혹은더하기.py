# 곱하기 혹은 더하기
# 시작: 20:22
# 종료: 20:34
# 제한시간: 30분 (-18)

# 각자리가 0~9로 이루어진 문자열 S
# 왼쪽부터 + 혹은 x를 하여 가장 큰수 만들기
# 1 <= s의 길이 <=  20

# 풀이 1)
# 0이나 1은 더하기, 2부터는 무조건 곱셈을 해야함
# 기존 값이 0이면 덧셈을 해야함

# s = [int(num) for num in input()]
# s.sort()
# # 정답 초기화
# answer = 0
# for n in s:
#    if n <= 1 or answer == 0:
#        answer += n
#    else:
#        answer *= n
# print(answer)
    
# Solution
# 문제를 제대로안읽었음!!
# 숫자는 입력된 순서대로 연산되어야함

data = input()

result = int(data[0])

for num in data[1:]:
    num = int(num)
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
        
