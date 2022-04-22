# 16:08
# 제한 20분 ()

s = 'K1KA5CB7'

num = 0
alphas = []

for letter in s:
    if letter.isnumeric():
        num += int(letter)
    else:
        alphas.append(letter)

num = 0 if num==0 else str(num) 

print(''.join(sorted(alphas)) + num)
