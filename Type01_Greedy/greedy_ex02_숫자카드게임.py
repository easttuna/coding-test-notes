import numpy as np

# 입력
# 첫째줄에 카드가 놓인 행열의 개수, N M
# 둘째줄부터 N개 줄에 걸쳐 각 행 입력 받음
# n, m = map(int, input().split())

# cards = list()
# for _ in range(n):
#   row = list(map(int, input().split()))
#   cards.append(row)

# cards = np.array(cards)
# card_selected = cards.min(axis=1).max()
# print(card_selected)


n, m = map(int, input().split())
cards = np.zeros((n,m), dtype=int)

for idx in range(n):
  row = list(map(int, input().split()))
  cards[idx] = row

cards = np.array(cards)
card_selected = cards.min(axis=1).max()
print(card_selected)