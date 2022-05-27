def solution(n, k, cmd):
    
    exist = [True for _ in range(n)]
    pointer = k
    
    trash_bin =  list()  # 최근에 제거된 것을 복구하기 위함
    
    for command in cmd:
        command = command.split()
        if len(command) == 2:  # 이동명령
            delta = 1 if command[0] == 'D' else -1
            cnt = int(command[1])
            
            while cnt > 0:
                pointer += delta
                if exist[pointer] == True:
                    cnt -= 1
                else:
                    continue
        else:
            if command[0] == 'C':
                exist[pointer] = False  # 삭제
                trash_bin.append(pointer)  
                
                delta = 1 if True in exist[pointer+1:] else -1
                while True:
                    pointer += delta
                    if exist[pointer] == True:
                        break
                        
            else:  # command == 'Z'
                exist[trash_bin.pop()] = True                      
    answer = ''
    for b in exist:
        if b:
            answer += 'O'
        else:
            answer += 'X'
    return answer

case = 8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"],

print(solution(*case))
