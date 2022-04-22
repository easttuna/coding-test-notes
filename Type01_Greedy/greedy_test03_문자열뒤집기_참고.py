
num_list = input()
res = [ item for item in num_list.split(num_list[0]) if item ]
print(len(res))